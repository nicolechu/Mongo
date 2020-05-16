import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://nicolechu:zigpqXVEfNubZEEx@cpsc408-60p7w.gcp.mongodb.net/test?retryWrites=true&w=majority')

db = client.gettingStarted

people = db.people

import datetime
personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}

people.insert_one(personDocument)
