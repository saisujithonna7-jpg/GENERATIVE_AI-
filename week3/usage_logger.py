import os
import time
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError


class UsageLogger:
    def __init__(self):
        load_dotenv(Path(__file__).parent / ".env", override=True)
        mongo_uri = os.getenv("MONGODB_URI")
        if not mongo_uri or "<db_username>" in mongo_uri or "<cluster-address>" in mongo_uri:
            raise ValueError(
                "MONGODB_URI is not configured in week3/.env. "
                "Please replace <db_username>, <db_password>, and <cluster-address> "
                "with your MongoDB Atlas connection string."
            )

        self.client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=10000,
            retryWrites=True
        )

        # Check that MongoDB is reachable
        self.client.admin.command("ping")

        db = self.client["llm_monitoring"]
        self.collection = db["api_usage"]

    def log_call(self, record):
        # Work on a copy so the caller's dictionary is not changed
        document = dict(record)
        document["timestamp"] = datetime.now(timezone.utc)

        for attempt in range(3):
            try:
                self.collection.insert_one(document)
                print("Usage details saved to MongoDB.")
                return True
            except PyMongoError as error:
                print(f"MongoDB write attempt {attempt + 1} failed: {error}")
                if attempt < 2:
                    time.sleep(2 ** attempt)

        print("Warning: usage record could not be saved.")
        return False

    def close(self):
        self.client.close()
