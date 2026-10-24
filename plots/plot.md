# Scientific Documentation & Validity Audit of Generated Plots (`plots/`)

In strict accordance with the `responsible-research` protocol, every visual figure produced by `src/modeling.py` is systematically audited below with its input dataset, mathematical formulations, statistical classification, confidence intervals, and methodological boundaries.

---

## 1. Summary of Generated Figures

### A. Dedicated Single-Commodity Descriptive Time Series:
| Figure File | Sector / Scope | Visual Layout | Methodological Classification |
| :--- | :--- | :--- | :--- |
| [`commodity_oil_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_oil_1970_2026.png) | Crude Oil & Hydrocarbons | 2-Panel Stacked (Extraction kb/d & bbl/capita) | `Amtliche_Registerstatistik` / Descriptive |
| [`commodity_steel_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_steel_1970_2026.png) | Crude Steel (SIDOR / CVG) | 2-Panel Stacked (Crude Steel kt & kg/capita) | `Amtliche_Registerstatistik` / Descriptive |
| [`commodity_aluminum_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_aluminum_1970_2026.png) | Primary Aluminum (CVG) | 2-Panel Stacked (Primary Alum kt & kg/capita) | `Amtliche_Registerstatistik` / Descriptive |
| [`commodity_wood_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_wood_1970_2026.png) | Industrial Forestry (FAOSTAT) | 2-Panel Stacked (Roundwood k m³ & m³/1k cap) | `Amtliche_Registerstatistik` / Descriptive |
| [`commodity_services_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_services_1970_2026.png) | Tertiary Services Value-Added | 2-Panel Stacked (GVA $B & $/cap + Productivity) | `Amtliche_Registerstatistik` / Descriptive |
| [`commodities_multi_sector_overview_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodities_multi_sector_overview_1970_2026.png) | Multi-Sector 5-Panel Overview | 5 Synchronized Panels (1970–2026 Absolute Volume) | Comprehensive Multi-Sector Synthesis |
| [`commodities_per_capita_overview_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodities_per_capita_overview_1970_2026.png) | Multi-Sector Per-Capita Overview | 5 Synchronized Panels (Per-Capita Tier 1 vs Tier 0) | Comprehensive Multi-Sector Synthesis / Nennerproblem |

### B. Econometric & Causal Decomposition Figures:
| Figure File | Visual Type | Sector / Scope | Methodological Classification |
| :--- | :--- | :--- | :--- |
| [`panel_a_sectoral_collapse.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_a_sectoral_collapse.png) | Grouped Bar Chart | All 5 Sectors (Peak vs. 1998 vs. 2026) | `Amtliche_Registerstatistik` / Empirical Ratio |
| [`panel_b_multi_sector_trajectories.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_b_multi_sector_trajectories.png) | Multi-Line Time Series | 56-Year Indices (1970–2026) & 10 Historical Breaks | `Amtliche_Registerstatistik` / Index Standardization |
| [`panel_c_demographic_denominators.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_c_demographic_denominators.png) | Multi-Series Area / Line | Tier 0 vs. Tier 1 vs. Tier 2 Demographics | `Amtliche_Registerstatistik` / Nennerproblem |
| [`panel_d_tertiarization_employment.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_d_tertiarization_employment.png) | Dual-Axis Time Series | Services Value Added (% GDP) vs. Employment Share | `Amtliche_Registerstatistik` / Sectoral Shift |
| [`panel_e_joint_failure_model.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_e_joint_failure_model.png) | Bounded Bar Chart | Joint Failure Model ($M_{\text{ind}}$) & Fréchet Bounds | `Strukturelle_Modellkalibrierung` / Copula Bounds |
| [`panel_f_2d_production_surface.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_f_2d_production_surface.png) | 2D Contour Map (`viridis`) | Capex $\times$ Institutional Stability $\to$ Output | `Strukturelle_Modellkalibrierung` / Marginal Preserving |
| [`panel_g_extraction_decay_curve.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_g_extraction_decay_curve.png) | Parametric Fit vs. Peers | Crude Extraction Decay Curve vs. Colombia & Brazil | `Laengsschnitt_Registerkohorte` / Non-linear Fit |
| [`panel_h_econometric_regression.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_h_econometric_regression.png) | OLS Regression with 95% CIs | Steel Output vs. Services Labor Productivity ($N=57$) | `Laengsschnitt_Registerkohorte` / Econometric OLS |
| [`panel_i_causal_waterfall.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_i_causal_waterfall.png) | Sequential Causal Waterfall | Decomposition of 1998–2026 Output Collapse | `Kausale_Waterfall_Dekomposition` / Shapley $K!$ |
| [`venezuela_output_collapse_waterfall.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/venezuela_output_collapse_waterfall.png) | Standalone Causal Waterfall | 6-Stage Decomposition + Shapley Attribution Inset | `Kausale_Waterfall_Dekomposition` / Shapley $K!$ |
| [`venezuela_productivity_3x3_en.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/venezuela_productivity_3x3_en.png) | Composite 9-Panel Matrix | Unified $3 \times 3$ Synoptic Matrix (English) | Comprehensive Multi-Pillar Research Synthesis |
| [`venezuela_productivity_3x3_de.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/venezuela_productivity_3x3_de.png) | Composite 9-Panel Matrix | Unified $3 \times 3$ Synoptic Matrix (German) | Comprehensive Multi-Pillar Research Synthesis |

---

## 2. Dedicated Single-Commodity Descriptive Analysis

### 1. Crude Oil Production & Extraction Productivity ([`commodity_oil_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_oil_1970_2026.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `rawdata/opec_eia_venezuela_oil_1970_2026.csv`
- **Descriptive Visual Architecture**:
  - **Top Panel**: Uninterrupted annual time series of crude extraction (1970–2026) tracking OPEC Secondary Sources ($512\text{--}3{,}708\text{ kb/d}$), OPEC Direct Communication ($569\text{--}3{,}708\text{ kb/d}$), and U.S. EIA estimates ($527\text{--}3{,}754\text{ kb/d}$).
  - **Bottom Panel**: Per-capita physical output in barrels per resident per year ($\text{bbl/cap/yr}$), explicitly contrasting Tier 1 migration-adjusted resident population against Tier 0 unadjusted extrapolation ($>34\text{M}$) and Tier 2 working-age labor pool ($15\text{--}64$).
- **Documented Historical Timepoints**:
  - **1974/76**: Oil Nationalization & creation of PDVSA ($2{,}294\text{ kb/d}$ ceiling).
  - **1983**: Viernes Negro currency devaluation and OPEC production quotas ($1{,}801\text{ kb/d}$).
  - **1998**: Chávez presidential election during historic oil price slump ($<\$11\text{/bbl}$, Apertura peak $3{,}134\text{ kb/d}$).
  - **2002/03**: General strike (*Paro Petrolero*) and dismissal of $\sim 18{,}000$ engineers ($2{,}335\text{ kb/d}$ annual avg; monthly trough $250\text{ kb/d}$).
  - **2013**: Maduro transition plateau ($2{,}354\text{ kb/d}$) before late-2014 global price collapse.
  - **2017**: U.S. financial debt sanctions (EO 13808; $1{,}910\text{ kb/d}$).
  - **2019**: U.S. sectoral oil embargo (EO 13850) and nationwide electric blackouts ($796\text{ kb/d}$).
  - **2020**: Sanctions and pandemic trough ($512\text{ kb/d}$ annual avg; $392\text{ kb/d}$ July trough).
  - **2024–2026**: Chevron OFAC General License 41 rebound ($867\text{--}1{,}030\text{ kb/d}$).
- **Key Descriptive Statistics**:
  - Peak: 1970 ($3{,}708\text{ kb/d}$, $118.8\text{ bbl/cap/yr}$)
  - 1998 Baseline: $3{,}134\text{ kb/d}$ ($53.8\text{ bbl/cap/yr}$)
  - Nadir: 2020 ($512\text{ kb/d}$, $6.6\text{ bbl/cap/yr}$)
  - 2026 Current: $990\text{--}1{,}030\text{ kb/d}$ ($10.8\text{ bbl/cap/yr}$)
  - Net Peak-to-Current Collapse: **$-90.9\%$ per capita**.

---

### 2. Crude Steel & Iron Ore (SIDOR / CVG) ([`commodity_steel_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_steel_1970_2026.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `rawdata/worldsteel_usgs_venezuela_steel_1970_2026.csv`
- **Descriptive Visual Architecture**:
  - **Top Panel**: National crude steel output ($27\text{--}5{,}005\text{ kt}$), SIDOR plant liquid steel ($20\text{--}4{,}300\text{ kt}$), and installed continuous casting capacity ($4{,}300\text{ kt/yr}$).
  - **Bottom Panel**: Per-capita crude steel in kg/resident/year (Tier 1 vs. Tier 0) and per working-age resident.
- **Documented Historical Timepoints**:
  - **1975**: Iron ore nationalization (*CVG Ferrominera*) & launch of Plan IV EAF expansion.
  - **1997**: SIDOR privatization to Consorcio Amazonia (Ternium/Techint) for $\$1.20\text{B}$.
  - **2007**: All-time record apex ($5{,}005\text{ kt}$ national, $4{,}300\text{ kt}$ SIDOR, $100\%$ capacity utilization).
  - **2008**: Chávez expropriates and renationalizes SIDOR ("Sidor Socialista"); payroll surges from 5k to 19k.
  - **2010**: Guri hydroelectric rationing forces furnace shutdowns; private mini-mill Sidetur expropriated.
  - **2016**: Foreign exchange and refractory brick shortages drop national output below $560\text{ kt}$.
  - **2019**: March nationwide electrical grid failure cripples remaining active electric arc furnaces ($50\text{ kt}$).
  - **2022**: Historical trough of $27\text{ kt}$ ($0.4\%$ capacity utilization; worldsteel registers $0.0\text{ Mt}$).
  - **2024–2026**: Near-total paralysis ($32\text{--}35\text{ kt/yr}$, $<1\%$ utilization).
- **Key Descriptive Statistics**:
  - Peak: 2007 ($5{,}005\text{ kt}$, $182.5\text{ kg/cap/yr}$)
  - 1998 Baseline: $3{,}585\text{ kt}$ ($153.2\text{ kg/cap/yr}$)
  - Nadir: 2022 ($27\text{ kt}$, $1.0\text{ kg/cap/yr}$)
  - 2026 Current: $35\text{ kt}$ ($1.2\text{ kg/cap/yr}$)
  - Net Peak-to-Current Collapse: **$-99.3\%$ per capita**.

---

### 3. Primary Aluminum & Bauxite (ALCASA & VENALUM / CVG) ([`commodity_aluminum_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_aluminum_1970_2026.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `rawdata/usgs_cvg_venezuela_aluminum_1970_2026.csv`
- **Descriptive Visual Architecture**:
  - **Top Panel**: Primary unalloyed aluminum output ($8\text{--}642\text{ kt}$), CVG Venalum smelter ($8\text{--}441\text{ kt}$), CVG Alcasa ($0\text{--}210\text{ kt}$), and upstream bauxite/alumina refining.
  - **Bottom Panel**: Per-capita primary aluminum output (kg/resident/year: Tier 1 vs. Tier 0).
- **Documented Historical Timepoints**:
  - **1978**: Inauguration of CVG Venalum (CVG $80\%$, Japanese consortium $20\%$).
  - **1983**: Interalumina refinery commissioned ($1{,}900\text{ kt}$ capacity).
  - **1987**: Los Pijiguaos bauxite mine operational ($5.9\text{ Mt}$ capacity).
  - **1989**: Venalum Line 5 ("V Line") commissioned (capacity $430\text{ kt}$).
  - **1997**: All-time historical output record of $642.0\text{ kt}$; Venezuela ranks 12th globally.
  - **2001–2008**: High-volume export plateau averaging $612.6\text{ kt/yr}$.
  - **2009**: Guri El Niño drought; government mandates power rationing; Alcasa Line 1 permanently turned off.
  - **2013**: CADIVI currency rationing leads to severe shortages of petroleum coke, pitch, and cryolite.
  - **2019**: March nationwide blackout: power de-energized $>4$ hours; molten cryolite bath freezes solid inside reduction cells (irreversible destruction; output drops to $8\text{ kt}$).
  - **2020–2026**: Alcasa reduction cells dismantled for scrap; Venalum operates trace reactivated cells ($20\text{--}47\text{ kt/yr}$, $<5\%$ capacity).
- **Key Descriptive Statistics**:
  - Peak: 1997 ($642.0\text{ kt}$, $28.1\text{ kg/cap/yr}$)
  - 1998 Baseline: $570.0\text{ kt}$ ($24.4\text{ kg/cap/yr}$)
  - Nadir: 2019 ($8.0\text{ kt}$, $0.3\text{ kg/cap/yr}$)
  - 2026 Current: $32.0\text{ kt}$ ($1.1\text{ kg/cap/yr}$)
  - Net Peak-to-Current Collapse: **$-96.1\%$ per capita**.

---

### 4. Industrial Forestry & Wood Products (PROFORCA / FAOSTAT) ([`commodity_wood_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_wood_1970_2026.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `rawdata/faostat_venezuela_wood_forestry_1970_2026.csv`
- **Descriptive Visual Architecture**:
  - **Top Panel**: Industrial roundwood ($558\text{--}2{,}295\text{k m}^3$) and sawnwood ($137\text{--}439\text{k m}^3$) from FAOSTAT.
  - **Bottom Panel**: Per-capita industrial roundwood ($\text{m}^3$ per $1{,}000$ residents: Tier 1 vs. Tier 0).
- **Documented Historical Timepoints**:
  - **1970s**: Cabrera Malo afforestation campaign planting *Pinus caribaea* across the Monagas/Anzoátegui savannas.
  - **1988**: Establishment of state enterprise CVG PROFORCA to industrialize plantation forestry ($>500\text{k ha}$).
  - **1999**: Plantation harvesting peak ($1{,}466.9\text{k m}^3$; Caribbean pine accounts for $70.6\%$ of national roundwood).
  - **2008**: Secondary reporting peak ($2{,}295\text{k m}^3$).
  - **2012**: PROFORCA reorganized into state enterprise *Maderas del Orinoco, C.A.*
  - **2014–2018**: Machinery abandonment, unmaintained firebreaks, and catastrophic dry-season wildfires.
  - **2019**: Creation of *Mavetur, S.A.* joint venture (Turkish Glenmore Proje Insaat $49\%$), reorienting output to raw woodchip exports.
  - **2020–2026**: Depressed domestic sawnwood output ($137\text{--}173\text{k m}^3$), with FAO reporting estimated baselines (Flag `E`).
- **Key Descriptive Statistics**:
  - Peak: 1999 ($1{,}466.9\text{k m}^3$, $62.6\text{ m}^3\text{/1k cap}$)
  - 1998 Baseline: $1{,}165.0\text{k m}^3$ ($49.8\text{ m}^3\text{/1k cap}$)
  - 2026 Current: $1{,}364.0\text{k m}^3$ ($47.6\text{ m}^3\text{/1k cap}$)
  - Net Peak-to-Current Collapse: **$-24.0\%$ per capita**.

---

### 5. Tertiary Services Value-Added, Employment & Productivity ([`commodity_services_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodity_services_1970_2026.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `rawdata/un_wb_venezuela_services_1970_2026.csv`
- **Descriptive Visual Architecture**:
  - **Top Panel**: Services Gross Value-Added in constant 2015 USD ($\$56.4\text{B}\text{--}\$213.6\text{B}$) and constant 2017 PPP international dollars ($\$88.0\text{B}\text{--}\$333.1\text{B}$).
  - **Bottom Panel**: Services GVA per resident in constant 2015 USD (Tier 1 vs. Tier 0) alongside the Real Services Labor Productivity Index ($2015 = 100$).
- **Documented Historical Timepoints**:
  - **1974**: First oil boom expansion of public administration and commerce.
  - **1983**: Viernes Negro; services share of GDP reaches all-time peak of $61.05\%$ prior to currency devaluation.
  - **1989**: Caracazo and IMF structural adjustment; price adjustments and transport fare hikes.
  - **1994**: Banco Latino banking crisis; failure of $>50\%$ of commercial banking system (bailout cost $11\%$ of GDP; financial GVA down $-21.4\%$).
  - **1998**: Chávez presidential election ($112.0\text{B}$ GVA).
  - **2004–2012**: Petro-consumption boom and social missions (*Barrio Adentro*, *Mercal*).
  - **2013**: Historical volume apex ($\$213.6\text{B}$ in 2015 USD; $\$7{,}143\text{/cap}$), followed by Maduro succession.
  - **2014–2020**: Hyperinflationary collapse; services GVA drops $-71.35\%$ to $\$61.2\text{B}$, while labor productivity index plummets from $112.5$ to $31.7$.
  - **2021–2026**: De facto transactional dollarization; services employment stabilizes at $>71\%$ due to informal subsistence trade.
- **Key Descriptive Statistics**:
  - Peak: 2013 ($\$213.6\text{B}$, $\$7{,}143\text{/cap}$)
  - 1998 Baseline: $\$112.0\text{B}$ ($\$4{,}786\text{/cap}$)
  - Nadir: 2020 ($\$61.2\text{B}$, $\$2{,}168\text{/cap}$)
  - 2026 Current: $\$80.5\text{B}$ ($\$2{,}811\text{/cap}$)
  - Net Peak-to-Current Collapse: **$-60.6\%$ per capita**.

---

### 6. Multi-Sector Synoptic Overview ([`commodities_multi_sector_overview_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodities_multi_sector_overview_1970_2026.png))
- **Visual Design**: 5 vertically stacked, synchronized panels sharing the exact same $1970\text{--}2026$ horizontal time axis.
- **Unified Timeline**: All 10 historical break lines are marked continuously across all 5 sectors (1974 Nationalization, 1983 Viernes Negro, 1989 Caracazo, 1992 Coup attempt, 1994 Banco Latino, 1998 Chávez election, 2002 Coup, 2003 Strike, 2013 Maduro succession, 2019 Sanctions/Blackouts).
- **Core Narrative**: Demonstrates how oil dominated the 1970s and 1980s, basic industries (steel and aluminum) expanded to export apexes in the late 1990s and 2000s, and all physical production sectors suffered concurrent structural paralysis post-2013.

---

### 7. Multi-Sector Per-Capita Synoptic Overview ([`commodities_per_capita_overview_1970_2026.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/commodities_per_capita_overview_1970_2026.png))
- **Visual Design**: 5 vertically stacked, synchronized panels tracking per-capita production across all 5 sectors (Crude Oil bbl/cap/yr, Crude Steel kg/cap/yr, Primary Aluminum kg/cap/yr, Industrial Wood m³/1k cap/yr, Tertiary Services GVA $/cap/yr) over the identical 1970–2026 horizontal time axis.
- **Demographic Decomposition**: Contrasts Tier 1 migration-adjusted resident population ($N_{\text{res}} \sim 28.4\text{M}$ in 2026) in solid teal line against Tier 0 unadjusted extrapolation ($N_{\text{proj}} > 34.0\text{M}$ in 2026) in dashed purple line, shading the Nennerproblem distortion gap resulting from the net exodus of $>7.7\text{M}$ Venezuelan migrants and refugees.
- **Unified Timeline**: Continuous vertical timeline references for all 10 historical break points across the entire 56-year trajectory.
- **Key Empirical Takeaway**: Illustrates that the per-capita collapse is even more severe than nominal figures suggest for industrial metals (-99.3% in steel, -96.1% in aluminum, -90.9% in oil), while unadjusted population denominators erroneously depress per-capita indicators by an additional ~19–24% during the humanitarian emergency.

---

## 3. Panel-by-Panel Scientific Validity Audit of Econometric & Matrix Panels (A–I)

### Panel A: Absolute vs. Per-Capita Output Collapse Across Key Sectors ([`panel_a_sectoral_collapse.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_a_sectoral_collapse.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`
- **Mathematical Formula**:
  $$\text{Relative Output Rate}_s = \frac{Y_{s, t} / P_{t, \text{Tier 1}}}{Y_{s, \text{peak}} / P_{\text{peak}, \text{Tier 1}}} \times 100$$
- **Empirical Findings**:
  - Crude Oil: Peak at $118.8\text{ bbl/cap/yr}$ (1970) collapsed to $10.8\text{ bbl/cap/yr}$ in 2026 ($-91\%$ collapse).
  - Steel: Peak at $182.5\text{ kg/cap}$ (2007) collapsed to $1.2\text{ kg/cap}$ in 2026 ($-99.3\%$ collapse).
  - Aluminum: Peak at $28.1\text{ kg/cap}$ (1997) collapsed to $1.1\text{ kg/cap}$ in 2026 ($-96\%$ collapse).
  - Wood: Peak at $62.6\text{ m}^3\text{/1k cap}$ (1999) contracted to $47.6\text{ m}^3\text{/1k cap}$ in 2026 ($-24\%$ collapse).
  - Services: Peak at $\$7,143\text{/cap}$ (2013) collapsed to $\$2,811\text{/cap}$ in 2026 ($-61\%$ collapse).
- **Caveats**: Uses Tier 1 migration-adjusted population denominators; if Tier 0 unadjusted population were used, per-capita collapse would be overstated by an additional $20\text{--}25\%$.

### Panel B: 56-Year Multi-Sector Per-Capita Trajectories & The 10 Historical Timepoints ([`panel_b_multi_sector_trajectories.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_b_multi_sector_trajectories.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `datasets/venezuela_structural_breaks_1970_2026.csv`
- **Mathematical Formula**:
  $$I_{s, t} = \left( \frac{Y_{s, t} / P_{t, \text{Tier 1}}}{Y_{s, 1970} / P_{1970, \text{Tier 1}}} \right) \times 100, \quad \text{Composite Laspeyres Index}_t = \frac{1}{5} \sum_{s=1}^{5} I_{s, t}$$
- **Break Annotations**: Vertical annotations for all 10 historical timepoints (1974, 1983, 1989, 1992, 1994, 1998, 2002, 2003, 2013, 2019).

### Panel C: Demographic Denominators & Nennerproblem (*Responsible Demographics*) ([`panel_c_demographic_denominators.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_c_demographic_denominators.png))
- **Input Datasets**: `datasets/venezuela_demographics_denominators.csv`
- **Mathematical Alignment**: Contrasts:
  - Tier 0: $P_{t, \text{Tier 0}} > 34\text{ million}$ (unrevised linear projection).
  - Tier 1: $P_{t, \text{Tier 1}} \approx 28.4\text{ million}$ (UN WPP 2024 / ENCOVI resident population).
  - Tier 2: $P_{t, \text{Tier 2}} \approx 18.4\text{ million}$ (working-age cohort 15–64).
- **Demographic Reserve Inversion**: Resolves the $19\%$ Nennerproblem gap resulting from the departure of $>7.7\text{ million}$ emigrants.

### Panel D: Tertiarization & Informal Employment Shift ([`panel_d_tertiarization_employment.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_d_tertiarization_employment.png))
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`
- **Empirical Indicators**: Services share of GDP peaked at $61.05\%$ in 1983 (pre-Viernes Negro). Services employment share grew steadily from $44.8\%$ (1970) to $>71\%$ (2020–2026) due to informalization of displaced industrial labor.

### Panel E: Multi-Factor Joint Failure Risk ($M_{\text{ind}}$) & Fréchet–Hoeffding Bounds ([`panel_e_joint_failure_model.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_e_joint_failure_model.png))
- **Input Model**: Evaluates joint failure probability across three structural dimensions: Capex deficit ($F_1$), electric grid curtailment ($F_2$), and skilled labor exodus ($F_3$).
- **Mathematical Bounds**:
  $$P_{\text{ind}} = P(F_1) \cdot P(F_2) \cdot P(F_3)$$
  $$P_{\min} = \max(0, P(F_1) + P(F_2) + P(F_3) - 2), \quad P_{\max} = \min(P(F_1), P(F_2), P(F_3))$$
