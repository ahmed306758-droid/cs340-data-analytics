import os
# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = os.environ.get('MONGO_PASSWORD', '') 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
       # Complete this create method to implement the C in CRUD.

    def create(self, data):
        """
        Inserts a document into MongoDB.

        Returns:
            True if successful, False otherwise.
        """

        if data is not None:
            try:
                self.collection.insert_one(data)
                return True

            except Exception as e:
                print("Error inserting document:", e)
                return False

        else:
            return False


    # Create method to implement the R in CRUD.

    def read(self, data):
        """
        Reads documents from MongoDB collection.

        Returns:
            List of documents if successful.
            Empty list if unsuccessful.
        """

        if data is not None:
            try:
                results = self.collection.find(data)
                return list(results)

            except Exception as e:
                print("Error reading documents:", e)
                return []

        else:
            return []