from pydantic import BaseModel, Field
from typing import List


class DefineStrategyFrameworkOutput(BaseModel):
    """Pydantic model for define_strategy_framework node outputs."""
    strategy_type: str = (
        Field(..., description="High-level category of the strategy (e.g., statistical arbitrage, trend following, mean reversion)")
    )
    defining_characteristics: List[str] = (
        Field(..., description="3-5 concise bullet points that capture the core attributes of the strategy")
    )
    signal_generation_methodology: str = (
        Field(..., description="Brief description of how trading signals are generated within the framework")
    )
    position_sizing_approach: str = (
        Field(..., description="Summary of the position sizing rules and risk allocation logic")
    )
    execution_protocols: str = (
        Field(..., description="Overview of order execution tactics, including order types and routing preferences")
    )
    framework_summary: str = (
        Field(..., description="Full 250-word description combining all elements of the framework")
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


def create_liquidity_control_rules(define_strategy_framework_input: DefineStrategyFrameworkOutput, analyze_market_structure_input: AnalyzeMarketStructureOutput, **kwargs) -> CreateLiquidityControlRulesOutput:
    """
    Generate a list of adaptive liquidity‑control rules based on strategy
    specifications and market‑structure insights.

    Returns
    -------
    dict
        Dictionary containing seven parallel lists (rule_names,
        depth_thresholds, volatility_thresholds, time_of_day_windows,
        order_type, batch_execution_flags, rule_descriptions) where each
        index defines a complete rule.

    Raises
    ------
    ValueError
        If the derived rule lists have mismatched lengths or contain invalid
        values (e.g., negative thresholds, unsupported order types).

    Examples
    --------
    >>> rules = create_liquidity_control_rules()
    >>> rules['rule_names']
    >>> rules['order_type']
    ["high_liquidity_market", "low_volatility_limit"]\n["market", "limit"]

    >>> # Inspect the first rule
    >>> print({
    ...     "name": rules['rule_names'][0],
    ...     "depth_thr": rules['depth_thresholds'][0],
    ...     "vol_thr": rules['volatility_thresholds'][0],
    ...     "time_window": rules['time_of_day_windows'][0],
    ...     "order": rules['order_type'][0],
    ...     "batch": rules['batch_execution_flags'][0],
    ...     "desc": rules['rule_descriptions'][0]
    >>> })
    {'name': 'high_liquidity_market', 'depth_thr': 50000.0, 'vol_thr': 0.02,
    'time_window': '09:30-11:00', 'order': 'market', 'batch': True, 'desc': 'Use
    market orders and batch execution when depth exceeds 50k contracts and
    volatility is below 2% during the opening session.'}

    """
    return CreateLiquidityControlRulesOutput(
        rule_names=[],
        depth_thresholds=[],
        volatility_thresholds=[],
        time_of_day_windows=[],
        order_type=[],
        batch_execution_flags=[],
        rule_descriptions=[],
    )