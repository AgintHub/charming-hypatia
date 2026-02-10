# analyze_market_structure PRD

## Description
Characterize market depth and liquidity patterns


## Conceptual Info

This node consumes cleaned order‑book and price series (produced by `process_historical_data`) together with high‑level statistical descriptors of returns (produced by `calculate_statistical_metrics`). It quantifies how market depth and liquidity evolve across time, derives participation‑rate, slippage and latency‑sensitivity profiles, discovers recurring day‑of‑week and intraday patterns, and finally synthesizes a concise narrative that can be consumed by downstream signal‑generation and liquidity‑control modules.

## Docstring

### Summary
Analyze market depth and liquidity regimes to produce participation, slippage, latency, and pattern insights.

### Parameters

- **cleaned_data_csv** (str): CSV string from `process_historical_data` containing timestamped OHLCV and open‑interest data.
- **statistical_metrics** (dict): Dictionary from `calculate_statistical_metrics` containing return moments and volatility‑clustering metrics for each contract series.

### Returns

dict: Dictionary with keys matching the node's output_structure: participation_rates, slippage_estimates, latency_sensitivity, day_of_week_patterns, time_of_day_patterns, and summary_report.

### Raises

- ValueError: If `cleaned_data_csv` is empty or malformed.
- KeyError: If required fields are missing from `statistical_metrics`.

### Examples

```python
>>> cleaned_csv = "timestamp,open,high,low,close,volume,open_interest\n2023-01-01 09:30,100,101,99,100.5,5000,2000"
>>> stats = {"contract_series": ["CL_F2023"], "daily_return_std": [0.015]}
>>> result = analyze_market_structure(cleaned_csv, stats)
>>> result['summary_report']
"The market exhibits high participation during morning sessions with low slippage, but latency sensitivity rises sharply after 14:00 UTC. Monday shows consistently high depth, while the 09:30‑11:30 window is the most liquid."
```

```python
>>> cleaned_csv = "timestamp,open,high,low,close,volume,open_interest\n2023-01-02 10:00,200,202,198,201,8000,3000"
>>> stats = {"contract_series": ["GC_F2023"], "daily_return_std": [0.02]}
>>> result = analyze_market_structure(cleaned_csv, stats)
>>> result['participation_rates']
[0.12, 0.15, 0.09, 0.11]
```
