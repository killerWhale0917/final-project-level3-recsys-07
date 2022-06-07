from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional,Dict,List

from server.services.crud import *
from models.Rule_based.rule_based import *
from server.services.recomendation import *

app = FastAPI()

class Item(BaseModel):
    item_id: List[int]
    image_url: Optional[List]
    item_name: Optional[List]

class ItemIn(BaseModel):
    item_ids: List[int]

class ItemOut(BaseModel):
    item_ids: List[int]
    img_url: Optional[List]
    item_name: Optional[List]
    big_class: Optional[List]

class Tags(BaseModel):
    tag_list: List[str]

# TEST
@app.get("/")
def server_test():
    return {"server" : "test"}

# image url
@app.get('/item/image/{item_id}')
def read_images_url(item_id : int):
    return get_image_url(item_id)

# Item info id, name, img_url
@app.post('/items/info/', response_model=ItemOut)
async def read_item_info(item: ItemIn):
    return get_item_info(item.item_ids)

# recommendation from item_id
@app.get('/rule_base/recommendation/{item_id}')
def rule_base_recommendation(item_id : int):
    return get_rulebase_recommendation(item_id)

# lightGCN recommendation
@app.get('/lightGCN/recommendation/{item_id}')
def lightGCN_recommendation(item_id : int):
    return get_lightGCN_recommendation(item_id)

# TODO : MultiVAE recommendation
@app.get('/MultiVAE/recommendation/{item_id}')
def MultiVAE_recommendation(item_id : int):
    pass

# 아이템의 옷 이름 가져오기
@app.post('/items/names', response_model=Item)
async def read_clothes_name(item: Item):
    return get_clothes_name(item)

@app.get('/codi')
def read_codi(select_item: int, pick_item: int):
    return get_codi(select_item,pick_item)

@app.post('/codis/info', response_model=ItemOut)
def read_codi_info(itemIn:ItemIn):
    return get_codi_info(itemIn.item_ids)

# key word 검색
@app.post('/items')
def read_item_from_tag(tagIn : Tags):
    return get_item_from_tag(tagIn.tag_list)

# 태그 리스트 가져오기
@app.get("/tags")
def read_item_tags():
    return get_item_tags()

# TODO : 추천된 코디 클릭시 implicit feedback 저장

# TODO : 만족도 평가 받기