import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://nicolechu:zigpqXVEfNubZEEx@cpsc408-60p7w.gcp.mongodb.net/test?retryWrites=true&w=majority')

db = client.cpsc408

student = db.Student

# insert new documents
student.insert_one({ "FirstName": "Alex",
                     "LastName": "Jones",
                     "Major": ["CPSC", "BIO"],
                     "Courses": [ "CPSC 350", "CPSC 408", "MATH 350"] })

# select document w/ criteria
for s in student.find({"Major" : "CPSC"}):
    print(s["FirstName"])

# select document
for s in student.find():
    print(s)

print(client.list_database_names())