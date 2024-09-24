from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_team_data():
    seasons = list(range(datetime.now().year - util.years_back, datetime.now().year + 1))

    print('>>> Getting Team Data')
    team_desc = nfl.import_team_desc()
    util.write_data_file(team_desc, 'teams.csv')

    print('>>> Getting Depth Charts')
    for s in seasons:
        data = nfl.import_depth_charts([s])
        filename = str(s) + '_depth_charts.csv'
        util.write_data_file(data, filename)

if __name__=="__main__":
    get_nfl_team_data()