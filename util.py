
def write_data_file(df, filename):
    filename = 'data/nfl/' + filename
    df.to_csv(filename)