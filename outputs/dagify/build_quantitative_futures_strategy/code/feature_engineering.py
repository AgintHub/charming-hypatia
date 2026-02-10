from pydantic import BaseModel, Field
from typing import List


class ProcessHistoricalDataOutput(BaseModel):
    """Pydantic model for process_historical_data node outputs."""
    cleaned_data_csv: str = (
        Field(..., description="CSV formatted string of the cleaned dataset, including header row with columns such as timestamp, open, high, low, close, volume, open_interest")
    )
    record_count: int = (
        Field(..., description="Number of rows/records in the cleaned dataset")
    )
    start_timestamp: str = (
        Field(..., description="ISO8601 timestamp of the first record in the cleaned dataset")
    )
    end_timestamp: str = (
        Field(..., description="ISO8601 timestamp of the last record in the cleaned dataset")
    )
    time_interval_minutes: int = (
        Field(..., description="Uniform time interval in minutes between consecutive records in the cleaned dataset")
    )
    is_successful: bool = (
        Field(..., description="Indicates whether the cleaning and normalization process completed without errors")
    )


class IdentifyRiskFactorsOutput(BaseModel):
    """Pydantic model for identify_risk_factors node outputs."""
    risk_factors: List[str] = (
        Field(..., description="List of identified risk factor names (e.g., \"Interest Rates\", \"Crude Oil Prices\")")
    )
    risk_factor_categories: List[str] = (
        Field(..., description="Parallel list indicating the category for each risk factor in risk_factors; each entry is one of \"price driver\", \"volatility factor\", or \"liquidity risk\"")
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


def feature_engineering(process_historical_data_input: ProcessHistoricalDataOutput, identify_risk_factors_input: IdentifyRiskFactorsOutput, **kwargs) -> FeatureEngineeringOutput:
    """
    Generate engineered predictive features from cleaned futures data and macro
    risk factors, and rank them by predictive importance.

    Parameters
    ----------
    cleaned_data_csv : str
        CSV string containing the cleaned, uniformly‑spaced futures price
        and volume series produced by `process_historical_data`.
    risk_factors : List[str]
        List of macro‑economic or market risk factor names identified by
        `identify_risk_factors`.
    risk_factor_categories : List[str]
        Parallel list indicating each risk factor's category ("price
        driver", "volatility factor", or "liquidity risk").

    Returns
    -------
    dict
        Dictionary with keys `feature_names`, `feature_descriptions`,
        `feature_importance_scores`, `selected_feature_names`, and
        `selected_feature_importance` matching the node's output_structure.

    Raises
    ------
    ValueError
        If the CSV cannot be parsed or required columns are missing.
    RuntimeError
        If feature ranking fails due to insufficient data or singular matrix
        errors.

    Examples
    --------
    >>> cleaned_csv =
    "timestamp,open,high,low,close,volume,open_interest\n2023-01-01
    09:30,100,101,99,100.5,5000,10\n2023-01-01 09:31,100.5,102,100,101,5200,10"
    >>> risk_factors = ["Interest Rates", "Crude Oil Prices"]
    >>> risk_factor_categories = ["price driver", "price driver"]
    >>> features = feature_engineering(cleaned_csv, risk_factors,
    risk_factor_categories)
    {
      'feature_names': ['rsi_14', 'macd_hist', 'vol_surface_30d', ...],
      'feature_descriptions': ['14‑period Relative Strength Index', 'MACD
    histogram', '30‑day implied volatility surface', ...],
      'feature_importance_scores': [0.12, 0.09, 0.15, ...],
      'selected_feature_names': ['vol_surface_30d', 'rsi_14',
    'macro_spread_interest_crude'],
      'selected_feature_importance': [0.15, 0.12, 0.11]
    }

    >>> # When the input CSV is empty, the function raises an informative error
    >>> feature_engineering('', [], [])
    ValueError: Input CSV is empty or missing required columns.

    """
    return FeatureEngineeringOutput(
        feature_names=[],
        feature_descriptions=[],
        feature_importance_scores=[],
        selected_feature_names=[],
        selected_feature_importance=[],
    )