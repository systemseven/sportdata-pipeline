from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_team_data():
    seasons = list(range(datetime.now().year - 5, datetime.now().year))

    print('>>> Getting Schedule Data')
    schedule = nfl.import_schedules(seasons)
    util.write_data_file(schedule, 'schedule.csv')

if __name__=="__main__":
    get_nfl_team_data()