- **Results**: Joint failure probability escalated from $0.03\%$ (1970–1998) to $9.0\%$ (1999–2012) and $78.7\%$ (2013–2026), bounded within $[77\%, 90\%]$.

### Panel F: 2D Production Surface & Historical Collapse Path ([`panel_f_2d_production_surface.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_f_2d_production_surface.png))
- **Mathematical Specification**: Calibrated Cobb–Douglas / CES surface:
  $$Z(X_1, X_2) = 100 \cdot (X_1 / 100)^{0.5} \cdot (X_2 / 100)^{0.5}$$
- **Marginal Conservation Assertion**: Verified runtime assertion $\max |\mathbb{E}[Z] - \bar{Z}| < 10^{-10}$.

### Panel G: Parametric Extraction Decay Curve vs. Latin American Peers ([`panel_g_extraction_decay_curve.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_g_extraction_decay_curve.png))
- **Model**: Piecewise exponential decay fitted to Venezuela crude output per resident ($1998\text{--}2026$):
  $$y(t) = y_0 e^{-k t}, \quad \hat{y}_0 = 53.8\text{ bbl/cap}, \quad \hat{k} = 0.068\text{ yr}^{-1}$$
- **Peer Benchmark**: Compares against expanding regional peers (Brazil expanding from $2.2$ to $5.8\text{ bbl/cap}$; Colombia steady at $5.4\text{ bbl/cap}$).

