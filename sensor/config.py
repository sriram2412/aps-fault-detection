import pymongo
import json
import pandas as pd
from dataclasses import dataclass
#provide the mongodb localhost url to connect python to mongodb
import os
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


TARGET_COLUMN_MAPPING = {
    "pos":1,
    "neg":0
}

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"
