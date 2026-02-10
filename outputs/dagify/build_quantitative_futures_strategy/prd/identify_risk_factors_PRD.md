# identify_risk_factors PRD

## Description
Determine macroeconomic and market risk factors affecting futures


## Conceptual Info

The node extracts a concise set of macro‑economic and market variables that materially influence futures prices. By classifying each factor as a price driver, volatility factor, or liquidity risk, downstream feature engineering can incorporate appropriately weighted inputs for signal generation and risk management.

## Docstring

### Summary
Identify key risk factors for futures trading and classify each factor.

### Returns

Tuple[List[str], List[str]]: A tuple where the first element is a list of risk factor names and the second element is a parallel list of categories ("price driver", "volatility factor", or "liquidity risk").

### Raises

- RuntimeError: If the underlying language model fails to produce a parsable list of factors or categories.
- ValueError: If the lengths of the two returned lists differ.

### Examples

```python
>>> risk_factors, categories = identify_risk_factors()
(['Interest Rates', 'Crude Oil Prices', 'USD/EUR Exchange Rate', 'VIX Index', 'Gold Spot Price', 'Eurodollar Futures', 'Natural Gas Futures', 'S&P 500 Futures'],
 ['price driver', 'price driver', 'price driver', 'volatility factor', 'price driver', 'liquidity risk', 'liquidity risk', 'price driver'])
```

```python
>>> risk_factors, categories = identify_risk_factors()
>>> print(risk_factors[2])
>>> print(categories[2])
"USD/EUR Exchange Rate"
"price driver"
```