### Panel H: Econometric OLS Regression with 95% Confidence Intervals ([`panel_h_econometric_regression.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_h_econometric_regression.png))
- **Model**: OLS regression of Steel Output Index ($Y$) on Services Labor Productivity Index ($X$) across $N = 57$ observations ($1970\text{--}2026$):
  $$\hat{Y} = -6.83 + 0.84 \cdot X, \quad R^2 = 0.68, \quad p < 0.001$$
- **95% Confidence Interval for Slope**: $\beta \in [0.68, 1.00]$.

### Panel I: Causal Waterfall & Path-Independent Shapley ($K!$) Attribution ([`panel_i_causal_waterfall.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/panel_i_causal_waterfall.png))
- **Model**: 5-factor causal attribution of the $-85.0$ net drop in composite per-capita output:
  - 1. Human Capital & Technical Purge: $\Delta = -28.0$ (Shapley $\phi = -28.0$)
  - 2. Capex Starvation & Expropriation: $\Delta = -32.0$ (Shapley $\phi = -32.0$)
  - 3. Electric Grid (SEN) & Input Collapse: $\Delta = -20.0$ (Shapley $\phi = -20.0$)
  - 4. Financial & Sectoral Sanctions: $\Delta = -15.0$ (Shapley $\phi = -15.0$)
  - 5. Emigration Denominator Buffer: $\Delta = +10.0$ (Shapley $\phi = +10.0$)
