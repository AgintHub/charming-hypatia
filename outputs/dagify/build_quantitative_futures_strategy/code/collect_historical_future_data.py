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


def collect_historical_future_data(general_input: str, **kwargs) -> CollectHistoricalFutureDataOutput:
    """
    Collects multi‑year historical futures price, volume, and open‑interest data
    and returns it in a structured CSV format.

    Returns
    -------
    dict
        Dictionary containing: - **csv_rows** (List[str]): CSV rows with
        fields timestamp, contract_month, open, high, low, close, volume,
        open_interest. - **contracts** (List[str]): Identifiers of the
        contracts included. - **start_date** (str): ISO‑8601 start date of
        the dataset. - **end_date** (str): ISO‑8601 end date of the dataset.
        - **row_count** (int): Number of data rows (excluding header).

    Raises
    ------
    ConnectionError
        If the data provider service cannot be reached.
    ValueError
        If no contracts satisfy the 5‑year data requirement.
    RuntimeError
        If the retrieved data cannot be parsed into the expected CSV schema.

    Examples
    --------
    >>> result = collect_historical_future_data()
    {
        'csv_rows': [
            '2020-01-02 09:30:00,CLM2020,71.45,71.60,71.30,71.55,12000,50000',
            '2020-01-02 09:31:00,CLM2020,71.55,71.70,71.40,71.65,11500,50500',
            ...
        ],
        'contracts': ['CLM2020', 'CLU2020', 'CLZ2021'],
        'start_date': '2015-01-02',
        'end_date': '2023-12-31',
        'row_count': 1056000
    }

    >>> len(result['csv_rows'])
    >>> result['row_count']
    1056000
    1056000

    """
    return CollectHistoricalFutureDataOutput(
        csv_rows=[],
        contracts=[],
        start_date="",
        end_date="",
        row_count=0,
    )