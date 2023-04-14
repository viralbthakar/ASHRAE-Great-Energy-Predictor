# ASHRAE-Great-Energy-Predictor

## Installation
Create and Setup new conda environment using following set of commands.
```bash
conda create -n asharae-energy python=3.10
conda activate asharae-energy
pip install -r requirements.txt
```

## Dataset Download
- Setup Kaggle API using [this guide](https://www.kaggle.com/docs/api).
- Run following set of commands to download the dataset.
```bash
mkdir data
cd data
kaggle competitions download -c ashrae-energy-prediction
unzip ashrae-energy-prediction.zip -d ./raw_data
```

## Dataset Description and Details [Reference](https://www.kaggle.com/competitions/ashrae-energy-prediction/data)
The assessment of energy efficiency improvements in buildings can be difficult due to the lack of a baseline for comparison. Counterfactual models are used to estimate the energy consumption of a building before and after retrofitting. By comparing the actual energy consumption of a retrofitted building with the modeled values of the original building, the savings from the retrofit can be calculated. More accurate counterfactual models could help improve market incentives and financing options for energy efficiency projects.

The competition being described challenges participants to build counterfactual models for four energy types using historical usage rates and observed weather data. The dataset provided includes three years of hourly meter readings from over one thousand buildings at various locations around the world. This competition aims to improve the accuracy of counterfactual modeling for energy efficiency assessments, which could have significant implications for promoting energy efficiency measures in buildings and supporting sustainable practices in the built environment.

### Files
#### train.csv
- `building_id` - Foreign key for the building metadata.
- `meter` - The meter id code. Read as `{0: electricity, 1: chilledwater, 2: steam, 3: hotwater}`. Not every building has all meter types.
- `timestamp` - When the measurement was taken
- `meter_reading` - The target variable. Energy consumption in kWh (or equivalent). Note that this is real data with measurement error, which we expect will impose a baseline level of modeling error. UPDATE: as discussed here, the site 0 electric meter readings are in kBTU.

#### building_meta.csv
- `site_id` - Foreign key for the weather files.
- `building_id` - Foreign key for training.csv
- `primary_use` - Indicator of the primary category of activities for the building based on EnergyStar property type definitions
- `square_feet` - Gross floor area of the building
- `year_built` - Year building was opened
- `floor_count` - Number of floors of the building

#### weather_[train/test].csv
Weather data from a meteorological station as close as possible to the site.

- `site_id`
- `air_temperature` - Degrees Celsius
- `cloud_coverage` - Portion of the sky covered in clouds, in oktas
- `dew_temperature` - Degrees Celsius
- `precip_depth_1_hr` - Millimeters
- `sea_level_pressure` - Millibar/hectopascals
- `wind_direction` - Compass direction (0-360)
- `wind_speed` - Meters per second

#### test.csv
The submission files use row numbers for ID codes in order to save space on the file uploads. test.csv has no feature data; it exists so you can get your predictions into the correct order.

- `row_id` - Row id for your submission file
- `building_id` - Building id code
- `meter` - The meter id code
- `timestamp` - Timestamps for the test data period

#### sample_submission.csv
A valid sample submission.

- All floats in the solution file were truncated to four decimal places; we recommend you do the same to save space on your file upload.
- There are gaps in some of the meter readings for both the train and test sets. Gaps in the test set are not revealed or scored.