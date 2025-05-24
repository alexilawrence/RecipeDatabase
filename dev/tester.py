import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

mongClient = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(mongClient)
db = client.myDatabase

recipeColl = db.get_collection('recipes')
usersColl = db.get_collection('users')
recipes = list(recipeColl.find({"visibility":{"$eq":'public'}}))

users = {str(user['userID']): user["username"] for user in usersColl.find()}


for recipe in recipes:
    recipe["username"] = users.get(str(recipe['userID']))

print(recipes)