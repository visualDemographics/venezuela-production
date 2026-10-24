# Clean & Harmonized Datasets Documentation (`datasets/`)

In accordance with `responsible-research` and `responsible-demographics`, all datasets in `datasets/` are deterministically generated from primary sources in `rawdata/` via `src/data_preparation.py`.

---

## 1. Summary of Active Datasets

| Dataset File | Rows | Columns | Temporal Coverage | Methodological Status | Primary Source Entities |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [`venezuela_sectoral_panel_1970_2026.csv`](file:///Users/selle/Documents/GitHub/venezuela-production/datasets/venezuela_sectoral_panel_1970_2026.csv) | 57 | 53 | 1970–2026 | `Amtliche_Registerstatistik` | OPEC, EIA, worldsteel, USGS, FAOSTAT, UN SNAAMA, WB WDI, UN WPP, ENCOVI |
| [`venezuela_structural_breaks_1970_2026.csv`](file:///Users/selle/Documents/GitHub/venezuela-production/datasets/venezuela_structural_breaks_1970_2026.csv) | 10 | 10 | 1974–2026 | `Amtliche_Registerstatistik` | BCV, CNE, Monaldi et al., Rodriguez, Baptista, Krivoy |
| [`venezuela_peer_panel_1970_2026.csv`](file:///Users/selle/Documents/GitHub/venezuela-production/datasets/venezuela_peer_panel_1970_2026.csv) | 228 | 11 | 1970–2026 | `Amtliche_Registerstatistik` | OPEC, worldsteel, UN SNAAMA (Venezuela, Brazil, Colombia, Chile) |
| [`venezuela_demographics_denominators.csv`](file:///Users/selle/Documents/GitHub/venezuela-production/datasets/venezuela_demographics_denominators.csv) | 57 | 17 | 1970–2026 | `Amtliche_Registerstatistik` | UN WPP (2024 Revision), UCAB ENCOVI, R4V Inter-Agency Platform |
| [`literature_empirical_benchmarks.csv`](file:///Users/selle/Documents/GitHub/venezuela-production/datasets/literature_empirical_benchmarks.csv) | 23 | 18 | 1970–2026 | `Amtliche_Registerstatistik` / `Laengsschnitt` | Audited benchmark citations with verbatim quotes and coordinates |

---

## 2. Sectoral Panel Data Dictionary (`venezuela_sectoral_panel_1970_2026.csv`)

### Temporal & Demographic Denominator Fields:
- `year`: Gregorian calendar year ($1970 \le t \le 2026$).
- `tier0_precrisis_unadjusted_pop`: Pre-crisis linear population projection ($>34\text{M}$ by 2024) assuming no mass displacement shock.
- `tier1_migration_adjusted_population`: De facto resident population based on UN WPP 2024 and ENCOVI demographic revisions ($\sim 28.4\text{M}$ in 2024), accounting for the net exodus of $>7.7\text{ million}$ Venezuelans.
- `working_age_pop_15_64`: Resident population aged 15–64 (Tier 2 active labor pool).
- `r4v_cumulative_emigrants`: Cumulative Venezuelan diaspora worldwide (R4V registry).

### Sector 1: Crude Oil & Hydrocarbons:
- `opec_secondary_kbd`: Crude oil extraction according to OPEC secondary sources (thousand bbl/day).
- `opec_direct_kbd`: Crude oil extraction self-reported by the Ministry of Petroleum / PDVSA.
- `eia_crude_kbd`: Crude oil extraction reported by the U.S. Energy Information Administration.
- `annual_production_mb`: Total annual physical extraction (million barrels).
- `oil_bbl_per_cap_tier0`: Annual barrels per capita under unadjusted Tier 0 projection ($Y_t / P_{t,\text{Tier 0}}$).
- `oil_bbl_per_cap_tier1`: Annual barrels per capita under migration-adjusted Tier 1 population ($Y_t / P_{t,\text{Tier 1}}$).
- `oil_bbl_per_worker_tier2`: Annual barrels per working-age resident ($Y_t / P_{t,\text{Tier 2}}$).

### Sector 2: Crude Steel & Metallurgy:
- `venezuela_crude_steel_kt`: Total national crude steel production (thousand metric tons).
- `sidor_liquid_steel_kt`: SIDOR Matanzas plant liquid steel production (thousand metric tons).
- `sidor_installed_capacity_kt`: Effective continuous casting capacity ($4{,}300\text{ kt/yr}$).
- `sidor_capacity_utilization_pct`: Percentage capacity utilization of SIDOR.
- `steel_kg_per_cap_tier0`: Steel output in kg per capita under Tier 0.
- `steel_kg_per_cap_tier1`: Steel output in kg per capita under Tier 1.
- `steel_kg_per_worker_tier2`: Steel output in kg per working-age resident under Tier 2.

### Sector 3: Primary Aluminum & Upstream Minerals:
- `primary_aluminum_total_kt`: Total primary unalloyed aluminum output (thousand metric tons).
- `alcasa_aluminum_kt`: CVG Alcasa output (kt).
- `venalum_aluminum_kt`: CVG Venalum output (kt).
- `bauxite_kt`: CVG Bauxilum Los Pijiguaos mine extraction (kt).
- `alumina_kt`: CVG Bauxilum Puerto Ordaz refinery output (kt).
- `aluminum_kg_per_cap_tier0`: Aluminum output in kg per capita under Tier 0.
- `aluminum_kg_per_cap_tier1`: Aluminum output in kg per capita under Tier 1.

### Sector 4: Industrial Forestry & Wood Products:
- `wood_industrial_roundwood_m3`: FAOSTAT Industrial roundwood physical production ($\text{m}^3$).
- `wood_sawnwood_m3`: FAOSTAT Sawnwood production ($\text{m}^3$).
- `wood_m3_per_1k_cap_tier0`: Industrial roundwood in $\text{m}^3$ per $1{,}000$ residents under Tier 0.
- `wood_m3_per_1k_cap_tier1`: Industrial roundwood in $\text{m}^3$ per $1{,}000$ residents under Tier 1.

### Sector 5: Services & Value-Added:
- `services_gva_constant_2015_usd_b`: Gross value-added of services in billion constant 2015 USD (UN SNAAMA / World Bank WDI).
- `services_gva_ppp_constant_2017_int_usd_b`: Services GVA in billion constant 2017 PPP international dollars.
- `services_share_gdp_pct`: Services share of total GDP (%).
- `employment_services_pct_total`: Services share of total employment (% modeled ILO).
- `services_real_gva_per_cap_tier1_usd`: Services real value-added per resident in constant 2015 USD.
- `services_labor_productivity_idx_2015_100`: Index of real services labor productivity ($2015 = 100$).

### Multi-Sector Normalized Indices:
- `idx_[sector]_per_cap_1970`: Normalized per-capita Tier 1 physical output index ($1970 = 100$).
- `idx_[sector]_per_cap_1998`: Normalized per-capita Tier 1 physical output index ($1998 = 100$).
- `idx_composite_per_cap_1970`: Equally-weighted composite per-capita output index across all 5 sectors ($1970 = 100$).
- `idx_composite_per_cap_1998`: Equally-weighted composite per-capita output index across all 5 sectors ($1998 = 100$).

