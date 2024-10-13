import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Source of excel files
folder_path = "/Users/suryaganesan/Documents/GitHub/UAS-initial-sizing/source"

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

st.title("UAS Sizing Graphs")

# Calculate the number of rows and columns for subplots
num_plots = len(parameter_list)
cols = 3
rows = (num_plots - 1) // cols + 1

fig, axes = plt.subplots(rows, cols, figsize=(8, 2.2 * rows))
plt.subplots_adjust(hspace=2, wspace=2)
axes = axes.flatten()

for index, (parameter_name, person_values) in enumerate(parameter_list.items()):

    if index < len(axes):
        ax = axes[index]

        # Graph for each parameter on the list
        people = list(person_values.keys())
        values = list(person_values.values())

        x = np.arange(len(people))

        ax.bar(people, values, width=0.6)
        ax.set_xlabel("People", fontsize=6)
        ax.set_ylabel("Value", fontsize=6)
        ax.set_title(f"{parameter_name}", fontsize=8)
        ax.set_xticks(x)
        ax.set_xticklabels(people, rotation=45, ha="right", fontsize=6)
        ax.tick_params(axis="y", labelsize=8)

# Remove any unused subplots
for i in range(index + 1, len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
st.pyplot(fig)
