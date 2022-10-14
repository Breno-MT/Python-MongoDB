from pymongo_get_database import get_database
from pandas import DataFrame


dbname = get_database()

collection_name = dbname["user_1_items"]


# items_details = collection_name.find()
# items_details = collection_name.find({"category" : "food"}).sort("item_name",1) # find by name asc
# items_details = collection_name.find({"category" : "food"}).sort("item_name",-1) # find by name desc
# items_details = collection_name.find()

# items_df = DataFrame(items_details)

# print(items_df)

def search_by_category(name):
    names = collection_name.find({"category": {"$regex": f"{name}"}})
    names_df = DataFrame(names)

    if names:
        print(names_df)

search_by_category('fo2')

