from datetime import datetime
import nfl_data_py as nfl
import util


def get_nfl_player_data():
    seasons = list(range(datetime.now().year - 5, datetime.now().year + 1))

    print('>>> Getting Odds Data')
    data = nfl.import_win_totals()
    util.write_data_file(data, 'odds_wins.csv')

    data = nfl.import_sc_lines(seasons)
    util.write_data_file(data, 'odds_lines.csv')

if __name__=="__main__":
    get_nfl_player_data()