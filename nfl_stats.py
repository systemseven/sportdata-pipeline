from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_player_data():
    seasons = list(range(datetime.now().year - 5, datetime.now().year))

    print('>>> Getting PBP Data')
    data = nfl.import_pbp_data(seasons)
    util.write_data_file(data, 'pbp_data.csv')

    print('>>> Getting NGS Data')
    for type in ['passing', 'rushing', 'receiving']:
        data = nfl.import_ngs_data(type, seasons)
        filename = type + '_ngs_data.csv'
        util.write_data_file(data, filename)

    print('>>> Getting QBR Data')
    data = nfl.import_qbr(seasons)
    util.write_data_file(data, 'qbr_data.csv')

    print('>>> Getting Seasonal PFR Data')
    for type in ['pass', 'rush', 'rec']:
        data = nfl.import_seasonal_pfr(type, seasons)
        filename = type + '_seasonal_pfr_data.csv'
        util.write_data_file(data, filename)

    print('>>> Getting Weekly PFR Data')
    for type in ['pass', 'rush', 'rec']:
        data = nfl.import_weekly_pfr(type, seasons)
        filename = type + '_weekly_pfr_data.csv'
        util.write_data_file(data, filename)


    print('>>> Getting Snap Count Data')
    data = nfl.import_snap_counts(seasons)
    util.write_data_file(data, 'snap_counts.csv')

    print('>>> Getting FTN Chart Data')
    seasons = list(range(2022, datetime.now().year))
    data = nfl.import_ftn_data(seasons)
    util.write_data_file(data, 'ftn_data.csv')

if __name__=="__main__":
    get_nfl_player_data()