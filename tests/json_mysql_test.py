import os,unittest
from main.json_format_push_to_mysql import *

import pandas as pd

class TestStart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        raw_file = os.path.join(THIS_DIR, './resources/raw.csv')
        cls.raw_df = pd.read_csv(raw_file)
        user_engagent = os.path.join(THIS_DIR, './resources/user_engagent.csv')
        cls.user_engagent_df = pd.read_csv(user_engagent)
        explode = os.path.join(THIS_DIR, './resources/explode.csv')
        cls.explode_df = pd.read_csv(explode)
        normalize = os.path.join(THIS_DIR, './resources/normalize.csv')
        cls.normalize_df = pd.read_csv(normalize)
        user_filter = os.path.join(THIS_DIR, './resources/user_filter.csv')
        cls.user_filter_df = pd.read_csv(user_filter)
        agrt = os.path.join(THIS_DIR, './resources/agrt.csv')
        cls.agrt_df = pd.read_csv(agrt)


    def test_mysql_connection(self):
        result = connect_mysql()
        self.assertNotEqual(result,None,"mysql not configured or not up!")

    def test_mysql_table(self):
        engine = connect_mysql()
        result = engine.dialect.has_table(engine, 'users')
        self.assertTrue(result,"No table exist!")


    def test_mysql_to_sql_query(self):
        result = to_mysql_db(self.agrt_df,'test_db')
        self.assertTrue(result,"No table exist!")


if __name__ == '__main__':
    unittest.main()