import pymongo
from bson import ObjectId
import json

# Set up the connection string
connection_string = "mongodb+srv://StDB:lrJKqTsc8nNSgoIP@cluster0.izid3.mongodb.net/?retryWrites=true&w=majority"


def dbConnect():
    try:
        # Connect to the MongoDB server
        client = pymongo.MongoClient(connection_string)
        # Check if the connection was successful
        if client:
            print("Connected successfully to MongoDB Atlas!")
            return client
        

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB Atlas: %s" % e)

    except pymongo.errors.OperationFailure as e:
        print("Error inserting/updating document: %s" % e)


def get_items_category(client, categoryNo):
    result_array = [] 
    image_urls = []  # create an empty list
    try:
        # Select a database
        db = client["supermarket"]
        # Select a collectiona
        collection = db["itemList"]
        
        # Find documents in the collection with ItemCategory of categoryNo
        documents = collection.find({"ItemCategory": categoryNo})
        
        # Print the retrieved documents
        for document in documents:
            result_array.append(document)
             
        # for item in result_array:
        #     getItem = item["ImageUrl"]
        #     image_urls.append(getItem)  # extract "ImageUrl" and add to list
            
        print("Added to Array")
    except Exception as e:
        print("Error: ", str(e))
    
    return result_array



def ItemList(CategoryNo):
    try:
        # connect to database
        client = dbConnect()

        # get list of items for the given category
        imageList = get_items_category(client, CategoryNo)
        # Function to convert ObjectId to string
        def convert(o):
            if isinstance(o, ObjectId):
                return str(o)
            return o

        # Serialize the dictionary to JSON
        json_data = json.dumps(imageList, default=convert)
        print(json_data)
        return json_data
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

ItemList(1)

# client=dbConnect()
# addOrUpdateData(client)

def get_items_category_image(client, categoryNo):
    result_array = [] 
    image_urls = []  # create an empty list
    try:
        # Select a database
        db = client["supermarket"]
        # Select a collection
        collection = db["itemList"]
        
        # Find documents in the collection with ItemCategory of categoryNo
        documents = collection.find({"ItemCategory": categoryNo})
        
        # Print the retrieved documents
        for document in documents:
            result_array.append(document)
             
        for item in result_array:
            getItem = item["ImageUrl"]
            image_urls.append(getItem)  # extract "ImageUrl" and add to list
            
        print("Added to Array")
    except Exception as e:
        print("Error: ", str(e))
    
    return image_urls


def ItemList_image(CategoryNo):
    try:
        # connect to database
        client = dbConnect()

        # get list of items for the given category
        imageList = get_items_category_image(client, CategoryNo)
        # Function to convert ObjectId to string
        def convert(o):
            if isinstance(o, ObjectId):
                return str(o)
            return o

        # Serialize the dictionary to JSON
        json_data = json.dumps(imageList, default=convert)
        print(type(json_data))
        # print(json_data)
        return json_data
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    
# ItemList_image(3)