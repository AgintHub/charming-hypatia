from pydantic import BaseModel, Field
from typing import List


class CollectHistoricalFutureDataOutput(BaseModel):
    """Pydantic model for collect_historical_future_data node outputs."""
    csv_rows: List[str] = (
        Field(..., description="List of CSV-formatted rows, each row representing a timestamped record with fields: timestamp, contract_month, open, high, low, close, volume, open_interest")
    )
    contracts: List[str] = (
        Field(..., description="List of contract identifiers (e.g., futures symbols and months) included in the collected dataset")
    )
    start_date: str = (
        Field(..., description="Earliest date (inclusive) of the collected data in ISO 8601 format (YYYY-MM-DD)")
    )
    end_date: str = (
        Field(..., description="Latest date (inclusive) of the collected data in ISO 8601 format (YYYY-MM-DD)")
    )
    row_count: int = (
        Field(..., description="Total number of data rows collected (excluding header)")
    )


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


def process_historical_data(collect_historical_future_data_input: CollectHistoricalFutureDataOutput, **kwargs) -> ProcessHistoricalDataOutput:
    """
    Clean and normalize raw futures CSV rows into a continuous, regularly‑spaced
    dataset.

    Parameters
    ----------
    raw_csv_rows : List[str]
        List of CSV‑formatted rows produced by
        `collect_historical_future_data`. Each row contains: timestamp,
        contract_month, open, high, low, close, volume, open_interest.

    Returns
    -------
    dict
        Dictionary containing cleaned_data_csv, record_count,
        start_timestamp, end_timestamp, time_interval_minutes, and
        is_successful as defined in the node's output structure.

    Raises
    ------
    ValueError
        If raw_csv_rows is empty or missing required columns.
    RuntimeError
        If the cleaning process cannot infer a uniform time interval or
        fails during contract rollover stitching.

    Examples
    --------
    >>> result = process_historical_data([
    ...     "2020-01-01T09:30:00Z,2020F,100,101,99,100.5,2000,1500",
    ...     "2020-01-01T09:31:00Z,2020F,100.5,102,100,101,2100,1520"
    >>> ])
    >>> print(result['record_count'])
    2

    >>> result = process_historical_data(raw_csv_rows)
    >>> print(result['is_successful'])
    >>> print(result['time_interval_minutes'])
    True\n1

    """
    return ProcessHistoricalDataOutput(
        cleaned_data_csv="",
        record_count=0,
        start_timestamp="",
        end_timestamp="",
        time_interval_minutes=0,
        is_successful=False,
    )