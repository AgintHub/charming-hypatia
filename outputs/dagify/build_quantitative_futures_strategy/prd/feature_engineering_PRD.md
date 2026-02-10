# feature_engineering PRD

## Description
Create predictive features from raw data


## Conceptual Info

The feature_engineering node transforms cleaned historical futures data and identified macro‑level risk factors into a rich set of quantitative predictors. It synthesizes technical, volatility, momentum, liquidity, and macro‑economic features, then ranks them using statistical importance metrics to surface the most predictive variables for downstream modeling.

## Docstring

### Summary
Generate engineered predictive features from cleaned futures data and macro risk factors, and rank them by predictive importance.

### Parameters

- **cleaned_data_csv** (str): CSV string containing the cleaned, uniformly‑spaced futures price and volume series produced by `process_historical_data`.
- **risk_factors** (List[str]): List of macro‑economic or market risk factor names identified by `identify_risk_factors`.
- **risk_factor_categories** (List[str]): Parallel list indicating each risk factor's category ("price driver", "volatility factor", or "liquidity risk").

### Returns

dict: Dictionary with keys `feature_names`, `feature_descriptions`, `feature_importance_scores`, `selected_feature_names`, and `selected_feature_importance` matching the node's output_structure.

### Raises

- ValueError: If the CSV cannot be parsed or required columns are missing.
- RuntimeError: If feature ranking fails due to insufficient data or singular matrix errors.

### Examples

```python
>>> cleaned_csv = "timestamp,open,high,low,close,volume,open_interest\n2023-01-01 09:30,100,101,99,100.5,5000,10\n2023-01-01 09:31,100.5,102,100,101,5200,10"
>>> risk_factors = ["Interest Rates", "Crude Oil Prices"]
>>> risk_factor_categories = ["price driver", "price driver"]
>>> features = feature_engineering(cleaned_csv, risk_factors, risk_factor_categories)
{
  'feature_names': ['rsi_14', 'macd_hist', 'vol_surface_30d', ...],
  'feature_descriptions': ['14‑period Relative Strength Index', 'MACD histogram', '30‑day implied volatility surface', ...],
  'feature_importance_scores': [0.12, 0.09, 0.15, ...],
  'selected_feature_names': ['vol_surface_30d', 'rsi_14', 'macro_spread_interest_crude'],
  'selected_feature_importance': [0.15, 0.12, 0.11]
}
```

```python
>>> # When the input CSV is empty, the function raises an informative error
>>> feature_engineering('', [], [])
ValueError: Input CSV is empty or missing required columns.
```
