from pydantic import BaseModel, Field
from typing import List


class CalculateStatisticalMetricsOutput(BaseModel):
    """Pydantic model for calculate_statistical_metrics node outputs."""
    contract_series: List[str] = (
        Field(..., description="Identifiers of futures contract series for which metrics are calculated")
    )
    daily_return_mean: List[float] = (
        Field(..., description="Mean daily return for each contract series")
    )
    daily_return_std: List[float] = (
        Field(..., description="Standard deviation of daily returns for each contract series")
    )
    weekly_return_mean: List[float] = (
        Field(..., description="Mean weekly return for each contract series")
    )
    weekly_return_std: List[float] = (
        Field(..., description="Standard deviation of weekly returns for each contract series")
    )
    monthly_return_mean: List[float] = (
        Field(..., description="Mean monthly return for each contract series")
    )
    monthly_return_std: List[float] = (
        Field(..., description="Standard deviation of monthly returns for each contract series")
    )
    volatility_clustering_metric: List[float] = (
        Field(..., description="Metric quantifying volatility clustering for each contract series")
    )
    skewness: List[float] = (
        Field(..., description="Skewness of return distribution for each contract series")
    )
    kurtosis: List[float] = (
        Field(..., description="Kurtosis of return distribution for each contract series")
    )
    time_weighted_summary: str = (
        Field(..., description="Human\u2011readable summary of the statistical metrics, weighted by observation time")
    )


class FeatureEngineeringOutput(BaseModel):
    """Pydantic model for feature_engineering node outputs."""
    feature_names: List[str] = (
        Field(..., description="List of generated feature names (e.g., \"rsi_14\", \"macd_hist\", \"vol_surface_30d\")")
    )
    feature_descriptions: List[str] = (
        Field(..., description="Brief description of each feature corresponding to the order in feature_names")
    )
    feature_importance_scores: List[float] = (
        Field(..., description="Numerical importance scores for each feature as derived from ranking techniques (higher = more predictive)")
    )
    selected_feature_names: List[str] = (
        Field(..., description="Subset of feature_names that are identified as the strongest candidates based on importance scores")
    )
    selected_feature_importance: List[float] = (
        Field(..., description="Importance scores corresponding to the selected_feature_names")
    )


class AnalyzeMarketStructureOutput(BaseModel):
    """Pydantic model for analyze_market_structure node outputs."""
    participation_rates: List[float] = (
        Field(..., description="Calculated participation rates for each time interval (as percentages expressed in decimal form).")
    )
    slippage_estimates: List[float] = (
        Field(..., description="Estimated slippage values (price impact) for representative trade sizes, expressed in price units.")
    )
    latency_sensitivity: List[float] = (
        Field(..., description="Measured sensitivity of execution cost to latency, expressed as cost increase per millisecond.")
    )
    day_of_week_patterns: List[str] = (
        Field(..., description="Descriptive identifiers of recurring market depth patterns observed for each day of the week (e.g., \"Monday high liquidity\", \"Friday low depth\").")
    )
    time_of_day_patterns: List[str] = (
        Field(..., description="Descriptive identifiers of recurring market depth patterns observed for major time-of-day windows.")
    )
    summary_report: str = (
        Field(..., description="Narrative summary of the market structure analysis, highlighting key regimes and actionable insights.")
    )


class ModelRegressionBasedStrategyOutput(BaseModel):
    """Pydantic model for model_regression_based_strategy node outputs."""
    model_names: List[str] = (
        Field(..., description="Names or identifiers for each regression model generated")
    )
    model_descriptions: List[str] = (
        Field(..., description="Brief textual description of each model, including regularization method used")
    )
    model_performance: List[float] = (
        Field(..., description="Out-of-sample performance metric (e.g., R\u00b2 or information ratio) for each model")
    )
    selected_model_index: int = (
        Field(..., description="Zero\u2011based index of the model chosen as best performing")
    )
    selected_model_coefficients: List[float] = (
        Field(..., description="List of coefficient values for the selected model, ordered to match the feature list")
    )
    selected_model_coefficient_names: List[str] = (
        Field(..., description="Names of the features corresponding to each coefficient in the selected model")
    )
    selected_model_significant: List[bool] = (
        Field(..., description="Boolean flags indicating whether each coefficient in the selected model is statistically significant")
    )


def model_regression_based_strategy(calculate_statistical_metrics_input: CalculateStatisticalMetricsOutput, feature_engineering_input: FeatureEngineeringOutput, analyze_market_structure_input: AnalyzeMarketStructureOutput, **kwargs) -> ModelRegressionBasedStrategyOutput:
    """
    Builds and selects regression‑based predictive models for a statistical
    arbitrage strategy.

    Parameters
    ----------
    features : dict
        Dictionary containing feature engineering outputs:
        'selected_feature_names' (List[str]) and
        'selected_feature_importance' (List[float]).
    market_structure : dict
        Outputs from analyze_market_structure needed for model context
        (e.g., participation_rates, slippage_estimates).
    statistical_metrics : dict
        Outputs from calculate_statistical_metrics such as
        volatility_clustering_metric, skewness, kurtosis.
    regularization_methods : List[str]
        List of regularization techniques to apply (e.g., ['Lasso', 'Ridge',
        'ElasticNet']).
    out_of_sample_split : float
        Proportion of data reserved for out‑of‑sample validation (0 < split
        < 1).

    Returns
    -------
    dict
        Dictionary with keys matching the node's output_structure,
        containing model identifiers, descriptions, performance metrics,
        selected model index, coefficients, coefficient names, and
        significance flags.

    Raises
    ------
    ValueError
        If required input keys are missing or if out_of_sample_split is not
        in (0,1).
    RuntimeError
        If model fitting fails for all specified regularization methods.

    Examples
    --------
    >>> outputs = model_regression_based_strategy(
    ...     features={
    ...         'selected_feature_names': ['rsi_14', 'macd_hist',
    'vol_surface_30d'],
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

    >>> print(outputs['model_names'])
    >>> print(outputs['model_performance'])
    ['Lasso_Model', 'Ridge_Model']\n[0.74, 0.71]

    """
    return ModelRegressionBasedStrategyOutput(
        model_names=[],
        model_descriptions=[],
        model_performance=[],
        selected_model_index=0,
        selected_model_coefficients=[],
        selected_model_coefficient_names=[],
        selected_model_significant=[],
    )