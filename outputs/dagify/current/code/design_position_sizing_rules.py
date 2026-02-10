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


class CreateLiquidityControlRulesOutput(BaseModel):
    """Pydantic model for create_liquidity_control_rules node outputs."""
    rule_names: List[str] = (
        Field(..., description="Identifiers for each liquidity control rule")
    )
    depth_thresholds: List[float] = (
        Field(..., description="Depth\u2011of\u2011book thresholds (e.g., minimum available volume) for each rule")
    )
    volatility_thresholds: List[float] = (
        Field(..., description="Volatility levels (e.g., standard deviation of recent price changes) that trigger the rule")
    )
    time_of_day_windows: List[str] = (
        Field(..., description="Time\u2011of\u2011day regimes (e.g., \"09:30-11:00\", \"15:00-16:00\") applicable to each rule")
    )
    order_type: List[str] = (
        Field(..., description="Order execution type for each rule (e.g., \"market\", \"limit\")")
    )
    batch_execution_flags: List[bool] = (
        Field(..., description="Whether batch execution is enabled for each rule")
    )
    rule_descriptions: List[str] = (
        Field(..., description="Human\u2011readable description of each liquidity control rule")
    )


class DesignPositionSizingRulesOutput(BaseModel):
    """Pydantic model for design_position_sizing_rules node outputs."""
    position_sizing_algorithm: str = (
        Field(..., description="High\u2011level description of the position sizing methodology in natural language")
    )
    sizing_rules: List[str] = (
        Field(..., description="List of explicit rule expressions or formulas used to compute position size")
    )
    volatility_multiplier: float = (
        Field(..., description="Multiplier applied to base risk based on realized volatility")
    )
    liquidity_adjustment_factor: float = (
        Field(..., description="Factor that scales position size according to liquidity conditions (e.g., depth\u2011of\u2011book, spread)")
    )
    confidence_threshold: float = (
        Field(..., description="Minimum signal confidence level required to take a position")
    )
    var_constraint: float = (
        Field(..., description="Maximum allowed Value\u2011at\u2011Risk (VaR) expressed as a percentage of portfolio equity")
    )
    margin_requirement: float = (
        Field(..., description="Margin requirement per contract as a percentage of notional exposure")
    )
    notes: str = (
        Field(..., description="Additional remarks, assumptions, or implementation considerations")
    )


def design_position_sizing_rules(calculate_statistical_metrics_input: CalculateStatisticalMetricsOutput, create_liquidity_control_rules_input: CreateLiquidityControlRulesOutput, **kwargs) -> DesignPositionSizingRulesOutput:
    """
    Generate a full position‑sizing specification using statistical metrics and
    liquidity control rules.

    Parameters
    ----------
    statistical_metrics : dict
        Dictionary returned by `calculate_statistical_metrics` containing
        volatility and distribution statistics for each futures contract.
    liquidity_rules : dict
        Dictionary returned by `create_liquidity_control_rules` describing
        depth‑of‑book and volatility thresholds for trade‑size adjustments.

    Returns
    -------
    dict
        Dictionary matching the node's output_structure keys with the
        computed values.

    Raises
    ------
    KeyError
        If required keys are missing from the input dictionaries.
    ValueError
        If any input values are out of realistic bounds (e.g., negative
        volatility).

    Examples
    --------
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
      'position_sizing_algorithm': 'Volatility‑adjusted, liquidity‑aware sizing
    with confidence and risk caps.',
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
      'notes': 'Volatility multiplier derived from average daily_return_std;
    liquidity factor calibrated from depth thresholds.'
    }

    """
    return DesignPositionSizingRulesOutput(
        position_sizing_algorithm="",
        sizing_rules=[],
        volatility_multiplier=0.0,
        liquidity_adjustment_factor=0.0,
        confidence_threshold=0.0,
        var_constraint=0.0,
        margin_requirement=0.0,
        notes="",
    )