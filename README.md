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

### Algorithm

1. **Input Parameters**:

   - Accept a folder path containing Excel files.
   - Define a list of parameter names to search for.

2. **Initialize Data Structure**:

   - Create an empty dictionary called `parameter_list`.

3. **Iterate Over Excel Files**:

   - For each file in the specified folder:
     - If the file is an Excel file:
       - Extract the filename to identify the team member (e.g., `person_name`).

4. **Read Excel Data**:

   - Load the Excel file into a DataFrame.

5. **Search for Parameters**:

   - For each parameter name in the predefined list:
     - Check for the parameter in columns A, D, and H:

       - If found, strip any leading/trailing whitespace from the cell value.
       - Store the `parameter_value` associated with the `person_name` in `parameter_list`:

         ```python
         parameter_list[param_name] = {person_name: parameter_value}
         ```

6. **Compile Results**:

   - After processing all files and parameters, ensure `parameter_list` contains all data collected from team members.

7. **Display Results**:
   - Build a Streamlit user interface:
     - Create dropdown selectors for the parameters.
     - Generate graphs to visualize the parameter values against team member names.
