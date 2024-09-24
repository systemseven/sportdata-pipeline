from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_player_data():
    seasons = list(range(datetime.now().year - 5, datetime.now().year))

    print('>>> Getting Player IDs')
    data = nfl.import_ids()
    util.write_data_file(data, 'players.csv')

    print('>>> Getting Injury Data')
    data = nfl.import_injuries(seasons)
    util.write_data_file(data, 'injuries.csv')


    print('>>> Getting Official Data')
    data = nfl.import_officials(seasons)
    util.write_data_file(data, 'officials.csv')

    print('>>> Getting Weekly Roster Data')
    data = nfl.import_weekly_rosters(seasons)
    util.write_data_file(data, 'weekly_roster.csv')

    print('>>> Getting Season Roster Data')
    data = nfl.import_seasonal_rosters(seasons)
    util.write_data_file(data, 'seasonal_roster.csv')

if __name__=="__main__":
    get_nfl_player_data()