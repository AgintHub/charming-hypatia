# collect_historical_future_data PRD

## Description
Retrieve historical futures price data for targeted contracts


## Conceptual Info

This node gathers extensive historical price and volume information for a set of futures contracts spanning at least five years. The raw data is organized into CSV rows, each timestamped and annotated with contract month, enabling downstream cleaning, analysis, and strategy development.

## Docstring

### Summary
Collects multi‑year historical futures price, volume, and open‑interest data and returns it in a structured CSV format.

### Returns

dict: Dictionary containing:
- **csv_rows** (List[str]): CSV rows with fields timestamp, contract_month, open, high, low, close, volume, open_interest.
- **contracts** (List[str]): Identifiers of the contracts included.
- **start_date** (str): ISO‑8601 start date of the dataset.
- **end_date** (str): ISO‑8601 end date of the dataset.
- **row_count** (int): Number of data rows (excluding header).

### Raises

- ConnectionError: If the data provider service cannot be reached.
- ValueError: If no contracts satisfy the 5‑year data requirement.
- RuntimeError: If the retrieved data cannot be parsed into the expected CSV schema.

### Examples

```python
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
```

```python
>>> len(result['csv_rows'])
>>> result['row_count']
1056000
1056000
```
