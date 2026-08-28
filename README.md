# datafun-01-foundations

> Professional Python project: inspect data and plan experiments.

Hello! I'm Rebecca Lorey. Welcome to my foundational data analysis repository. This introductory data analytics project is centered on structured development and reproducible workflows for data analysis. Key areas covered include variable configurations, script orchestration, status logging, and data documentation to reliably import, inspect, and summarize incoming data streams.

## To run the module
uv run python -m datafun.app

## Project Concepts
The project introduces several important ideas:

1. **Grain** - what one row of data represents.
2. **Columns** - the information available about each observation.
3. **Target** - something we might want to predict later.
4. **Feature** - information that might help predict the target.
5. **Rationale** - why we think a feature might be useful.

## Custom Narrative (Extracted from Output)

```text
--------------------------------------------------------
Analyst Data Description (and Possible Prediction Plan):
--------------------------------------------------------
    A row represents:           Number of cricket chirps per second at a given temperature
    A target we might predict:  Temperature_F
    A feature that might help:  Chirps_Per_Second
    Why the feature might help:
We might be able to predict the temperature based on the number of cricket chirps per second.
```

## Initial Results

![Scatter plot showing the selected feature and target](/Users/rebeccalorey/Documents/GitHub/datafun-01-foundations/docs/images/feature-target-scatter.png)

## Important Folders and Files

- **data/** - the CSV data file
- **docs/** - the project narrative and documentation
- **src/datafun/app.py** - the Python logic
- **zensical.toml** - documentation site config


## Success
The app is running successfully if you see...

```
===================================
END main() - Executed successfully!
===================================
```

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
