'''
Docstring for push_data

dotenv is used to load data from.env where we have our mongoDB
certi makes sure that whenver mongodb is being called it is by a certified authority

when we are converting it to json it should be in key value pairs, like dictionary
I will take the data transpose it and then to_json and then to values, arrays of json
and then finally convert it to list, then return this list.

for mongodb i want the records i want to insert, the database, and the collection it is like table in dbms


'''

import os
import sys
import json
import certifi
import pymongo

import pandas as pd
import numpy as np

from Network_Security import logger
from Network_Security.exception.exception import NetworkSecurityException

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")
print(MONGO_DB_URL)

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True , inplace=True)
            # Converting the df into a list of json values to store in mongodb
            #records = list(json.load(df.T.to_json()).values())
            
            records = df.to_dict(orient='records')
            return records
            
        except Exception as e:
                raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self , records , database , collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "Rishabh0120"
    collection = "NetworkData"

    network_obj = NetworkDataExtract()
    
    records = network_obj.csv_to_json(FILE_PATH)

    no_of_records = network_obj.insert_data_to_mongodb(records , DATABASE , collection)

    print(no_of_records)