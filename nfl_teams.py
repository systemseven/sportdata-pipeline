from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_team_data():
    seasons = list(range(datetime.now().year - util.years_back, datetime.now().year))

    print('>>> Getting Team Data')
    team_desc = nfl.import_team_desc()
    util.write_data_file(team_desc, 'teams.csv')

    print('>>> Getting Depth Charts')
    data = nfl.import_depth_charts(seasons)
    util.write_data_file(data, 'depth_charts.csv')

if __name__=="__main__":
    get_nfl_team_data()