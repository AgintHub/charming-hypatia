from pydantic import BaseModel, Field
from typing import List


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


class BuildSignalGenerationModelOutput(BaseModel):
    """Pydantic model for build_signal_generation_model node outputs."""
    model_pseudocode: str = (
        Field(..., description="Pseudocode representation of the signal generation model, including logic flow and conditional statements.")
    )
    feature_names: List[str] = (
        Field(..., description="List of feature names used as inputs to the signal generation model.")
    )
    feature_weights: List[float] = (
        Field(..., description="Corresponding weight for each feature in the model, reflecting its importance.")
    )
    entry_thresholds: List[float] = (
        Field(..., description="Threshold values that trigger entry signals for each defined signal component.")
    )
    exit_thresholds: List[float] = (
        Field(..., description="Threshold values that trigger exit signals for each defined signal component.")
    )
    position_sizing_parameters: List[float] = (
        Field(..., description="Parameters related to position sizing (e.g., volatility scaling factor, max exposure) used within the model.")
    )


def build_signal_generation_model(feature_engineering_input: FeatureEngineeringOutput, define_strategy_framework_input: DefineStrategyFrameworkOutput, analyze_market_structure_input: AnalyzeMarketStructureOutput, **kwargs) -> BuildSignalGenerationModelOutput:
    """
    Constructs a weighted signal generation model using feature engineering
    output, strategy framework definitions, and market structure analysis.

    Returns
    -------
    dict
        A dictionary containing the model pseudocode and all parameter
        arrays: {     "model_pseudocode": str,     "feature_names":
        List[str],     "feature_weights": List[float],
        "entry_thresholds": List[float],     "exit_thresholds": List[float],
        "position_sizing_parameters": List[float] }

    Raises
    ------
    ValueError
        If the parent nodes do not provide matching lengths for
        feature_names and feature_weights.
    RuntimeError
        If required inputs from any parent node are missing or malformed.

    Examples
    --------
    >>> model = build_signal_generation_model()
    >>> print(model["feature_names"])
    >>> print(model["entry_thresholds"])
    ["rsi_14", "macd_hist", "vol_surface_30d"]\n[0.6, -0.3]

    >>> model = build_signal_generation_model()
    >>> print(model["model_pseudocode"])
    \"\"\"# Pseudocode\\nscore = 0.0\\nfor f, w in zip(feature_names,
    feature_weights):\\n    score += w * get_feature(f)\\nif score >
    entry_thresholds[0]:\\n    signal = 'LONG'\\nelif score <
    exit_thresholds[0]:\\n    signal = 'SHORT'\\nelse:\\n    signal = 'HOLD'\\n#
    Position sizing\\nsize = base_notional *
    position_sizing_parameters[0]\\n\"\"\""

    """
    return BuildSignalGenerationModelOutput(
        model_pseudocode="",
        feature_names=[],
        feature_weights=[],
        entry_thresholds=[],
        exit_thresholds=[],
        position_sizing_parameters=[],
    )