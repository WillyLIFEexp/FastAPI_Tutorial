from app.database_mongo import db
from bson import ObjectId
from datetime import datetime
from app.schemas.product import ProductCreate, ProductUpdate

def product_serializer(prod: dict) -> dict:
    """
    Convert a MongoDB document into a JSON-serializable dictionary.

    - MongoDB uses the key '_id' for the primary key.
    - This function converts '_id' to a string and renames it to 'id'.
    - It also removes the original '_id' field from the dictionary.
    """
    if prod:
        prod['id'] = str(prod["_id"])
        del prod['_id']
    return prod

async def create_product(prod: ProductCreate) -> dict:
    """
    Create a new product in the 'products' collection.

    Steps:
      1. Convert the Pydantic model (ProductCreate) to a dictionary.
      2. Add a 'created_at' field with the current UTC datetime.
      3. Insert the product data into the MongoDB collection.
      4. Retrieve the newly inserted document using its '_id'.
      5. Serialize the document to convert '_id' to 'id' and return it.
    """
    prod_data = prod.dict()
    prod_data['created_at'] = datetime.now()
    result = await db.products.insert_one(prod_data)
    new_prod = await db.products.find_one({"_id": result.inserted_id})
    return product_serializer(new_prod)

async def get_all_products(limit: int=100) -> list:
    """
    Retrieve all products from the 'products' collection.

    Steps:
      1. Query the collection for all documents.
      2. Convert the cursor to a list, with an optional limit.
      3. Serialize each product document for JSON compatibility.
    """
    product_cursor = db.products.find()
    prod_lst = await product_cursor.to_list(length=limit)
    return [product_serializer(prod_item) for prod_item in prod_lst]

async def get_product(prod_id: str) -> dict:
    """
    Retrieve a single product by its unique identifier.

    Steps:
      1. Convert the product_id (string) to a MongoDB ObjectId.
      2. Query the collection for a document with that '_id'.
      3. If found, serialize and return the document; otherwise, return None.
    """
    prod = await db.products.find_one({"_id": ObjectId(prod_id)})
    if prod:
        return product_serializer(prod)

    return None

async def update_product(prod_id: str, update_data: ProductUpdate) -> dict:
    """
    Update an existing product document with the provided data.

    Steps:
      1. Convert the update data from the Pydantic model to a dictionary.
      2. Remove any fields that are None (i.e., not provided in the update).
      3. Use an update operation to set the new values.
      4. Retrieve and return the updated document.
    """
    updated_prod_data = update_data.dict()
    updated_info = {k: v for k, v in updated_prod_data.items() if v is not None}
    if updated_info:
        await db.products.update_one({"_id": ObjectId(prod_id)}, {"$set": updated_info})
    return await get_product(prod_id)


async def delete_product(prod_id: str) -> dict:
    """
    Delete a product document by its id.

    Steps:
      1. Retrieve the product (so you can return its data after deletion).
      2. If the product exists, perform a deletion operation.
      3. Return the deleted product document (or None if not found).
    """
    prod_data = db.products.find_one({"_id": prod_id})
    if prod_data:
        await db.products.delete_one({'_id': prod_id})
    return prod_data

