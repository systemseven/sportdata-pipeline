from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_player_data():
    seasons = list(range(datetime.now().year - util.years_back, datetime.now().year + 1))

    print('>>> Getting PBP Data')
    for s in seasons:
        data = nfl.import_pbp_data([s])
        filename = str(s) + '_pbp_data.csv'
        util.write_data_file(data, filename)

    print('>>> Getting NGS Data')
    for type in ['passing', 'rushing', 'receiving']:
        for s in seasons:
            data = nfl.import_ngs_data(type, [s])
            filename = str(s) + '_ngs_data.csv'
            util.write_data_file(data, filename)

    print('>>> Getting QBR Data')
    for s in seasons:
        data = nfl.import_qbr([s])
        filename = str(s) + '_qbr_data.csv'
        util.write_data_file(data, filename)

    print('>>> Getting Seasonal PFR Data')
    for type in ['pass', 'rush', 'rec']:
        for s in seasons:
            data = nfl.import_seasonal_pfr(type, [s])
            filename = str(s) + '_seasonal_pfr.csv'
            util.write_data_file(data, filename)

    print('>>> (skip) Getting Weekly PFR Data')
    for type in ['pass', 'rush', 'rec']:
        for s in seasons:
            data = nfl.import_weekly_pfr(type, [s])
            filename = str(s) + '_weekly_pfr.csv'
            util.write_data_file(data, filename)

    print('>>> Getting Weekly Data')
    for s in seasons:
        data = nfl.import_weekly_data([s])
        filename = str(s) + '_weekly_data.csv'
        util.write_data_file(data, filename)

    print('>>> Getting Seasonal Data')
    for s in seasons:
        data = nfl.import_weekly_data([s])
        filename = str(s) + '_seasonal_data.csv'
        util.write_data_file(data, filename)

    print('>>> Getting Snap Count Data')
    for s in seasons:
        data = nfl.import_snap_counts([s])
        filename = str(s) + '_snap_counts.csv'
        util.write_data_file(data, filename)

    print('>>> Getting FTN Chart Data')
    seasons = list(range(2022, datetime.now().year))
    for s in seasons:
        data = nfl.import_ftn_data([s])
        filename = str(s) + '_ftn_data.csv'
        util.write_data_file(data, filename)


if __name__=="__main__":
    get_nfl_player_data()