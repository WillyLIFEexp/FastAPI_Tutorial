from fastapi import APIRouter, HTTPException
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.crud.product import create_product, get_all_products, get_product, update_product, delete_product


router = APIRouter(prefix="/products", tags=["Prod"])

@router.post("/", response_model=ProductResponse)
async def create_new_product(prod: ProductCreate):
    new_product = await create_product(prod)
    return new_product

@router.get('/', response_model=list[ProductResponse])
async def read_products():
    prod_info = await get_all_products()
    return prod_info

@router.get('/{prod_id}', response_model=ProductResponse)
async def read_product(prod_id: str):
    prod_info = await get_product(prod_id)
    if not prod_info:
        raise HTTPException(status_code=404, detail="Can't find the Product")
    return prod_info

@router.put("/{prod_id}", response_model=ProductResponse)
async def change_product(prod_id: str, update_prod: ProductUpdate):
    updated_prod = await update_product(prod_id, update_prod)
    if not update_prod:
        raise HTTPException(status_code=404, detail="Can't find the Product")
    return update_product

@router.delete('/{prod_id}', response_model=ProductResponse)
async def remove_product(prod_id: str):
    deleted_prod = await delete_product(prod_id)
    if not deleted_prod:
        raise HTTPException(status_code=404, detail="Can't find the Product")
    return deleted_prod
