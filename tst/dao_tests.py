from db.dao.ideal import IdealDAO
from db.dao.train import TrainDAO
from db.schemas.test import Test
import unittest

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

class TestTrainDAO(unittest.TestCase):
    dao = TrainDAO(SqliteFactory)

    def test_save(self):
        entry = {
            'x': 1,
            'y1': 2,
            'y2': 3,
            'y3': 4,
            'y4': 5,
        }
        self.dao.save(entry)
        rows = self.dao.get_all()
        self.assertEqual(rows[0]['x'], entry['x'])
        self.assertEqual(rows[0]['y1'], entry['y1'])
        self.assertEqual(rows[0]['y2'], entry['y2'])
        self.assertEqual(rows[0]['y3'], entry['y3'])
        self.assertEqual(rows[0]['y4'], entry['y4'])

class TestIealDAO(unittest.TestCase):
    dao = IdealDAO(SqliteFactory)

    def test_save(self):
        entry = {'x': 1}

        for i in range(1, 51):
            entry["y%d" % i] = i + 1

        self.dao.save(entry)
        rows = self.dao.get_all()
        self.assertEqual(rows[0]['x'], entry['x'])

        for i in range(1, 51):
            key = "y%d" % i
            self.assertEqual(rows[0][key], entry[key])

if __name__ == '__main__':
    unittest.main()