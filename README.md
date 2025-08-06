# Currency Converter

A simple Python-based currency converter supporting both fiat currencies and Bitcoin, with optional 7-day historical charting in a Tkinter GUI.

## Features

- **Fiat & Crypto Conversion**: Convert any supported fiat currency or Bitcoin (BTC) to another using Coinbase’s exchange-rates API.  
- **7-Day History Plot**: View the value of your converted amount over the past 7 days in a built-in GUI chart.  
- **Lightweight & Cache-Enabled**: Uses LRU caching to minimize redundant API calls.

## Table of Contents

- [Installation](#installation)  
- [Usage](#usage)  
  - [As a Module (CLI / Script)](#as-a-module-cli--script)  
  - [Graphical UI](#graphical-ui)  
- [Project Structure](#project-structure)  
- [Acknowledgements](#acknowledgements)  
- [License](#license)  

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/currency-converter.git
   cd currency-converter
