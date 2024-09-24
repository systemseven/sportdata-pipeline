from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_player_data():
    seasons = list(range(datetime.now().year - 5, datetime.now().year + 1))

    print('>>> Getting Player IDs')
    data = nfl.import_ids()
    util.write_data_file(data, 'players.csv')

    print('>>> Getting Injury Data')
    for s in seasons:
        data = nfl.import_injuries([s])
        filename = str(s) + '_injuries.csv'
        util.write_data_file(data, filename)


    print('>>> Getting Official Data')
    for s in seasons:
        data = nfl.import_officials([s])
        filename = str(s) + '_injuries.csv'
        util.write_data_file(data, filename)

    print('>>> Getting Weekly Roster Data')
    for s in seasons:
        data = nfl.import_weekly_rosters([s])
        filename = str(s) + '_weekly_roster.csv'
        util.write_data_file(data, filename)

    print('>>> Getting Season Roster Data')
    for s in seasons:
        data = nfl.import_seasonal_rosters([s])
        filename = str(s) + '_seasonal_roster.csv'
        util.write_data_file(data, filename)

if __name__=="__main__":
    get_nfl_player_data()