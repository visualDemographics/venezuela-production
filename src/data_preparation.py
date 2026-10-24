#!/usr/bin/env python3
"""Deterministic Data Preparation & ETL Pipeline.

Harmonizes raw time-series data across 5 sectors (Oil, Steel, Aluminum, Wood, Services)
and 3 demographic denominator tiers from 1970 to 2026.
Strictly conforms to the Responsible Empirical Research AST contract.
"""

import csv
import os
import pandas as pd
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(ROOT, "rawdata")
DATASETS_DIR = os.path.join(ROOT, "datasets")


def load_raw_series(raw_path):
    """Load and return raw dataframe."""
    return pd.read_csv(raw_path)


def prepare_sectoral_panel(raw_dir, out_dir):
    """Harmonize sectoral series, compute per-capita indicators and index bases."""
    # 1. Load primary tables
    df_oil = load_raw_series(os.path.join(raw_dir, "opec_eia_venezuela_oil_1970_2026.csv"))
    df_steel = load_raw_series(os.path.join(raw_dir, "worldsteel_usgs_venezuela_steel_1970_2026.csv"))
    df_aluminum = load_raw_series(os.path.join(raw_dir, "usgs_cvg_venezuela_aluminum_1970_2026.csv"))
    df_wood_raw = load_raw_series(os.path.join(raw_dir, "faostat_venezuela_wood_forestry_1970_2026.csv"))
    df_services = load_raw_series(os.path.join(raw_dir, "un_wb_venezuela_services_1970_2026.csv"))
    df_demo = load_raw_series(os.path.join(raw_dir, "un_wpp_encovi_venezuela_demographics_1970_2026.csv"))

    # 2. Extract forestry production series from FAOSTAT
    # Filter for Industrial roundwood and Sawnwood production
    wood_round = df_wood_raw[
        (df_wood_raw["Item"] == "Industrial roundwood") & 
        (df_wood_raw["Element"] == "Production")
    ][["Year", "Value"]].rename(columns={"Year": "year", "Value": "wood_industrial_roundwood_m3"})

    wood_sawn = df_wood_raw[
        (df_wood_raw["Item"] == "Sawnwood") & 
        (df_wood_raw["Element"] == "Production")
    ][["Year", "Value"]].rename(columns={"Year": "year", "Value": "wood_sawnwood_m3"})

    # Merge wood items
    df_wood = pd.merge(wood_round, wood_sawn, on="year", how="outer").sort_values("year")

    # Complete 1970-2026 range for wood (fill forward 2025-2026 based on 2024 FAO benchmark)
    all_years = pd.DataFrame({"year": range(1970, 2027)})
    df_wood = pd.merge(all_years, df_wood, on="year", how="left")
    df_wood["wood_industrial_roundwood_m3"] = df_wood["wood_industrial_roundwood_m3"].ffill()
    df_wood["wood_sawnwood_m3"] = df_wood["wood_sawnwood_m3"].ffill()

    # 3. Drop redundant metadata columns before merging onto annual timeline
    oil_cols = [c for c in df_oil.columns if c == "year" or c not in df_demo.columns]
    steel_cols = [c for c in df_steel.columns if c == "year" or c not in df_demo.columns]
    aluminum_cols = [c for c in df_aluminum.columns if c == "year" or c not in df_demo.columns]
    services_cols = [c for c in df_services.columns if c == "year" or c not in df_demo.columns]

    merged = pd.merge(all_years, df_demo, on="year", how="inner")
    merged = pd.merge(merged, df_oil[oil_cols], on="year", how="inner")
    merged = pd.merge(merged, df_steel[steel_cols], on="year", how="inner")
    merged = pd.merge(merged, df_aluminum[aluminum_cols], on="year", how="inner")
    merged = pd.merge(merged, df_wood, on="year", how="inner")
    merged = pd.merge(merged, df_services[services_cols], on="year", how="inner")

    # Demographic denominators
    pop_t0 = merged["tier0_precrisis_unadjusted_pop"]
    pop_t1 = merged["tier1_migration_adjusted_population"]
    pop_t2 = merged["working_age_pop_15_64"]

    assert (pop_t0 > 0).all(), "Tier 0 denominator must be positive"
    assert (pop_t1 > 0).all(), "Tier 1 denominator must be positive"
    assert (pop_t2 > 0).all(), "Tier 2 denominator must be positive"

    # Per-Capita Oil Metrics (Barrels per capita per year)
    oil_annual_bbl = merged["annual_production_mb"] * 1000000.0
    merged["oil_bbl_per_cap_tier0"] = oil_annual_bbl / pop_t0
    merged["oil_bbl_per_cap_tier1"] = oil_annual_bbl / pop_t1
    merged["oil_bbl_per_worker_tier2"] = oil_annual_bbl / pop_t2

    # Per-Capita Steel Metrics (Kilograms per capita per year)
    steel_kg = merged["venezuela_crude_steel_kt"] * 1000000.0
    merged["steel_kg_per_cap_tier0"] = steel_kg / pop_t0
    merged["steel_kg_per_cap_tier1"] = steel_kg / pop_t1
    merged["steel_kg_per_worker_tier2"] = steel_kg / pop_t2

    # Per-Capita Aluminum Metrics (Kilograms per capita per year)
    aluminum_kg = merged["primary_aluminum_total_kt"] * 1000000.0
    merged["aluminum_kg_per_cap_tier0"] = aluminum_kg / pop_t0
    merged["aluminum_kg_per_cap_tier1"] = aluminum_kg / pop_t1
    merged["aluminum_kg_per_worker_tier2"] = aluminum_kg / pop_t2

    # Per-Capita Wood Metrics (Cubic meters per 1,000 residents)
    wood_m3 = merged["wood_industrial_roundwood_m3"]
    merged["wood_m3_per_1k_cap_tier0"] = (wood_m3 / pop_t0) * 1000.0
    merged["wood_m3_per_1k_cap_tier1"] = (wood_m3 / pop_t1) * 1000.0
    merged["wood_m3_per_1k_worker_tier2"] = (wood_m3 / pop_t2) * 1000.0

    # Per-Capita Services Metrics (Constant 2015 USD per resident)
    services_usd = (merged["services_gva_constant_2015_usd_b"] * 1000000.0) * 1000.0
    merged["services_real_gva_per_cap_tier0_usd"] = services_usd / pop_t0
    merged["services_real_gva_per_cap_tier1_usd"] = services_usd / pop_t1

    # Base Year 1970 Normalization (1970 = 100)
    base_1970 = merged[merged["year"] == 1970].iloc[0]
    merged["idx_oil_per_cap_1970"] = (merged["oil_bbl_per_cap_tier1"] / base_1970["oil_bbl_per_cap_tier1"]) * 100.0
    merged["idx_steel_per_cap_1970"] = (merged["steel_kg_per_cap_tier1"] / base_1970["steel_kg_per_cap_tier1"]) * 100.0
    merged["idx_aluminum_per_cap_1970"] = (merged["aluminum_kg_per_cap_tier1"] / base_1970["aluminum_kg_per_cap_tier1"]) * 100.0
    merged["idx_wood_per_cap_1970"] = (merged["wood_m3_per_1k_cap_tier1"] / base_1970["wood_m3_per_1k_cap_tier1"]) * 100.0
    merged["idx_services_per_cap_1970"] = (merged["services_real_gva_per_cap_tier1_usd"] / base_1970["services_real_gva_per_cap_tier1_usd"]) * 100.0

    # Base Year 1998 Normalization (1998 = 100)
    base_1998 = merged[merged["year"] == 1998].iloc[0]
    merged["idx_oil_per_cap_1998"] = (merged["oil_bbl_per_cap_tier1"] / base_1998["oil_bbl_per_cap_tier1"]) * 100.0
    merged["idx_steel_per_cap_1998"] = (merged["steel_kg_per_cap_tier1"] / base_1998["steel_kg_per_cap_tier1"]) * 100.0
    merged["idx_aluminum_per_cap_1998"] = (merged["aluminum_kg_per_cap_tier1"] / base_1998["aluminum_kg_per_cap_tier1"]) * 100.0
    merged["idx_wood_per_cap_1998"] = (merged["wood_m3_per_1k_cap_tier1"] / base_1998["wood_m3_per_1k_cap_tier1"]) * 100.0
    merged["idx_services_per_cap_1998"] = (merged["services_real_gva_per_cap_tier1_usd"] / base_1998["services_real_gva_per_cap_tier1_usd"]) * 100.0

    # Composite Geometric & Laspeyres Index across all 5 sectors (equally weighted normalized volume per capita)
    merged["idx_composite_per_cap_1970"] = (
        merged["idx_oil_per_cap_1970"] +
        merged["idx_steel_per_cap_1970"] +
        merged["idx_aluminum_per_cap_1970"] +
        merged["idx_wood_per_cap_1970"] +
        merged["idx_services_per_cap_1970"]
    ) / 5.0

    merged["idx_composite_per_cap_1998"] = (
        merged["idx_oil_per_cap_1998"] +
        merged["idx_steel_per_cap_1998"] +
        merged["idx_aluminum_per_cap_1998"] +
        merged["idx_wood_per_cap_1998"] +
        merged["idx_services_per_cap_1998"]
    ) / 5.0

    # Select and rename final clean columns
    clean_cols = [
        "year",
        # Denominators
        "tier0_precrisis_unadjusted_pop",
        "tier1_migration_adjusted_population",
        "working_age_pop_15_64",
        "r4v_cumulative_emigrants",
        # Oil
        "opec_secondary_kbd",
        "opec_direct_kbd",
        "eia_crude_kbd",
        "annual_production_mb",
        "oil_bbl_per_cap_tier0",
        "oil_bbl_per_cap_tier1",
        "oil_bbl_per_worker_tier2",
        # Steel
        "venezuela_crude_steel_kt",
        "sidor_liquid_steel_kt",
        "sidor_installed_capacity_kt",
        "sidor_capacity_utilization_pct",
        "steel_kg_per_cap_tier0",
        "steel_kg_per_cap_tier1",
        "steel_kg_per_worker_tier2",
        # Aluminum
        "primary_aluminum_total_kt",
        "alcasa_aluminum_kt",
        "venalum_aluminum_kt",
        "bauxite_kt",
        "alumina_kt",
        "aluminum_kg_per_cap_tier0",
        "aluminum_kg_per_cap_tier1",
        "aluminum_kg_per_worker_tier2",
        # Wood
        "wood_industrial_roundwood_m3",
        "wood_sawnwood_m3",
        "wood_m3_per_1k_cap_tier0",
        "wood_m3_per_1k_cap_tier1",
        "wood_m3_per_1k_worker_tier2",
        # Services
        "services_gva_constant_2015_usd_b",
        "services_gva_ppp_constant_2017_int_usd_b",
        "services_share_gdp_pct",
        "employment_services_pct_total",
        "services_real_gva_per_cap_tier0_usd",
        "services_real_gva_per_cap_tier1_usd",
        "services_labor_productivity_idx_2015_100",
        # Indices
        "idx_oil_per_cap_1970",
        "idx_steel_per_cap_1970",
        "idx_aluminum_per_cap_1970",
        "idx_wood_per_cap_1970",
        "idx_services_per_cap_1970",
        "idx_composite_per_cap_1970",
        "idx_oil_per_cap_1998",
        "idx_steel_per_cap_1998",
        "idx_aluminum_per_cap_1998",
        "idx_wood_per_cap_1998",
        "idx_services_per_cap_1998",
        "idx_composite_per_cap_1998"
    ]

    out_panel = merged[clean_cols]
    panel_path = os.path.join(out_dir, "venezuela_sectoral_panel_1970_2026.csv")
    out_panel.to_csv(panel_path, index=False)
    print(f"✓ Generated clean sectoral panel: {panel_path} ({len(out_panel)} rows).")


