from db.connection_factory import AbstractFactory, SqliteMemoryFactory
from sqlalchemy.sql.expression import column
from db.dao.ideal import IdealDAO
import os
from db.dao.test import TestDAO
from db.dao.ideal import IdealDAO
from db.dao.train import TrainDAO
from csv_loader import load_csv
DATA_DIR = 'data'
FILE_TO_DAO = {
    'test.csv': TestDAO,
    'ideal.csv': IdealDAO,
    'train.csv': TrainDAO,
}

def load_csv_to_db(factory: AbstractFactory):
    files = [ f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f)) ]
    
    for f in files:
        dao = FILE_TO_DAO[f](factory)
        frame = load_csv(f)
        columns = list(frame.columns)
        
        for _, row in frame.iterrows():
            data = {}
            
            for c in columns:
                data[c] = row[c]
            
            dao.save(data)

if __name__ == '__main__':
    load_csv_to_db(SqliteMemoryFactory)