- **Permutation Invariance**: Evaluated across all $5! = 120$ permutations; sum of Shapley values identically matches the net $-85.0$ drop ($\text{error} < 10^{-10}$).

### Standalone Causal Waterfall Figure ([`venezuela_output_collapse_waterfall.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/venezuela_output_collapse_waterfall.png))
- **Architecture**: Full high-resolution rendering of the sequential causal waterfall with an embedded Shapley attribution summary inset and pedagogical step annotations.

### Unified 9-Panel Synoptic Matrices ([`venezuela_productivity_3x3_en.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/venezuela_productivity_3x3_en.png) & [`venezuela_productivity_3x3_de.png`](file:///Users/selle/Documents/GitHub/venezuela-production/plots/venezuela_productivity_3x3_de.png))
- **Visual Design**: Multi-lingual publication-ready $3 \times 3$ synoptic matrices combining Panels A through I (`figsize=(20, 16)`, `dpi=300`) with bilingual annotations (English and German).

---

## 4. Mathematical Safeguards, Runtime Assertions & AST Conformance
All modeling and rendering routines adhere strictly to the `responsible-research` AST contract:
1. **Zero Synthetic Generation**: No `scipy.stats.*.rvs()` or `np.random.*` calls.
2. **Zero Silent Fallbacks**: No `.get(k, <num>)` or conditional ternary magic numbers.
3. **Strict Parameter Lineage**: Central empirical catalog loaded dynamically from `datasets/literature_empirical_benchmarks.csv`.
4. **Marginal Conservation**: Verified mathematical identity $\max |\mathbb{E}[Z] - \bar{Z}| < 10^{-10}$ on bivariate surfaces.
