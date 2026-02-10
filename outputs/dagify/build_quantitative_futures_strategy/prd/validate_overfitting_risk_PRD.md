# validate_overfitting_risk PRD

## Description
Assess model robustness to different market regimes by stress‑testing the optimized parameters obtained from `optimize_model_parameters`. The node evaluates how performance degrades when the same parameters are applied to distinct market environments and flags regimes where over‑fitting is evident.


## Conceptual Info

The node validates that the hyper‑parameters found by `optimize_model_parameters` are not over‑fitted to a single market condition. By re‑running the back‑test on a suite of contrasting regimes, it quantifies performance drop, isolates vulnerable parameter slices, and produces a concise robustness verdict.

## Docstring

### Summary
Stress‑tests optimized model parameters across multiple market regimes and reports robustness metrics.

### Parameters

- **optimized_parameters** (dict): Dictionary of parameter settings returned by `optimize_model_parameters`. Keys are parameter names and values are the selected values (e.g., {'signal_threshold': 0.45, 'position_scale': 1.2}).
- **regime_definitions** (dict): Mapping of regime name to a callable that filters historical data to that regime. Example: {'bull': bull_filter, 'bear': bear_filter, ...}.

### Returns

dict: A dictionary containing the five output fields defined in `output_structure`.

### Raises

- ValueError: If `optimized_parameters` is empty or missing required keys.
- KeyError: If a requested regime is not present in `regime_definitions`.
- RuntimeError: If back‑testing fails for any regime due to data issues.

### Examples

```python
>>> result = validate_overfitting_risk(
...     optimized_parameters={'signal_threshold': 0.48, 'position_scale': 1.1},
...     regime_definitions={
...         'bull': bull_filter,
...         'bear': bear_filter,
...         'high_vol': high_vol_filter,
...         'low_vol': low_vol_filter,
...         'sideways': sideways_filter
...     }
>>> )
{'tested_regimes': ['bull', 'bear', 'high_vol', 'low_vol', 'sideways'], 'degradation_scores': [0.02, 0.15, 0.09, 0.03, 0.05], 'affected_parameter_ranges': ['signal_threshold: 0.30‑0.55', 'position_scale: 0.8‑1.3', 'signal_threshold: 0.30‑0.55', 'position_scale: 0.9‑1.2', 'signal_threshold: 0.35‑0.50'], 'robustness_summary': 'Model remains robust in bull, low_vol and sideways regimes (≤5% Sharpe drop) but degrades in bear regime (15% drop).', 'is_robust': False}
```

```python
>>> result = validate_overfitting_risk(
...     optimized_parameters={'signal_threshold': 0.55, 'position_scale': 0.9},
...     regime_definitions={'bull': bull_filter, 'bear': bear_filter, 'high_vol': high_vol_filter, 'low_vol': low_vol_filter, 'sideways': sideways_filter}
>>> )
{'tested_regimes': ['bull', 'bear', 'high_vol', 'low_vol', 'sideways'], 'degradation_scores': [0.01, 0.04, 0.02, 0.01, 0.03], 'affected_parameter_ranges': ['signal_threshold: 0.50‑0.60', 'signal_threshold: 0.50‑0.60', 'signal_threshold: 0.50‑0.60', 'signal_threshold: 0.50‑0.60', 'signal_threshold: 0.50‑0.60'], 'robustness_summary': 'All regimes show ≤4% Sharpe degradation; model is robust.', 'is_robust': True}
```
