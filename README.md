
## Table of Contents: 

- [Introduction](#introduction)
- [Data Description](#data-description)
- [Codebook](#codebook)
- [Data Quality](#data-quality)
- [Repository Content](#repository-content)
- [Data Lineage](#data-lineage)
- [Processing Rules](#installation)
- [Run](#run)

## Introduction
The project streamines the extraction and analysis of demographic data from the  American Community Survey 5-Year Data (ACS5). The project aims to provide cleaned data for each year from 2009-2019 for the required variables.

**Notes about American Community Survey 5-Year Data:**

- The American Community Survey (ACS) is an ongoing survey that provides data every year -- giving communities the current information they need to plan investments and services. The ACS covers a broad range of topics about social, economic, demographic, and housing characteristics of the U.S. population.

- ACS data is available from 2009 onwards; however, ZCTA (ZIP Code Tabulation Area) level information is available from 2011 onwards.

- The ACS is an ongoing survey that collects responses every day of the year. The ACS estimates do not represent a specific point in time during the collection period, but rather a pooling of the data collected during the entire period. For 1-year estimates, the ACS uses data collected in that calendar year — January 1 through December 31. Similarly, the 5-year estimates use data collected over a 5-year period. For example, the 2016-2020 5-year estimates will use ACS data collected from January 1, 2016, through December 31, 2020. Read further about the period estimates [here.](https://www.census.gov/newsroom/blogs/random-samplings/2022/03/period-estimates-american-community-survey.html) 


## Data Description 

- **Time Coverage** : 2009 - 2019
- **ZCTA Coverage**: 33120
- **Population**: All 50 states including the District of Columbia, Puerto Rico, and other U.S. territories.
- **Data Source**: The [American Community Survey (ACS)](https://www.census.gov/data/developers/data-sets/acs-5year.html) is an ongoing survey that provides data every year -- giving communities the current information they need to plan investments and services. The ACS covers a broad range of topics about social, economic, demographic, and housing characteristics of the U.S. population. 

## Codebook

| Variable Name | Description | Derivation |
|---|---| --- |
| pct_blk  | % of the population listed as black  | ```B02001_003E/B02001_001E``` <br> B02001_003E: Estimate!!Total!!Black or African American alone <br> B02001_001E: Estimate!!Total - Race |
| medhouseholdincome | median household income | `B19013_001E`  <br> B19013_001E: : Median Household Income In The Past 12 Months In 2011 Inflation-Adjusted Dollars |
| pct_owner_occ | % of housing units occupied by their owner  | `For Years 2009 - 2014: (B11012_004E + B11012_008E + B11012_011E + B11012_014E)/ B11012_001E` <br> B11012_004E: Estimate!!Total!!Family households!!Married-couple family!!Owner-occupied housing units <br> B11012_008E: Estimate!!Total!!Family households!!Other family!!Male householder, no wife present!!Owner-occupied housing units <br> B11012_011E: Estimate!!Total!!Family households!!Other family!!Female householder, no husband present!!Owner-occupied housing units B11012_014E: Estimate!!Total!!Nonfamily households!!Owner-occupied housing units <br> B11012_001E: Estimate!!Total - HOUSEHOLD TYPE BY TENURE <br> `For Years 2015 - 2018: B25011_002E/B25011_001E` <br> B25011_002E: Estimate!!Total!!Owner occupied <br> B25011_001E: Estimate!!Total: TENURE BY HOUSEHOLD TYPE (INCLUDING LIVING ALONE) AND AGE OF HOUSEHOLDER|
| hispanic| % of the population identified as Hispanic, regardless of reported race  | `B03003_003E/B03003_001E` <br> B03003_003E: Estimate!!Total!!Hispanic or Latino <br> B03003_001E: Estimate!!Total |
| education | % of the population older than 65 not graduating from high school  | `(B15001_036E+B15001_037E+B15001_077E+B15001_078E)/(B15001_035E+B15001_076E)` <br> B15001_036E: Estimate!!Total!!Male!!65 years and over!!Less than 9th grade <br>  B15001_037E: Estimate!!Total!!Male!!65 years and over!!9th to 12th grade, no diploma <br> B15001_077E: Estimate!!Total!!Female!!65 years and over!!Less than 9th grade <br> B15001_078E: Estimate!!Total!!Female!!65 years and over!!9th to 12th grade, no diploma <br> B15001_035E: Estimate!!Total!!Male!!65 years and over <br> B15001_076E: Estimate!!Total!!Female!!65 years and over |


## Data Quality 

The below table provides a comprehensive overview of the missing values in the generated dataset. It contains a record of null values for each variable across different years. 

| variable_name      | total_zcta | 2011_null | 2012_null | 2013_null | 2014_null | 2015_null | 2016_null | 2017_null | 2018_null |
|--------------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| pct_blk            | 33120      | 369       | 337       | 336       | 306       | 310       | 321       | 317       | 321       |
| medhouseholdincome | 33120      | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| pct_owner_occ      | 33120      | 615       | 589       | 596       | 573       | 571       | 580       | 573       | 578       |
| hispanic           | 33120      | 369       | 337       | 336       | 306       | 310       | 321       | 317       | 321       |
| education          | 33120      | 1199      | 1138      | 1103      | 1034      | 1024      | 1011      | 1046      | 1019      |


## Repository Content

The repository contains: 

- [census_zcta.py](https://github.com/NSAPH-Data-Processing/census_acs5/blob/dev/census_zcta.py): The main script for querying Census API and generating final datasets.
- [requirements.yml](https://github.com/NSAPH-Data-Processing/census_acs5/blob/dev/requirements.yml): Environment setup file for result reproducibility.
- [notes/eda_output.ipynb](https://github.com/NSAPH-Data-Processing/census_acs5/blob/dev/notes/eda_output.ipynb): EDA notebook exploring dataset variables across years.

## Data Lineage

- **Data Source** :The primary data source for this project is the [American Community Survey 5-Year Data (ACS5)](https://www.census.gov/programs-surveys/acs/about.html), which is publicly available and maintained by U.S. Census Bureau. The ACS5 data provides a comprehensive snapshot of various demographic variables. 

- **Extraction** : We leverage a [Python wrapper](https://pypi.org/project/census/) to efficiently extract data from the US Census Bureau's API. This wrapper provides us with direct access to ACS and SF1 datasets, facilitating swift retrieval of the specific variables necessary for subsequent analysis and processing.

- **Processing & Final Dataset** : We transform the subset of variables obtained from the API and generate the final datasets for each respective year.

## Processing Rules

**Processing rules applied in census_zcta.py**

To align with the aggregated nature of ACS estimates over 5-year periods, a specific processing rule is employed within the project. Each dataset generated from ACS data is internally tagged to a year that is 2 years prior. This tagging ensures that the data extracted in a given year corresponds to the ACS data collected 2 years later, providing consistency with the 5-year estimates.

For instance, when extracting data for the year 2020 from the ACS, the data is tagged internally as ACS 2018. This alignment respects the fact that the 2020 5-year estimates encompass ACS data collected from January 1, 2016, through December 31, 2020. This approach enables accurate and meaningful analysis while considering the temporal aggregation inherent in ACS data reporting.


## Run

(I) **Clone the repository** 

Clone the repository

```bash
git clone <https://github.com/<user>/repo>
cd <repo>
```

(II) **Create Conda Environment**
Create conda environment using the requirements.yaml file

```bash
conda env create -f requirements.yml
conda activate <env_name> #environment name as found in requirements.yml
```

It is also possible to use `mamba`.

```bash
mamba env create -f requirements.yml
mamba activate <env_name>
```

(III) **Create entrypoints** 
Add symlinks to input, intermediate and output folders inside the corresponding `/data` subfolders.

For example:

```bash
export HOME_DIR=$(pwd)

cd $HOME_DIR/data/input/ .
ln -s <input_path> . #paths as found in data/input/README.md if any

cd $HOME_DIR/data/output/
ln -s <output_path> . #paths as found in data/output/README.md if any
```

The README.md files inside the `/data` subfolders contain path documentation for NSAPH internal purposes.

(IV) **Run pipeline** 

Run the script for all years:

```bash
python ./<main_script>.py --year <year>
```

or run the pipeline:

```bash
snakemake --cores
```


