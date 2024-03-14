# Project methods overview

## Data Sources
- CBI (Composite Burn Index)
- [LCMAP (Land Change Monitoring, Assessment, and Projection)](https://www.usgs.gov/special-topics/lcmap/data): Land cover information
- CU Boulder Disturbance Stack
- [CHELSA V1.2](https://chelsa-climate.org/downloads/): climate data
- [NASADEM](https://planetarycomputer.microsoft.com/dataset/nasadem) from Microsoft Planetary Computer for topographic data
## Data Processing Steps
Describe data processing steps taken, the order of scripts, etc.

## Data Analysis
We took our processed data and fit an XGBoost model with it (initially with default parameters), to get _ f1 score. Then, using the `shap` Python package, we plotted the shap values to visualize each feature's impact on the model output.

## Visualizations
Describe visualizations created and any specialized techniques or libraries that users should be aware of.

## Conclusions
Summary of the full workflow and its outcomes. Reflect on the methods used.

## References
Citations of tools, data sources, and other references used.
