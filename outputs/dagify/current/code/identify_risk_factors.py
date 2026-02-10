from pydantic import BaseModel, Field
from typing import List


class IdentifyRiskFactorsOutput(BaseModel):
    """Pydantic model for identify_risk_factors node outputs."""
    risk_factors: List[str] = (
        Field(..., description="List of identified risk factor names (e.g., \"Interest Rates\", \"Crude Oil Prices\")")
    )
    risk_factor_categories: List[str] = (
        Field(..., description="Parallel list indicating the category for each risk factor in risk_factors; each entry is one of \"price driver\", \"volatility factor\", or \"liquidity risk\"")
    )


def identify_risk_factors(general_input: str, **kwargs) -> IdentifyRiskFactorsOutput:
    """
    Identify key risk factors for futures trading and classify each factor.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple where the first element is a list of risk factor names and
        the second element is a parallel list of categories ("price driver",
        "volatility factor", or "liquidity risk").

    Raises
    ------
    RuntimeError
        If the underlying language model fails to produce a parsable list of
        factors or categories.
    ValueError
        If the lengths of the two returned lists differ.

    Examples
    --------
    >>> risk_factors, categories = identify_risk_factors()
    (['Interest Rates', 'Crude Oil Prices', 'USD/EUR Exchange Rate', 'VIX
    Index', 'Gold Spot Price', 'Eurodollar Futures', 'Natural Gas Futures', 'S&P
    500 Futures'],
     ['price driver', 'price driver', 'price driver', 'volatility factor',
    'price driver', 'liquidity risk', 'liquidity risk', 'price driver'])

    >>> risk_factors, categories = identify_risk_factors()
    >>> print(risk_factors[2])
    >>> print(categories[2])
    "USD/EUR Exchange Rate"
    "price driver"

    """
    return IdentifyRiskFactorsOutput(
        risk_factors=[],
        risk_factor_categories=[],
    )