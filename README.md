# UAS Initial Sizing Dashboard for Aircraft Design

## Purppose
The script addresses the challenge of efficiently comparing and analyzing UAV (Unmanned Aerial Vehicle) sizing inputs provided by multiple individuals working from the same template. In UAV design, critical parameters such as cruise range, payload capacity, wing span, and battery performance are often input manually into spreadsheets by different team members. Without a clear, visual method to compare these inputs, identifying discrepancies or aligning design decisions becomes time-consuming and prone to error.

This script provides a solution by automating the extraction of key UAV sizing parameters from multiple Excel files and generating an interactive dashboard using Streamlit.

## Tech Stack & Dependencies
- Python
- Pandas
- Openpyxl
- Streamlit
- Plotly

## Algorithm
- The application is provided with a folder path where several excel templates with measurements are filled in my templates. A list of parameter names is provided as a list variable which it looks for in columns A, 
