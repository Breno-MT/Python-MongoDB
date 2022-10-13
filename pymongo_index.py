from pymongo_get_database import get_database

dbname = get_database()

collection_name = dbname["user_1_items"]

category_index = collection_name.create_index("category")




