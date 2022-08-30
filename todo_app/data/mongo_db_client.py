import datetime
from flask import current_app
import pymongo
from todo_app.data.item import Item
import todo_app.data.configs.logger_settings as logger
import os

class MongoDBClient:

    def __init__(self):
        self.client = pymongo.MongoClient(os.getenv('MONGO_CON_STRING'))
        self.db = self.client[os.getenv('MONGO_DB_NAME')]
        self.items = self.db.items

    def get_items(self):
        """
        Get all items from the Mongo DB.

        Returns:
            items: List of items' as dictionary.
        """
        items = list(self.items.find())
        cards = []
        for card in items:
            cards.append(Item(
                card['_id'],
                card['name'],
                card['description'] if 'description' in card else None,
                card['due'] if 'due' in card else None,
                card['dateLastActivity'] if 'dateLastActivity' in card else None,
                card['status']
                )
            )
        return cards

    def add_item(self, title):
        """
            Create an item as part of the To Do list.

        Args:
            title: title name.
        """
        item = {
            "name": title,
            "dateLastActivity": datetime.datetime.utcnow(),
            "status": "To Do"
        }   
        self.items.insert_one(item)        

    def update_document(self, item_id, field, value):
        """
        Update a document's field.

        Args:
            item_id: ID of the item.
            field: field to update.
            value: value to set for the field.
        """
        finditem = { "_id": item_id }
        newstatus = { "$set": { 
            field: value,
            "dateLastActivity": datetime.datetime.utcnow()
            } 
        }
        self.db.items.update_one(finditem, newstatus)
