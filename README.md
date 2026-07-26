# Inventory Reorder Alert

This project is a simple Python script that checks stock levels from a CSV file and flags items that need restocking.

## Features
- Reads stock data from `stock.csv`
- Compares current quantity with reorder threshold
- Flags items as **Critical** (below 25% of threshold) or **Low**
- Suggests reorder quantity
- Prints a report to console
- Exports results to `restock_report.csv`

## Usage
1. Place `stock.csv` in the same folder as the script.
2. Run the script:
