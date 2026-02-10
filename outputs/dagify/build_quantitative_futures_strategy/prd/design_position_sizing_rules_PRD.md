# design_position_sizing_rules PRD

## Description
Create dynamic capital allocation methodology


## Conceptual Info

This node synthesizes statistical volatility metrics and liquidity control rules to produce a comprehensive position‑sizing specification. The resulting algorithm dynamically scales exposure based on realized volatility, market liquidity, signal confidence, and risk limits such as VaR and margin constraints, ensuring that each trade respects both market conditions and portfolio risk appetite.

## Docstring

### Summary
Generate a full position‑sizing specification using statistical metrics and liquidity control rules.

### Parameters

- **statistical_metrics** (dict): Dictionary returned by `calculate_statistical_metrics` containing volatility and distribution statistics for each futures contract.
- **liquidity_rules** (dict): Dictionary returned by `create_liquidity_control_rules` describing depth‑of‑book and volatility thresholds for trade‑size adjustments.

### Returns

dict: Dictionary matching the node's output_structure keys with the computed values.

### Raises

- KeyError: If required keys are missing from the input dictionaries.
- ValueError: If any input values are out of realistic bounds (e.g., negative volatility).

### Examples

```python
>>> stat_metrics = {
...     'volatility_clustering_metric': [0.12, 0.15],
...     'daily_return_std': [0.008, 0.010]
>>> }
>>> liq_rules = {
...     'depth_thresholds': [1000, 2000],
...     'volatility_thresholds': [0.02, 0.03]
>>> }
>>> result = design_position_sizing_rules(stat_metrics, liq_rules)
{
  'position_sizing_algorithm': 'Volatility‑adjusted, liquidity‑aware sizing with confidence and risk caps.',
  'sizing_rules': [
    'base_size = risk_cap / (volatility * volatility_multiplier)',
    'size *= liquidity_adjustment_factor if depth >= depth_threshold',
    "size = 0 if signal_confidence < confidence_threshold"
  ],
  'volatility_multiplier': 1.5,
  'liquidity_adjustment_factor': 0.8,
  'confidence_threshold': 0.7,
  'var_constraint': 0.02,
  'margin_requirement': 0.1,
  'notes': 'Volatility multiplier derived from average daily_return_std; liquidity factor calibrated from depth thresholds.'
}
```
