# Currency Converter

A simple currency conversion tool leveraging the Coinbase API, with both a Python module and a graphical interface.

## Files

- **currency_converter.py**  
  • Fetches live exchange rates and spot price history via Coinbase  
  • Functions:  
  &nbsp;&nbsp;– `get_exchange_rates(base: str) -> dict`  
  &nbsp;&nbsp;– `get_coinbase_time() -> datetime`  
  &nbsp;&nbsp;– `get_spot_history(pair: str, start: str, end: str) -> dict`  
  &nbsp;&nbsp;– `convert_currency(from_currency: str, to_currency: str, amount: float) -> float`

- **currency_gui.py**  
  • Builds a Tkinter window for interactive conversions  
  • Enter “From”/“To” currency codes and amount, then click **Convert**  
  • Optional **Show 7 Day History** button plots recent spot‐price movements

## Requirements

- Python 3.7 or higher  
- [requests](https://pypi.org/project/requests/)  
- [matplotlib](https://pypi.org/project/matplotlib/)  
- Tkinter (bundled with most Python installations)

## Installation

```bash
# Install dependencies
pip install requests matplotlib
```
## Usage
**As a module**
```python
from currency_converter import convert_currency

amount_in_eur = convert_currency("USD", "EUR", 100.0)
print(f"100 USD = {amount_in_eur:.2f} EUR")
```
**GUI Application**
```bash
python currency_gui.py
```
## Acknowledgements

- **Coinbase API** maintainers for providing free and reliable exchange-rate data.  
- **Requests** library authors for an easy-to-use HTTP client in Python.  
- **Matplotlib** contributors for the plotting framework used in the GUI history chart.  
- The **Tkinter** team for the built-in Python GUI toolkit.  



## License
**MIT License**
Copyright (c) 2025


