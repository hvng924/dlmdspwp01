from db.schemas.test import Test
import unittest

from sqlalchemy import engine
from db.connection_factory import SqliteFactory

from db.dao.test import TestDAO

class TestTestDAO(unittest.TestCase):
    dao = TestDAO(SqliteFactory)

    def test_save(self):
        entry = {
            'x': 1,
            'y': 2,
        }
        self.dao.save(entry)
        rows = self.dao.get_all()
        self.assertEqual(rows[0]['x'], entry['x'])
        self.assertEqual(rows[0]['y'], entry['y'])

if __name__ == '__main__':
    unittest.main()