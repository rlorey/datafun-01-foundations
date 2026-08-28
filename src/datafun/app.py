"""src/datafun/app.py - Project script.

Author: Rebecca Lorey
Date: 2026-08-20

HOW TO RUN THIS FILE:

From the VS Code menu (with only this project open in VS Code),
click "Terminal" / New Terminal to
open an integrated Terminal in the root project folder.
Paste the following command and press ENTER or RETURN
to run this file as a script:

uv run python -m datafun.app

DOMAIN:

A dataset of penguins.
See docs/data-card.md for more information about the dataset.

EXPLORE:

The data is loaded from a CSV file in the data/ folder.
Open that CSV in Excel and look at it.
One row of data represents one penguin.
We can
- open Excel and explore data OR
- open an editor and write Python

With Python, the instructions are write once / use as many times
as we like, and we can copy the instructions to other projects.
Work can be stored in GitHub and shared with others.

ORGANIZATION:

This file is the main script for the project.
Execution begins at the start of the main() function.
We organize the instructions into different files
(a Python file is called a module).
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
from eda_vizkit import save_chart, show_numeric_relationship
import matplotlib.pyplot as plt
import pandas as pd

from datafun.utils_data import get_analyst_description, inspect

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P01", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT, # they do NOT change when the program runs.
# By convention, constants are named in # UPPERCASE_WITH_UNDERSCORES.
# `Final` is added to indicate these variables # should not be reassigned.

# === PATHS ARE IMPORTANT ===

# Clearly define relative paths to important items (like data files).
# The `Python Standard Library` is available in every Python project.

# One of the modules in the Python Standard Library is `pathlib`,
# which provides classes for handling filesystem paths.

# === LOCATE THE DATA FILE ===

# Use the Path() constructor to create a Path object representing the "data" folder.
# Combine with the CSV file name
# to get the full path to the data file.
DATA_FILE_PATH: Final[Path] = Path("data") / "cricket_chirps_vs_temperature.csv"

# === OPEN THE DATA FILE IN EXCEL ===

# Look in the data/ folder. Open the file in Excel.
# Understand what is there and record your observations.

# === DETERMINE WHAT A ROW REPRESENTS ===

# CUSTOM: This is the GRAIN of the dataset - the single most
# important thing to know about any dataset.
# Come up with a short phrase that describes it.
# Fill this string value AFTER exploring the data.
GRAIN: Final[str] = "Number of chirps per second for a given temperature"  # CUSTOM

# === FIND A COLUMN YOU MIGHT BE ABLE TO PREDICT ===

# CUSTOM: Choose one NUMERIC target value that you might be able to predict
# from other columns in the dataset.
# This must match a numeric column name EXACTLY as it appears in the CSV file.
A_TARGET_WE_COULD_PREDICT: Final[str] = "Temperature_F"

# CUSTOM: Choose one other NUMERIC column
# as a FEATURE that might help predict the target.
# This must match a numeric column name EXACTLY as it appears in the CSV file.
A_FEATURE_THAT_MIGHT_HELP: Final[str] = "Chirps_Per_Second"

# CUSTOM: Document your thinking.
# Why do you think that feature could help predict the target?
# I said the following.
# The `r`` in front of the string indicates a `raw` string,
# so it is very forgiving - it'll show up in the log
# like I typed it.
# Open and close with three double quotes to get a multi-line string.
WHY_THE_FEATURE_MIGHT_HELP: Final[str] = r"""
It's possible that we could predict the temperature within a certain range given a number of cricket chirps per second."""


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point when running this file as a Python script.

    This is where the instructions begin.

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P01")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    # Use the imported privacy-preserving log_path() function
    # To indicate where we will look for the data file.
    log_path(LOG, "data file", path=DATA_FILE_PATH)

    # Call the built-in pandas `read_csv` function.
    # Store the tabular pandas DataFrame returned
    # in a local variable named `df`.

    df: pd.DataFrame = pd.read_csv(DATA_FILE_PATH)

    LOG.info("Data loaded successfully.")

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    # Call the inspect() function to get a string
    # with basic information about the DataFrame.
    # Pass in the pandas DataFrame (df)
    # The grain (what one row represents)
    # And the log so it knows where to send messages.

    inspection_string: str = inspect(df=df, grain=GRAIN, log=LOG)

    LOG.info(inspection_string)

    LOG.info("-------------------------------")
    LOG.info("03. DESCRIBE the data.")
    LOG.info("-------------------------------")

    # Call the get_analyst_description function.
    # Pass in the variables defined above.
    # The function will return a string
    # with a summary of the data from the analyst's perspective.

    summary_string: str = get_analyst_description(
        grain=GRAIN,
        target=A_TARGET_WE_COULD_PREDICT,
        feature=A_FEATURE_THAT_MIGHT_HELP,
        why=WHY_THE_FEATURE_MIGHT_HELP,
        log=LOG,
    )
    # Log the summary string.
    LOG.info(summary_string)

    LOG.info("-------------------------------")
    LOG.info("04. VISUALIZE the selected target and feature.")
    LOG.info("-------------------------------")

# Load data
df = pd.read_csv("data/cricket_chirps_vs_temperature.csv")


# 1. Safely locate your data file
DATA_FILE_PATH = Path("data") / "cricket_chirps_vs_temperature.csv"

if DATA_FILE_PATH.exists():
    df = pd.read_csv(DATA_FILE_PATH)
    
    # 2. Build the scatter plot visualization
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Chirps_Per_Second"], df["Temperature_F"], color="red", edgecolors="black", s=50)
    plt.title("Cricket Chirps vs Ambient Temperature")
    plt.xlabel("Chirps Per Second")
    plt.ylabel("Temperature (°F)")
    plt.grid(True, linestyle="--", alpha=0.6)
    
    # 3. Create the output folder and save it locally inside your project!
    OUTPUT_DIR = Path("docs/images")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    CHART_PATH = OUTPUT_DIR / "feature-target-scatter.png"
    plt.savefig(CHART_PATH, dpi=300)
    plt.close()
    print(f"🎉 Success! Your plot has been saved perfectly to: {CHART_PATH}")
else:
    print(f"❌ Error: Could not find the file at {DATA_FILE_PATH}. Please check your folder structure!")    
    

# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()

print("=========================================")
print("END main() – Executed successfully!")
print("=========================================")