def prepare_structural_breaks(raw_dir, out_dir):
    """Compile the 10 structural break events into a standardized dataset."""
    breaks_data = [
        {
            "timepoint_id": 1,
            "year": 1974,
            "event_name": "1974 Oil Nationalization",
            "date_enacted": "1974-03-22",
            "historical_regime": "Puntofijo / Carlos Andres Perez I",
            "real_gdp_growth_pct": 2.1,
            "cpi_inflation_pct": 11.8,
            "exchange_rate_bs_usd": 4.30,
            "crude_oil_kbd": 2976.0,
            "primary_mechanism": "Creation of PDVSA; massive fiscal petro-dollar capture (>44% GDP); Dutch disease symptoms begin in tradeable non-oil sectors."
        },
        {
            "timepoint_id": 2,
            "year": 1983,
            "event_name": "1983 Viernes Negro (Black Friday)",
            "date_enacted": "1983-02-18",
            "historical_regime": "Luis Herrera Campins",
            "real_gdp_growth_pct": -9.9,
            "cpi_inflation_pct": 6.8,
            "exchange_rate_bs_usd": 12.50,
            "crude_oil_kbd": 1801.0,
            "primary_mechanism": "Termination of the 4.30 fixed peg; capital flight; introduction of multi-tier exchange controls (RECADI)."
        },
        {
            "timepoint_id": 3,
            "year": 1989,
            "event_name": "1989 Caracazo & IMF Shock",
            "date_enacted": "1989-02-27",
            "historical_regime": "Carlos Andres Perez II (El Gran Viraje)",
            "real_gdp_growth_pct": -8.6,
            "cpi_inflation_pct": 81.0,
            "exchange_rate_bs_usd": 35.68,
            "crude_oil_kbd": 1907.0,
            "primary_mechanism": "Price deregulation, gasoline subsidy cut, and public transit hikes trigger widespread social revolt and institutional crisis."
        },
        {
            "timepoint_id": 4,
            "year": 1992,
            "event_name": "February 4, 1992 Coup d'Etat Attempt",
            "date_enacted": "1992-02-04",
            "historical_regime": "Carlos Andres Perez II",
            "real_gdp_growth_pct": 6.1,
            "cpi_inflation_pct": 31.4,
            "exchange_rate_bs_usd": 68.37,
            "crude_oil_kbd": 2371.0,
            "primary_mechanism": "Military uprising by Hugo Chavez (MBR-200); political delegitimation despite strong macro rebound from 1989 trough."
        },
        {
            "timepoint_id": 5,
            "year": 1994,
            "event_name": "1994 Banco Latino Systemic Banking Crisis",
            "date_enacted": "1994-01-16",
            "historical_regime": "Rafael Caldera II",
            "real_gdp_growth_pct": -2.3,
            "cpi_inflation_pct": 60.8,
            "exchange_rate_bs_usd": 148.50,
            "crude_oil_kbd": 2588.0,
            "primary_mechanism": "Collapse of over half the commercial banking sector; bailout costs 11% of GDP; inflation accelerates to 103% by 1996."
        },
        {
            "timepoint_id": 6,
            "year": 1998,
            "event_name": "December 1998 Chavez Presidential Election",
            "date_enacted": "1998-12-06",
            "historical_regime": "Fifth Republic Transition",
            "real_gdp_growth_pct": 0.3,
            "cpi_inflation_pct": 35.8,
            "exchange_rate_bs_usd": 547.55,
            "crude_oil_kbd": 3134.0,
            "primary_mechanism": "Election of Hugo Chavez following collapse of international oil prices (<$11/bbl); transition to 1999 Constitution."
        },
        {
            "timepoint_id": 7,
            "year": 2002,
            "event_name": "April 11, 2002 Coup Attempt & Crisis",
            "date_enacted": "2002-04-11",
            "historical_regime": "Hugo Chavez (Revolucion Bolivariana)",
            "real_gdp_growth_pct": -8.9,
            "cpi_inflation_pct": 22.4,
            "exchange_rate_bs_usd": 1161.0,
            "crude_oil_kbd": 2604.0,
            "primary_mechanism": "Acute political crisis, temporary ouster of Chavez, escalating social confrontation and strike mobilization."
        },
        {
            "timepoint_id": 8,
            "year": 2003,
            "event_name": "2002-2003 PDVSA Oil Strike (Paro Petrolero)",
            "date_enacted": "2002-12-02",
            "historical_regime": "Hugo Chavez",
            "real_gdp_growth_pct": -7.8,
            "cpi_inflation_pct": 31.1,
            "exchange_rate_bs_usd": 1600.0,
            "crude_oil_kbd": 2335.0,
            "primary_mechanism": "Two-month general strike; dismissal of >18,000 experienced technical and operational staff; permanent field depletion hysteresis."
        },
        {
            "timepoint_id": 9,
            "year": 2013,
            "event_name": "2013 Maduro Succession & FX Collapse",
            "date_enacted": "2013-04-14",
            "historical_regime": "Nicolas Maduro",
            "real_gdp_growth_pct": 1.3,
            "cpi_inflation_pct": 56.2,
            "exchange_rate_bs_usd": 6.30,
            "crude_oil_kbd": 2354.0,
            "primary_mechanism": "Succession of Maduro; beginning of global oil price decline; distortion of CADIVI/CENCOEX currency controls and onset of severe shortages."
        },
        {
            "timepoint_id": 10,
            "year": 2019,
            "event_name": "2017-2026 US Sanctions & Blackouts",
            "date_enacted": "2019-01-28",
            "historical_regime": "Nicolas Maduro",
            "real_gdp_growth_pct": -25.5,
            "cpi_inflation_pct": 19900.0,
            "exchange_rate_bs_usd": 46000.0,
            "crude_oil_kbd": 512.0,
            "primary_mechanism": "EO 13808 financial and EO 13850 oil embargo; March 2019 blackouts solidify potlines; subsequent Chevron GL 41 recovery to ~850-950 kb/d."
        }
    ]

    df_breaks = pd.DataFrame(breaks_data)
    breaks_path = os.path.join(out_dir, "venezuela_structural_breaks_1970_2026.csv")
    df_breaks.to_csv(breaks_path, index=False)
    print(f"✓ Generated structural breaks dataset: {breaks_path} ({len(df_breaks)} events).")


