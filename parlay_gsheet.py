'''
This script will pull seasonal data and convert it into a data frame
This dataframe will populate a google sheet that can be used to
build out parlay data and metrics
'''

import nfl_data_py as nfl
import numpy as np

import util


def parlay():
    season = 2024

    season_df = nfl.import_seasonal_data([season])
    season_df = season_df.rename(columns={'player_id': 'gsis_id'})

    players_df = nfl.import_players()

    players_df = players_df[['gsis_id', 'first_name', 'last_name', 'position', 'team_abbr']]
    stat_columns = ['first_name', 'last_name', 'position', 'team_abbr', 'completions', 'attempts', 'carries', 'passing_yards', 'passing_tds', 'rushing_yards', 'interceptions',  'receptions', 'targets', 'receiving_yards', 'receiving_tds', 'games', ]
    stats_df = players_df.merge(season_df, on=['gsis_id'])

    stats_df = stats_df[stat_columns]

    # if I can get position - set the below fields conditionally - that should have them be null for other rows

    season_tds = stats_df['passing_tds'] + stats_df['receiving_tds']
    stats_df['td_pg'] = round(season_tds / stats_df['games'], 1)

    stats_df['pass_yards_pg'] = round(stats_df['passing_yards'] / stats_df['games'], 1)
    stats_df['pass_attempts_pg'] = round(stats_df['attempts'] / stats_df['games'], 1)
    stats_df['pass_completions_pg'] = round(stats_df['completions'] / stats_df['games'], 1)
    stats_df['interceptions_pg'] = round(stats_df['interceptions'] / stats_df['games'], 1)

    stats_df['rush_yards_pg'] = round(stats_df['rushing_yards'] / stats_df['games'], 1)
    stats_df['rush_attempt_pg'] = round(stats_df['carries'] / stats_df['games'], 1)

    stats_df['rec_yards_pg'] = round(stats_df['receiving_yards'] / stats_df['games'], 1)
    stats_df['receptions_pg'] = round(stats_df['receptions'] / stats_df['games'], 1)
    stats_df['pass_attempt_pg'] = round(stats_df['targets'] / stats_df['games'], 1)

    util.write_data_file(stats_df, 'parlay_data.csv')


if __name__=="__main__":
    parlay()