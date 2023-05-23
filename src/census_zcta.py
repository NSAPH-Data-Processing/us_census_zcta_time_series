import pandas as pd
import argarse

def get_census_zcta():
    pass

def main(args):
    # read in census yaml ----
    census = pd.read_yaml(args.census_yaml)
    
    # get census data for all zcta for each variables----

    # merge dataframes ----

    # write ouput ----
    df.set_index('zcta', inplace=True)

    output_file = f"{args.output_prefix}_{args.year}.parquet"
    if args.output_format == 'csv':
        df.to_csv(output_file)
    elif args.output_format == 'parquet':
        df.to_parquet(output_file)

if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Generate SQL queries for census data')
    parser.add_argument(
        '--year', type=int, help='Year of output', 
        default=2011)
    parser.add_argument(
        'census_yaml', type=str, help='YAML file with census data', 
        default='../data/intermediate/scratch/census.yaml')
    parser.add_argument(
        'output_format', type=str, help='Output format', choices=['csv', 'parquet'],
        default='parquet')
    parser.add_argument(
        '--output_prefix', type=str, help='Output file name prefix', 
        default='../data/intermediate/scratch/census')
    args = parser.parse_args()
    main(args)
