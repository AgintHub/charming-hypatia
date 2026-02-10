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


def analyze_market_structure(process_historical_data_input: ProcessHistoricalDataOutput, calculate_statistical_metrics_input: CalculateStatisticalMetricsOutput, **kwargs) -> AnalyzeMarketStructureOutput:
    """
    Analyze market depth and liquidity regimes to produce participation,
    slippage, latency, and pattern insights.

    Parameters
    ----------
    cleaned_data_csv : str
        CSV string from `process_historical_data` containing timestamped
        OHLCV and open‑interest data.
    statistical_metrics : dict
        Dictionary from `calculate_statistical_metrics` containing return
        moments and volatility‑clustering metrics for each contract series.

    Returns
    -------
    dict
        Dictionary with keys matching the node's output_structure:
        participation_rates, slippage_estimates, latency_sensitivity,
        day_of_week_patterns, time_of_day_patterns, and summary_report.

    Raises
    ------
    ValueError
        If `cleaned_data_csv` is empty or malformed.
    KeyError
        If required fields are missing from `statistical_metrics`.

    Examples
    --------
    >>> cleaned_csv =
    "timestamp,open,high,low,close,volume,open_interest\n2023-01-01
    09:30,100,101,99,100.5,5000,2000"
    >>> stats = {"contract_series": ["CL_F2023"], "daily_return_std": [0.015]}
    >>> result = analyze_market_structure(cleaned_csv, stats)
    >>> result['summary_report']
    "The market exhibits high participation during morning sessions with low
    slippage, but latency sensitivity rises sharply after 14:00 UTC. Monday
    shows consistently high depth, while the 09:30‑11:30 window is the most
    liquid."

    >>> cleaned_csv =
    "timestamp,open,high,low,close,volume,open_interest\n2023-01-02
    10:00,200,202,198,201,8000,3000"
    >>> stats = {"contract_series": ["GC_F2023"], "daily_return_std": [0.02]}
    >>> result = analyze_market_structure(cleaned_csv, stats)
    >>> result['participation_rates']
    [0.12, 0.15, 0.09, 0.11]

    """
    return AnalyzeMarketStructureOutput(
        participation_rates=[],
        slippage_estimates=[],
        latency_sensitivity=[],
        day_of_week_patterns=[],
        time_of_day_patterns=[],
        summary_report="",
    )