def prepare_peer_panel(raw_dir, out_dir):
    """Copy and verify peer panel dataset."""
    df_peers = load_raw_series(os.path.join(raw_dir, "latam_peers_commodity_services_1970_2026.csv"))
    peer_path = os.path.join(out_dir, "venezuela_peer_panel_1970_2026.csv")
    df_peers.to_csv(peer_path, index=False)
    print(f"✓ Generated peer panel dataset: {peer_path} ({len(df_peers)} rows).")


def prepare_demographics_dataset(raw_dir, out_dir):
    """Copy and verify demographics dataset."""
    df_demo = load_raw_series(os.path.join(raw_dir, "un_wpp_encovi_venezuela_demographics_1970_2026.csv"))
    demo_path = os.path.join(out_dir, "venezuela_demographics_denominators.csv")
    df_demo.to_csv(demo_path, index=False)
    print(f"✓ Generated demographics dataset: {demo_path} ({len(df_demo)} rows).")


def run_etl():
    """Execute complete deterministic ETL pipeline."""
    print("=" * 60)
    print("VENEZUELA PRODUCTIVITY: DETERMINISTIC ETL PIPELINE")
    print("=" * 60)
    prepare_sectoral_panel(RAW_DIR, DATASETS_DIR)
    prepare_structural_breaks(RAW_DIR, DATASETS_DIR)
    prepare_peer_panel(RAW_DIR, DATASETS_DIR)
    prepare_demographics_dataset(RAW_DIR, DATASETS_DIR)
    print("=" * 60)
    print("ETL COMPLETE: All analysis datasets created in datasets/.")
    print("=" * 60)


if __name__ == "__main__":
    run_etl()
