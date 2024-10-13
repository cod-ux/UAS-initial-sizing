import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Source of excel files
folder_path = "/Users/suryaganesan/Documents/GitHub/UAS-initial-sizing/source"

# Streamlit Page Setup
st.set_page_config(layout="wide")

# List of parameter names in the file
parameter_names = [
    "Cruise Range",
    "Estimated Cruise Velocity",
    "Maximum expendable payload mass",
    "Maximum non-expendable payload mass",
    "Total payload mass",
    "Cruise Altitude",
    "Loiter Endurance",
    "Estimated Loiter Velocity",
    "Wing Span",
    "Wing Area",
    "Aspect Ratio",
    "Battery mass",
    "Battery Voltage",
    "Battery Capacity",
    "Battery Espec",
    "BatteryMF - Cruise",
    "BatteryMF- Loiter",
    "Compound Efficiency",
    "Usable Proportion Factor",
    "Cd0",
    "e",
    "k",
    "Clmd",
    "Cdmd",
    "Clmp",
    "Cdmp",
    "Clmd/Cdmd",
    "Clmp/Cdmp",
    "A",
    "Kvs",
    "c",
    "Intercept",
    "Estimated Battery MF",
]

# Dictionary for storing param_name - against {person_name: values}
parameter_list = {param_name: {} for param_name in parameter_names}

# Loop through files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path, sheet_name="Aircraft Sizing")
        person_name = os.path.splitext(filename)[0]

        # Find parameters and their values
        for param_name in parameter_names:
            param_row = df[df.iloc[:, 0] == param_name]
            if not param_row.empty:
                param_value = param_row.iloc[0, 1]
                parameter_list[param_name][person_name] = param_value
            else:
                parameter_list[param_name][person_name] = np.nan

print(parameter_list)


def create_chart(param_data, param_name):
    df = pd.DataFrame(list(param_data.items()), columns=["person_name", "param_value"])
    fig = px.line(
        df,
        x="person_name",
        y="param_value",
        title=f"{param_name} Chart",
        #        text="person_name",
        labels=False,
        markers=True,
    )
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(xaxis_title="Person Name", yaxis_title=param_name)
    fig.update_traces(
        hoverinfo="text",
        textposition="bottom center",
        text=person_name,
        marker=dict(symbol="hourglass", size=8),
    )

    return fig


# Streamlit Title
st.title("Parameter Charts")

# Create a 2x2 grid for the charts
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# List of columns for easy iteration
columns = [col1, col2, col3, col4]

# Create four charts with individual dropdowns
for i, column in enumerate(columns):
    with column:
        # Dropdown to select a parameter for this chart
        selected_param = st.selectbox(
            f"Select parameter for Chart {i+1}",
            list(parameter_list.keys()),
            key=f"dropdown_{i}",
        )

        # Display the selected parameter chart
        chart = create_chart(parameter_list[selected_param], selected_param)
        st.plotly_chart(chart, use_container_width=True, key=f"chart_{i}")
