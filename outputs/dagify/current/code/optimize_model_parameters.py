from pydantic import BaseModel, Field
from typing import List


class BacktestTradingSignalsOutput(BaseModel):
    """Pydantic model for backtest_trading_signals node outputs."""
    equity_curve: List[float] = (
        Field(..., description="Time\u2011series of portfolio equity values for each backtest period")
    )
    sharpe_ratio: float = (
        Field(..., description="Annualized Sharpe ratio of the backtested strategy")
    )
    max_drawdown: float = (
        Field(..., description="Maximum percentage drawdown observed across all walk\u2011forward windows")
    )
    annualized_return: float = (
        Field(..., description="Overall annualized return percentage from the backtest")
    )
    drawdown_duration_profile: List[int] = (
        Field(..., description="List of drawdown durations (in days) for each observed drawdown event")
    )


class OptimizeModelParametersOutput(BaseModel):
    """Pydantic model for optimize_model_parameters node outputs."""
    optimal_signal_parameters: List[str] = (
        Field(..., description="List of signal generation parameter settings in \"param=value\" format that achieved the best cross\u2011validation performance")
    )
    optimal_position_sizing_parameters: List[str] = (
        Field(..., description="List of position sizing parameter settings in \"param=value\" format derived from the optimization")
    )
    cross_validation_score: float = (
        Field(..., description="Aggregate performance metric (e.g., average Sharpe ratio) obtained during cross\u2011validation for the selected parameters")
    )
    walk_forward_consistency: bool = (
        Field(..., description="Indicates whether the optimized parameters maintained performance across walk\u2011forward windows")
    )
    parameter_ranges_documentation: str = (
        Field(..., description="Markdown\u2011formatted text summarizing the acceptable ranges for each tuned hyperparameter")
    )


def optimize_model_parameters(backtest_trading_signals_input: BacktestTradingSignalsOutput, **kwargs) -> OptimizeModelParametersOutput:
    """
    Optimize signal generation and position sizing hyper‑parameters via
    cross‑validation and walk‑forward analysis.

    Returns
    -------
    dict
        Dictionary containing keys `optimal_signal_parameters`,
        `optimal_position_sizing_parameters`, `cross_validation_score`,
        `walk_forward_consistency`, and `parameter_ranges_documentation` as
        defined in the node's output_structure.

    Raises
    ------
    RuntimeError
        If the dependent backtest data is unavailable or fails validation.
    ValueError
        If the optimization process does not converge to a feasible
        solution.

    Examples
    --------
    >>> results = optimize_model_parameters()
    >>> print(results['optimal_signal_parameters'])
    >>> print(results['cross_validation_score'])
    ["lookback=20", "threshold=0.05"]\n0.82

    >>> # Example of full result dictionary
    >>> results = {
    ...     "optimal_signal_parameters": ["ma_fast=10", "ma_slow=30"],
    ...     "optimal_position_sizing_parameters": ["vol_multiplier=1.2",
    "max_exposure=0.15"],
    ...     "cross_validation_score": 0.87,
    ...     "walk_forward_consistency": true,
    ...     "parameter_ranges_documentation": "## Parameter Ranges\n- ma_fast:
    5‑15\n- ma_slow: 20‑40\n- vol_multiplier: 0.8‑1.5\n- max_exposure: 0.1‑0.2"
    >>> }
    >>> print(results['walk_forward_consistency'])
    True

    """
    return OptimizeModelParametersOutput(
        optimal_signal_parameters=[],
        optimal_position_sizing_parameters=[],
        cross_validation_score=0.0,
        walk_forward_consistency=False,
        parameter_ranges_documentation="",
    )