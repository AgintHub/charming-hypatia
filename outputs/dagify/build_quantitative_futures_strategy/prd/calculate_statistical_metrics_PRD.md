# calculate_statistical_metrics PRD

## Description
Compute key statistical properties of returns distribution for each futures contract series, including daily/weekly/monthly return moments, volatility clustering, and non‑normality measures, and produce a time‑weighted human‑readable summary.


## Conceptual Info

This node transforms cleaned historical futures price data into a comprehensive statistical portrait of each contract series. By aggregating returns at daily, weekly, and monthly horizons and evaluating higher‑order moments and volatility clustering, it supplies downstream components (market‑structure analysis, position sizing, and regression models) with robust descriptors of return behavior that are essential for risk assessment and signal generation.

## Docstring

### Summary
Calculate statistical return metrics for multiple futures contract series from cleaned price data.

### Parameters

- **cleaned_data_csv** (str): CSV‑formatted string produced by `process_historical_data`, containing columns: timestamp, open, high, low, close, volume, open_interest.

### Returns

dict: Dictionary with keys matching the node's output_structure, each holding the computed metric list or summary string.

### Raises

- ValueError: If the CSV cannot be parsed, lacks required columns, or contains insufficient data for a given contract series.
- RuntimeError: If numerical computations (e.g., division by zero in volatility clustering) fail.

### Examples

```python
>>> csv_data = ("timestamp,open,high,low,close,volume,open_interest\n"
...             "2023-01-01 09:30,100,101,99,100.5,2000,10\n"
...             "2023-01-02 09:30,100.5,102,100,101,2100,11")
>>> metrics = calculate_statistical_metrics(csv_data)
{
  'contract_series': ['CL_FUT'],
  'daily_return_mean': [0.005],
  'daily_return_std': [0.0012],
  'weekly_return_mean': [0.032],
  'weekly_return_std': [0.005],
  'monthly_return_mean': [0.128],
  'monthly_return_std': [0.020],
  'volatility_clustering_metric': [1.45],
  'skewness': [0.12],
  'kurtosis': [3.4],
  'time_weighted_summary': 'Daily mean 0.5 %, weekly mean 3.2 %, monthly mean 12.8 %, volatility clustering 1.45, skew 0.12, kurtosis 3.4.'
}
```

```python
>>> # Missing required column triggers an error
>>> bad_csv = "timestamp,open,high,low,volume,open_interest\n2023-01-01 09:30,100,101,99,2000,10"
>>> calculate_statistical_metrics(bad_csv)
ValueError: CSV must contain a 'close' column.
```
