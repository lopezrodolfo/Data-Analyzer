# Data Analyzer

A Python module for importing, analyzing, and graphing data with linear relationships.

## Authors

Rodolfo Lopez

## Date

Fall 2019

## Features

- Calculate arithmetic mean
- Separate x and y values from data points
- Calculate regression slope
- Plot linear regression line
- Create scatter plots
- Read data from CSV files

## Requirements

- Python 3.x
- matplotlib

## Installation

1. Clone this repository or download the source code.
2. Install the required dependency:

```
pip install matplotlib
```

## Usage

1. Place your CSV data file in the same directory as `data_analyzer.py`.
2. Run the script:

   ```
   python data_analyzer.py
   ```

3. Enter the name of your CSV file when prompted.
4. The script will generate a scatter plot with a line of best fit.

## CSV File Format

- First row: column headers (x-label, y-label)
- Subsequent rows: x-value, y-value pairs
