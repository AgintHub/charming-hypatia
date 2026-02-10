# backtest_trading_signals PRD

## Description
Validate strategy performance on historical data using walk‑forward analysis with 12‑month rolling windows and report key performance metrics.


## Conceptual Info

Executes a walk‑forward backtest of the generated trading signals, applying the signal model, regression‑based forecasts, and liquidity control rules across successive 12‑month windows. It aggregates portfolio equity over time and computes standard risk‑adjusted performance statistics.

## Docstring

### Summary
Run a 12‑month rolling walk‑forward backtest of the strategy and return key performance metrics.

### Returns

dict: Dictionary containing `equity_curve`, `sharpe_ratio`, `max_drawdown`, `annualized_return`, and `drawdown_duration_profile` as defined in the output structure.

### Raises

- ValueError: If any of the dependent nodes fail to produce required inputs (e.g., missing model pseudocode or liquidity rules).
- RuntimeError: If the backtest simulation encounters an unexpected error such as data misalignment or division by zero.

### Examples

```python
>>> results = backtest_trading_signals()
{
  'equity_curve': [100000.0, 101200.5, 102450.3, ...],
  'sharpe_ratio': 1.45,
  'max_drawdown': -0.12,
  'annualized_return': 0.18,
  'drawdown_duration_profile': [5, 12, 7]
}
```

```python
>>> print(f"Annualized Return: {results['annualized_return']:.2%}")
Annualized Return: 18.00%
```
