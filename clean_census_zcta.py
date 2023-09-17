import pandas as pd
import numpy as np

def process_file(file_path):
    
    #read the csv file
    df = pd.read_parquet(file_path)

    # Update 'medincome' column: Replace negative values with null
    df['medhouseholdincome'] = df['medhouseholdincome'].apply(lambda x: np.NaN if x < 0 else x)

    # Save the updated DataFrame back to the CSV file
    df.to_parquet(file_path, index=False)


if __name__ == '__main__':
    
    for year in list(range(2009, 2019)):

        file__prefix = '/n/dominici_nsaph_l3/Lab/projects/analytic/census_acs5/'
        file_name = 'census_' + str(year)
        file_suffix = '.parquet'
        file_path = file__prefix + file_name + file_suffix

        process_file(file_path)

