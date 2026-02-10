# calculate_performance_metrics PRD

## Description
Quantify strategy efficiency across multiple dimensions


## Conceptual Info

This node ingests the backtested equity curve and trade‑level details for the baseline strategy as well as the optimized parameter set, computes a comprehensive suite of performance metrics for each, and returns a paired comparison. The metrics span return, risk‑adjusted ratios, trade success, holding characteristics, and drawdown recovery, enabling downstream documentation and decision‑making.

## Docstring

### Summary
Compute detailed performance metrics for baseline and optimized trading models.

### Parameters

- **baseline_backtest** (dict): Dictionary output from `backtest_trading_signals` for the baseline model containing keys: 'equity_curve' (list[float]), 'sharpe_ratio' (float), 'max_drawdown' (float), 'annualized_return' (float), 'drawdown_duration_profile' (list[int]).
- **optimized_params** (dict): Dictionary output from `optimize_model_parameters` containing the optimized parameter settings. Used to re‑run backtest internally for the optimized model.

### Returns

dict: Dictionary with the keys defined in the node's output_structure, each mapping to a float metric for baseline and optimized models.

### Raises

- ValueError: If required keys are missing from inputs or if the equity curve lengths are inconsistent.
- RuntimeError: If the optimized backtest fails to produce a valid equity curve.

### Examples

```python
>>> baseline = {
...     'equity_curve': [100, 102, 105, 103],
...     'sharpe_ratio': 1.2,
...     'max_drawdown': -0.04,
...     'annualized_return': 0.15,
...     'drawdown_duration_profile': [2, 3]
>>> }
>>> optimized_params = {'optimal_signal_parameters': ['threshold=0.6'], 'optimal_position_sizing_parameters': ['vol_factor=1.1']}
>>> metrics = calculate_performance_metrics(baseline, optimized_params)
{
  'baseline_annualized_return': 0.15,
  'optimized_annualized_return': 0.18,
  'baseline_sharpe_ratio': 1.2,
  'optimized_sharpe_ratio': 1.35,
  'baseline_sortino_ratio': 1.5,
  'optimized_sortino_ratio': 1.7,
  'baseline_calmar_ratio': 3.75,
  'optimized_calmar_ratio': 4.2,
  'baseline_win_rate': 0.55,
  'optimized_win_rate': 0.62,
  'baseline_avg_holding_period': 4.2,
  'optimized_avg_holding_period': 3.9,
  'baseline_drawdown_recovery_speed': 5.0,
  'optimized_drawdown_recovery_speed': 4.2
}
```
