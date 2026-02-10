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


def calculate_performance_metrics(backtest_trading_signals_input: BacktestTradingSignalsOutput, optimize_model_parameters_input: OptimizeModelParametersOutput, **kwargs) -> CalculatePerformanceMetricsOutput:
    """
    Compute detailed performance metrics for baseline and optimized trading
    models.

    Parameters
    ----------
    baseline_backtest : dict
        Dictionary output from `backtest_trading_signals` for the baseline
        model containing keys: 'equity_curve' (list[float]), 'sharpe_ratio'
        (float), 'max_drawdown' (float), 'annualized_return' (float),
        'drawdown_duration_profile' (list[int]).
    optimized_params : dict
        Dictionary output from `optimize_model_parameters` containing the
        optimized parameter settings. Used to re‑run backtest internally for
        the optimized model.

    Returns
    -------
    dict
        Dictionary with the keys defined in the node's output_structure,
        each mapping to a float metric for baseline and optimized models.

    Raises
    ------
    ValueError
        If required keys are missing from inputs or if the equity curve
        lengths are inconsistent.
    RuntimeError
        If the optimized backtest fails to produce a valid equity curve.

    Examples
    --------
    >>> baseline = {
    ...     'equity_curve': [100, 102, 105, 103],
    ...     'sharpe_ratio': 1.2,
    ...     'max_drawdown': -0.04,
    ...     'annualized_return': 0.15,
    ...     'drawdown_duration_profile': [2, 3]
    >>> }
    >>> optimized_params = {'optimal_signal_parameters': ['threshold=0.6'],
    'optimal_position_sizing_parameters': ['vol_factor=1.1']}
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

    """
    return CalculatePerformanceMetricsOutput(
        baseline_annualized_return=0.0,
        optimized_annualized_return=0.0,
        baseline_sharpe_ratio=0.0,
        optimized_sharpe_ratio=0.0,
        baseline_sortino_ratio=0.0,
        optimized_sortino_ratio=0.0,
        baseline_calmar_ratio=0.0,
        optimized_calmar_ratio=0.0,
        baseline_win_rate=0.0,
        optimized_win_rate=0.0,
        baseline_avg_holding_period=0.0,
        optimized_avg_holding_period=0.0,
        baseline_drawdown_recovery_speed=0.0,
        optimized_drawdown_recovery_speed=0.0,
    )