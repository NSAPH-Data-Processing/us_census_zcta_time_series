import pandas as pd
import argparse
import yaml
import pprint
from census import Census
from us import states
import numpy as np
import os

def get_census_zcta(var_name, var_entry, year):

    c = Census(args.api_key)
    if 'den' in var_entry:
        den_list = var_entry['den']
        num_list = var_entry['num']
        all_var_list = den_list + num_list
        data = c.acs5.get(all_var_list, {'for': 'zip code tabulation area:*', 'year': year})
        df = pd.DataFrame.from_records(data) 
        df[var_name] = df[num_list].sum(axis=1) / df[den_list].sum(axis=1)
    else:
        num_list = var_entry['num']
        all_var_list = num_list
        data = c.acs5.get(all_var_list, {'for': 'zip code tabulation area:*', 'year': year})
        df = pd.DataFrame.from_records(data)  
        df[var_name] = df[num_list].sum(axis=1)
        
    df.rename(columns={'zip code tabulation area':'zcta'}, inplace = True)
    col_list = ['zcta', var_name]
    df = df[col_list]
    df.set_index('zcta', inplace=True)
    return df

def main(args):
    # read in census yaml ----
    with open(args.census_yaml) as file:
        census_doc = yaml.safe_load(file)
    
    df_list = []
    
    # get census data for all zcta for each variables----
    for variable in census_doc.keys():
        var_entry = census_doc[variable][args.year]
        df_var = get_census_zcta(variable, var_entry, args.year)
        df_list.append(df_var)

    # merge dataframes ----
    df = pd.concat(df_list, axis=1)
    df.reset_index(inplace=True)

    # write ouput ----

    output_file = f"{args.output_prefix}_{args.year}"
    if args.output_format == 'csv':
        output_file = output_file + '.csv'
        df.to_csv(output_file, index=False)
    elif args.output_format == 'parquet':
        output_file = output_file + '.parquet'
        df.to_parquet(output_file, index=False)

if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Generate SQL queries for census data')
    parser.add_argument(
        '--year', type=int, help='Year of output', 
        default=2011)
    parser.add_argument(
        '--census_yaml', type=str, help='YAML file with census data', 
        default='../data/input/remote/census.yaml')
    parser.add_argument(
        '--output_format', type=str, help='Output format', choices=['csv', 'parquet'],
        default='parquet')
    parser.add_argument(
        '--output_prefix', type=str, help='Output file name prefix', 
        default='../data/intermediate/scratch/census')
    parser.add_argument('--api_key', type=str, default=os.environ['API_KEY'])
    args = parser.parse_args()
    main(args)
