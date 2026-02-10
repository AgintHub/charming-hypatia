from pydantic import BaseModel, Field
from typing import List


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


class ValidateOverfittingRiskOutput(BaseModel):
    """Pydantic model for validate_overfitting_risk node outputs."""
    tested_regimes: List[str] = (
        Field(..., description="Names of market regimes used in the stress test (e.g., bull, bear, high-volatility).")
    )
    degradation_scores: List[float] = (
        Field(..., description="Quantitative measure of backtesting performance degradation for each regime (e.g., drop in Sharpe ratio).")
    )
    affected_parameter_ranges: List[str] = (
        Field(..., description="String representations of parameter ranges that led to significant performance drops in each regime.")
    )
    robustness_summary: str = (
        Field(..., description="Brief textual summary indicating overall model robustness and any regimes of concern.")
    )
    is_robust: bool = (
        Field(..., description="Flag indicating whether the model passes a predefined robustness criterion across all tested regimes.")
    )


def validate_overfitting_risk(optimize_model_parameters_input: OptimizeModelParametersOutput, **kwargs) -> ValidateOverfittingRiskOutput:
    """
    Stress‑tests optimized model parameters across multiple market regimes and
    reports robustness metrics.

    Parameters
    ----------
    optimized_parameters : dict
        Dictionary of parameter settings returned by
        `optimize_model_parameters`. Keys are parameter names and values are
        the selected values (e.g., {'signal_threshold': 0.45,
        'position_scale': 1.2}).
    regime_definitions : dict
        Mapping of regime name to a callable that filters historical data to
        that regime. Example: {'bull': bull_filter, 'bear': bear_filter,
        ...}.

    Returns
    -------
    dict
        A dictionary containing the five output fields defined in
        `output_structure`.

    Raises
    ------
    ValueError
        If `optimized_parameters` is empty or missing required keys.
    KeyError
        If a requested regime is not present in `regime_definitions`.
    RuntimeError
        If back‑testing fails for any regime due to data issues.

    Examples
    --------
    >>> result = validate_overfitting_risk(
    ...     optimized_parameters={'signal_threshold': 0.48, 'position_scale':
    1.1},
    ...     regime_definitions={
    ...         'bull': bull_filter,
    ...         'bear': bear_filter,
    ...         'high_vol': high_vol_filter,
    ...         'low_vol': low_vol_filter,
    ...         'sideways': sideways_filter
    ...     }
    >>> )
    {'tested_regimes': ['bull', 'bear', 'high_vol', 'low_vol', 'sideways'],
    'degradation_scores': [0.02, 0.15, 0.09, 0.03, 0.05],
    'affected_parameter_ranges': ['signal_threshold: 0.30‑0.55',
    'position_scale: 0.8‑1.3', 'signal_threshold: 0.30‑0.55', 'position_scale:
    0.9‑1.2', 'signal_threshold: 0.35‑0.50'], 'robustness_summary': 'Model
    remains robust in bull, low_vol and sideways regimes (≤5% Sharpe drop) but
    degrades in bear regime (15% drop).', 'is_robust': False}

    >>> result = validate_overfitting_risk(
    ...     optimized_parameters={'signal_threshold': 0.55, 'position_scale':
    0.9},
    ...     regime_definitions={'bull': bull_filter, 'bear': bear_filter,
    'high_vol': high_vol_filter, 'low_vol': low_vol_filter, 'sideways':
    sideways_filter}
    >>> )
    {'tested_regimes': ['bull', 'bear', 'high_vol', 'low_vol', 'sideways'],
    'degradation_scores': [0.01, 0.04, 0.02, 0.01, 0.03],
    'affected_parameter_ranges': ['signal_threshold: 0.50‑0.60',
    'signal_threshold: 0.50‑0.60', 'signal_threshold: 0.50‑0.60',
    'signal_threshold: 0.50‑0.60', 'signal_threshold: 0.50‑0.60'],
    'robustness_summary': 'All regimes show ≤4% Sharpe degradation; model is
    robust.', 'is_robust': True}

    """
    return ValidateOverfittingRiskOutput(
        tested_regimes=[],
        degradation_scores=[],
        affected_parameter_ranges=[],
        robustness_summary="",
        is_robust=False,
    )