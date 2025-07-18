import requests
from functools import lru_cache
"""
This provides provides functions to convert between different currencies using the Coinbase API.
It supports both fiat currencies and Bitcoin (BTC) conversions.
"""
@lru_cache(maxsize=32)
def get_exchange_rates(base: str) -> dict:
    """
    Fetch all exchange rates for `base` from Coinbase.
    Returns a mapping of target‑currency → rate (as strings).
    """
    url    = "https://api.coinbase.com/v2/exchange-rates"
    params = {"currency": base}
    resp   = requests.get(url, params=params, timeout=5)
    resp.raise_for_status()
    data   = resp.json()
    return data["data"]["rates"]

def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    """
    Convert `amount` of from_currency → to_currency using Coinbase exchange-rates.
    
    1. Try direct: rate = rates[to_currency]  
    2. If not found (e.g. unsupported pair), fetch the inverse rates and invert.
    """
    fr = from_currency.strip().upper()
    to = to_currency.strip().upper()

    if fr == to:
        return amount

    # direct lookup
    rates = get_exchange_rates(fr)
    if to in rates:
        return amount * float(rates[to])

    # fallback to inverse lookup
    inv = get_exchange_rates(to)
    if fr in inv:
        return amount / float(inv[fr])