from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_team_data():
    seasons = list(range(datetime.now().year - util.years_back, datetime.now().year + 1))

    print('>>> Getting Schedule Data')
    for s in seasons:
        data = nfl.import_schedules([s])
        filename = str(s) + '_schedule.csv'
        util.write_data_file(data, filename)

if __name__=="__main__":
    get_nfl_team_data()