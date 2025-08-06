# Currency Converter

A simple Python library and GUI application for converting between fiat currencies and Bitcoin (BTC) using the Coinbase API.

---

## Features

- **Real-time Conversion**: Convert any supported currency pair using live exchange rates from Coinbase.
- **Inverse Lookup**: Automatically falls back to inverse rate calculation if the direct pair is unavailable.
- **Historical Spot Prices**: Fetch and visualize the last 7 days of spot price history for any trading pair.
- **Graphical Interface**: User-friendly Tkinter GUI with conversion and history charting capabilities.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- `requests` library  
- `matplotlib` library  
- `tkinter` (usually included with standard Python installations)

### Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
