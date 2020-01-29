"""
This  program runs on JSON data filters and aggregate to get the user count by date.
command:

    python3.6 agrt_push_to_sql(input_location)

"""

import pandas as pd
import argparse
import sqlalchemy as db
from tabulate import tabulate
import glob,sys




def to_mysql_db(df,db):
    """
    this function connects to sql and pushes data to mysql
    :param dataframe:
    :return msg:
    """
    pass
def query_mysql(db):
    """
    this function connects to docker container mysql and queries users table
    :return:Tabular format data
    """
    pass

def connect_mysql(database=None):
    """
    this function connects to docker container mysql
    """
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--input_location', required=False, default='./input/')
    args = vars(parser.parse_args())
    filter_agrt_push_rec_mysql(args['input_location'])
