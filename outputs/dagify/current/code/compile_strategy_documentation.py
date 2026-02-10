from pydantic import BaseModel, Field
from typing import List


class CalculatePerformanceMetricsOutput(BaseModel):
    """Pydantic model for calculate_performance_metrics node outputs."""
    baseline_annualized_return: float = (
        Field(..., description="Annualized return of the baseline model (percentage expressed as decimal)")
    )
    optimized_annualized_return: float = (
        Field(..., description="Annualized return of the optimized model (percentage expressed as decimal)")
    )
    baseline_sharpe_ratio: float = (
        Field(..., description="Sharpe ratio of the baseline model")
    )
    optimized_sharpe_ratio: float = (
        Field(..., description="Sharpe ratio of the optimized model")
    )
    baseline_sortino_ratio: float = (
        Field(..., description="Sortino ratio of the baseline model")
    )
    optimized_sortino_ratio: float = (
        Field(..., description="Sortino ratio of the optimized model")
    )
    baseline_calmar_ratio: float = (
        Field(..., description="Calmar ratio of the baseline model")
    )
    optimized_calmar_ratio: float = (
        Field(..., description="Calmar ratio of the optimized model")
    )
    baseline_win_rate: float = (
        Field(..., description="Proportion of winning trades for the baseline model (0 to 1)")
    )
    optimized_win_rate: float = (
        Field(..., description="Proportion of winning trades for the optimized model (0 to 1)")
    )
    baseline_avg_holding_period: float = (
        Field(..., description="Average holding period of trades in the baseline model (in days)")
    )
    optimized_avg_holding_period: float = (
        Field(..., description="Average holding period of trades in the optimized model (in days)")
    )
    baseline_drawdown_recovery_speed: float = (
        Field(..., description="Speed of drawdown recovery for the baseline model (e.g., days to recover 50% of max drawdown)")
    )
    optimized_drawdown_recovery_speed: float = (
        Field(..., description="Speed of drawdown recovery for the optimized model (e.g., days to recover 50% of max drawdown)")
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


class CompileStrategyDocumentationOutput(BaseModel):
    """Pydantic model for compile_strategy_documentation node outputs."""
    investment_thesis: str = (
        Field(..., description="A concise 200\u2011word description of the investment thesis behind the strategy")
    )
    signal_generation_flowchart: str = (
        Field(..., description="Markdown or textual representation of the flowchart describing the signal generation methodology")
    )
    risk_controls_table: str = (
        Field(..., description="Formatted table (as markdown text) listing risk control rules and their definitions")
    )
    parameter_ranges: str = (
        Field(..., description="Description of key model and execution parameters with recommended ranges")
    )
    performance_summary_table: str = (
        Field(..., description="Markdown table summarizing performance metrics (e.g., annualized return, Sharpe, drawdown) for baseline and optimized models")
    )
    system_requirements: str = (
        Field(..., description="List of hardware, software, and operational requirements needed to run the strategy")
    )


def compile_strategy_documentation(calculate_performance_metrics_input: CalculatePerformanceMetricsOutput, define_strategy_framework_input: DefineStrategyFrameworkOutput, **kwargs) -> CompileStrategyDocumentationOutput:
    """
    Generate a full strategy documentation package from framework and
    performance data.

    Returns
    -------
    dict
        A dictionary containing the six documentation sections defined in
        the output_structure.

    Raises
    ------
    KeyError
        If required fields from parent nodes are missing.
    ValueError
        If any generated section exceeds its length or formatting
        constraints.

    Examples
    --------
    >>> doc = compile_strategy_documentation()
    >>> print(doc['investment_thesis'])
    >>> print(doc['performance_summary_table'])
    A concise 200‑word investment thesis describing the market inefficiency the
    strategy exploits...\n| Metric                | Baseline | Optimized
    |\n|----------------------|----------|-----------|\n| Annualized Return    |
    0.12     | 0.18      |\n| Sharpe Ratio         | 1.4      | 2.1       |\n|
    Max Drawdown         | -0.08    | -0.05     |

    >>> doc = compile_strategy_documentation()
    >>> assert isinstance(doc['signal_generation_flowchart'], str)
    >>> assert doc['system_requirements'].startswith('Hardware')
    True

    """
    return CompileStrategyDocumentationOutput(
        investment_thesis="",
        signal_generation_flowchart="",
        risk_controls_table="",
        parameter_ranges="",
        performance_summary_table="",
        system_requirements="",
    )