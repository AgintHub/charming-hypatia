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


def calculate_statistical_metrics(process_historical_data_input: ProcessHistoricalDataOutput, **kwargs) -> CalculateStatisticalMetricsOutput:
    """
    Calculate statistical return metrics for multiple futures contract series
    from cleaned price data.

    Parameters
    ----------
    cleaned_data_csv : str
        CSV‑formatted string produced by `process_historical_data`,
        containing columns: timestamp, open, high, low, close, volume,
        open_interest.

    Returns
    -------
    dict
        Dictionary with keys matching the node's output_structure, each
        holding the computed metric list or summary string.

    Raises
    ------
    ValueError
        If the CSV cannot be parsed, lacks required columns, or contains
        insufficient data for a given contract series.
    RuntimeError
        If numerical computations (e.g., division by zero in volatility
        clustering) fail.

    Examples
    --------
    >>> csv_data = ("timestamp,open,high,low,close,volume,open_interest\n"
    ...             "2023-01-01 09:30,100,101,99,100.5,2000,10\n"
    ...             "2023-01-02 09:30,100.5,102,100,101,2100,11")
    >>> metrics = calculate_statistical_metrics(csv_data)
    {
      'contract_series': ['CL_FUT'],
      'daily_return_mean': [0.005],
      'daily_return_std': [0.0012],
      'weekly_return_mean': [0.032],
      'weekly_return_std': [0.005],
      'monthly_return_mean': [0.128],
      'monthly_return_std': [0.020],
      'volatility_clustering_metric': [1.45],
      'skewness': [0.12],
      'kurtosis': [3.4],
      'time_weighted_summary': 'Daily mean 0.5 %, weekly mean 3.2 %, monthly
    mean 12.8 %, volatility clustering 1.45, skew 0.12, kurtosis 3.4.'
    }

    >>> # Missing required column triggers an error
    >>> bad_csv = "timestamp,open,high,low,volume,open_interest\n2023-01-01
    09:30,100,101,99,2000,10"
    >>> calculate_statistical_metrics(bad_csv)
    ValueError: CSV must contain a 'close' column.

    """
    return CalculateStatisticalMetricsOutput(
        contract_series=[],
        daily_return_mean=[],
        daily_return_std=[],
        weekly_return_mean=[],
        weekly_return_std=[],
        monthly_return_mean=[],
        monthly_return_std=[],
        volatility_clustering_metric=[],
        skewness=[],
        kurtosis=[],
        time_weighted_summary="",
    )