
years_back = 5

def write_data_file(df, filename):
    filename = 'data/nfl/' + filename
    df.to_csv(filename, compression='gzip')