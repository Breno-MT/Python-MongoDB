from pymongo_get_database import get_database

dbname = get_database()


collection_name = dbname["user_1_items"]


item_1 = {
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance"
}

item_2 = {
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
}


collection_name.insert_many([item_1, item_2])
