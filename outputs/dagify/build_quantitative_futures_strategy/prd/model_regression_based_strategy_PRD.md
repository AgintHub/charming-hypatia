# model_regression_based_strategy PRD

## Description
Construct statistical arbitrage models for predictive signals using engineered features, market structure insights, and statistical metrics. Generates multiple regularized regression models, evaluates out‑of‑sample performance, and selects the best model with documented coefficient significance.


## Conceptual Info

This node translates engineered predictive features, market‑structure signals, and statistical return metrics into a suite of regularized regression models that forecast future price movements. By evaluating each model on a hold‑out dataset, it identifies the most robust predictor and provides full coefficient details, enabling downstream signal generation and risk management components.

## Docstring

### Summary
Builds and selects regression‑based predictive models for a statistical arbitrage strategy.

### Parameters

- **features** (dict): Dictionary containing feature engineering outputs: 'selected_feature_names' (List[str]) and 'selected_feature_importance' (List[float]).
- **market_structure** (dict): Outputs from analyze_market_structure needed for model context (e.g., participation_rates, slippage_estimates).
- **statistical_metrics** (dict): Outputs from calculate_statistical_metrics such as volatility_clustering_metric, skewness, kurtosis.
- **regularization_methods** (List[str]): List of regularization techniques to apply (e.g., ['Lasso', 'Ridge', 'ElasticNet']).
- **out_of_sample_split** (float): Proportion of data reserved for out‑of‑sample validation (0 < split < 1).

### Returns

dict: Dictionary with keys matching the node's output_structure, containing model identifiers, descriptions, performance metrics, selected model index, coefficients, coefficient names, and significance flags.

### Raises

- ValueError: If required input keys are missing or if out_of_sample_split is not in (0,1).
- RuntimeError: If model fitting fails for all specified regularization methods.

### Examples

```python
>>> outputs = model_regression_based_strategy(
...     features={
...         'selected_feature_names': ['rsi_14', 'macd_hist', 'vol_surface_30d'],
...         'selected_feature_importance': [0.8, 0.6, 0.4]
...     },
...     market_structure={
...         'participation_rates': [0.12, 0.15],
...         'slippage_estimates': [0.0005, 0.0007]
...     },
...     statistical_metrics={
...         'volatility_clustering_metric': [0.3],
...         'skewness': [0.1],
...         'kurtosis': [3.2]
...     },
...     regularization_methods=['Lasso', 'Ridge'],
...     out_of_sample_split=0.2
>>> )
>>> print(outputs['selected_model_index'])
0
```

```python
>>> print(outputs['model_names'])
>>> print(outputs['model_performance'])
['Lasso_Model', 'Ridge_Model']\n[0.74, 0.71]
```
