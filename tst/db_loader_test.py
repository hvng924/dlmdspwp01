from sqlalchemy.sql.expression import column
from csv_loader import load_csv
from pandas.core import frame
from db.dao.test import TestDAO
from db.connection_factory import SqliteMemoryFactory
import unittest
from db_loader import load_csv_to_db

class TestDBLoader(unittest.TestCase):
    def test_db_loader(self):
        load_csv_to_db(SqliteMemoryFactory)
        dao = TestDAO(SqliteMemoryFactory)
        imported_data = dao.get_all()
        frame = load_csv('test.csv')
        columns = list(frame.columns)
        
        for idx, row in frame.iterrows():
            data = imported_data[idx]

            for c in columns:
                self.assertEqual(data[c], row[c])