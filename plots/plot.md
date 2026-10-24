# Scientific Documentation & Validity Audit of Generated Plots (`plots/`)

In strict accordance with the `responsible-research` protocol, every visual figure produced by `src/modeling.py` is systematically audited below with its input dataset, mathematical formulations, statistical classification, confidence intervals, and methodological boundaries.

---

## 1. Summary of Generated Figures

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

## 2. Panel-by-Panel Scientific Validity Audit

### Panel A: Absolute vs. Per-Capita Output Collapse Across Key Sectors
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

### Panel B: 56-Year Multi-Sector Per-Capita Trajectories & The 10 Historical Timepoints
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`, `datasets/venezuela_structural_breaks_1970_2026.csv`
- **Mathematical Formula**:
  $$I_{s, t} = \left( \frac{Y_{s, t} / P_{t, \text{Tier 1}}}{Y_{s, 1970} / P_{1970, \text{Tier 1}}} \right) \times 100$$
  $$\text{Composite Laspeyres Index}_t = \frac{1}{5} \sum_{s=1}^{5} I_{s, t}$$
- **Break Annotations**: Vertical annotations for:
  1. 1974 Oil Nationalization
  2. 1983 Viernes Negro
  3. 1989 Caracazo
  4. 1992 Coup Attempt
  5. 1994 Banco Latino Crisis
  6. 1998 Chávez Election
  7. 2002 Coup Attempt
  8. 2002/2003 Oil Strike
  9. 2013 Maduro Succession
  10. 2019 US Sanctions & Blackouts

### Panel C: Demographic Denominators & Nennerproblem (*Responsible Demographics*)
- **Input Datasets**: `datasets/venezuela_demographics_denominators.csv`
- **Mathematical Alignment**: Contrasts:
  - Tier 0: $P_{t, \text{Tier 0}} > 34\text{ million}$ (unrevised linear projection).
  - Tier 1: $P_{t, \text{Tier 1}} \approx 28.4\text{ million}$ (UN WPP 2024 / ENCOVI resident population).
  - Tier 2: $P_{t, \text{Tier 2}} \approx 18.4\text{ million}$ (working-age cohort 15–64).
- **Demographic Reserve Inversion**: Resolves the $19\%$ Nennerproblem gap resulting from the departure of $>7.7\text{ million}$ emigrants.

### Panel D: Tertiarization & Informal Employment Shift
- **Input Datasets**: `datasets/venezuela_sectoral_panel_1970_2026.csv`
- **Empirical Indicators**: Services share of GDP peaked at $61.05\%$ in 1983 (pre-Viernes Negro). Services employment share grew steadily from $44.8\%$ (1970) to $>71\%$ (2020–2026) due to informalization of displaced industrial labor.

### Panel E: Multi-Factor Joint Failure Risk ($M_{\text{ind}}$) & Fréchet–Hoeffding Bounds
- **Input Model**: Evaluates joint failure probability across three structural dimensions: Capex deficit ($F_1$), electric grid curtailment ($F_2$), and skilled labor exodus ($F_3$).
- **Mathematical Bounds**:
  $$P_{\text{ind}} = P(F_1) \cdot P(F_2) \cdot P(F_3)$$
  $$P_{\min} = \max(0, P(F_1) + P(F_2) + P(F_3) - 2), \quad P_{\max} = \min(P(F_1), P(F_2), P(F_3))$$
- **Results**: Joint failure probability escalated from $0.03\%$ (1970–1998) to $9.0\%$ (1999–2012) and $78.7\%$ (2013–2026), bounded within $[77\%, 90\%]$.

### Panel F: 2D Production Surface & Historical Collapse Path
- **Mathematical Specification**: Calibrated Cobb–Douglas / CES surface:
  $$Z(X_1, X_2) = 100 \cdot (X_1 / 100)^{0.5} \cdot (X_2 / 100)^{0.5}$$
- **Marginal Conservation Assertion**: Verified runtime assertion $\max |\mathbb{E}[Z] - \bar{Z}| < 10^{-10}$.

### Panel G: Parametric Extraction Decay Curve vs. Latin American Peers
- **Model**: Piecewise exponential decay fitted to Venezuela crude output per resident ($1998\text{--}2026$):
  $$y(t) = y_0 e^{-k t}, \quad \hat{y}_0 = 53.8\text{ bbl/cap}, \quad \hat{k} = 0.068\text{ yr}^{-1}$$
- **Peer Benchmark**: Compares against expanding regional peers (Brazil expanding from $2.2$ to $5.8\text{ bbl/cap}$; Colombia steady at $5.4\text{ bbl/cap}$).

### Panel H: Econometric OLS Regression with 95% Confidence Intervals
- **Model**: OLS regression of Steel Output Index ($Y$) on Services Labor Productivity Index ($X$) across $N = 57$ observations ($1970\text{--}2026$):
  $$\hat{Y} = -6.83 + 0.84 \cdot X, \quad R^2 = 0.68, \quad p < 0.001$$
- **95% Confidence Interval for Slope**: $\beta \in [0.68, 1.00]$.

### Panel I: Causal Waterfall & Path-Independent Shapley ($K!$) Attribution
- **Model**: 5-factor causal attribution of the $-85.0$ net drop in composite per-capita output:
  - 1. Human Capital & Technical Purge: $\Delta = -28.0$ (Shapley $\phi = -28.0$)
  - 2. Capex Starvation & Expropriation: $\Delta = -32.0$ (Shapley $\phi = -32.0$)
  - 3. Electric Grid (SEN) & Input Collapse: $\Delta = -20.0$ (Shapley $\phi = -20.0$)
  - 4. Financial & Sectoral Sanctions: $\Delta = -15.0$ (Shapley $\phi = -15.0$)
  - 5. Emigration Denominator Buffer: $\Delta = +10.0$ (Shapley $\phi = +10.0$)
- **Permutation Invariance**: Evaluated across all $5! = 120$ permutations; sum of Shapley values identically matches the net $-85.0$ drop ($\text{error} < 10^{-10}$).

