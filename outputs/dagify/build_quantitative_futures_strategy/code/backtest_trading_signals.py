from pydantic import BaseModel, Field
from typing import List


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


def backtest_trading_signals(build_signal_generation_model_input: BuildSignalGenerationModelOutput, model_regression_based_strategy_input: ModelRegressionBasedStrategyOutput, create_liquidity_control_rules_input: CreateLiquidityControlRulesOutput, **kwargs) -> BacktestTradingSignalsOutput:
    """
    Run a 12‑month rolling walk‑forward backtest of the strategy and return key
    performance metrics.

    Returns
    -------
    dict
        Dictionary containing `equity_curve`, `sharpe_ratio`,
        `max_drawdown`, `annualized_return`, and `drawdown_duration_profile`
        as defined in the output structure.

    Raises
    ------
    ValueError
        If any of the dependent nodes fail to produce required inputs (e.g.,
        missing model pseudocode or liquidity rules).
    RuntimeError
        If the backtest simulation encounters an unexpected error such as
        data misalignment or division by zero.

    Examples
    --------
    >>> results = backtest_trading_signals()
    {
      'equity_curve': [100000.0, 101200.5, 102450.3, ...],
      'sharpe_ratio': 1.45,
      'max_drawdown': -0.12,
      'annualized_return': 0.18,
      'drawdown_duration_profile': [5, 12, 7]
    }

    >>> print(f"Annualized Return: {results['annualized_return']:.2%}")
    Annualized Return: 18.00%

    """
    return BacktestTradingSignalsOutput(
        equity_curve=[],
        sharpe_ratio=0.0,
        max_drawdown=0.0,
        annualized_return=0.0,
        drawdown_duration_profile=[],
    )