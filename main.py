from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
  alexnet = 'alexnet'
  resnet = 'resnet'
  lenet = 'lenet'

class MyNames(str, Enum):
  Trish = 'Trish'
  Testimony = 'Testimony'
  Zoe = 'Zoe'
  Patricia = 'Patricia'
  Asiimire = 'Asiimire'


app = FastAPI()

@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
  if model_name is ModelName.alextnet:
    return {'model_name': model_name, 'message': 'Deep learning FTW!'}
  if model_name.value == 'lenet':
    return {'model_name': model_name, 'message': 'LeCNN all the images'}
  return {'model_name': model_name, 'message': 'Have some residuals'}

@app.get('/my_names/{name}')
async def get_name(name: MyNames):
  if name is ModelName.Trish:
    return {'name': name, 'message': 'That\'s my name at MUK'}
  if name.value == 'Zoe' """MyNames.name.value""":
    return {'name': name, 'message': 'That\'s for A level'}
  return {'name':name, 'message':'That\'s also my name!'}

@app.get('/')
async def root():
  return {"message":"Hello world"}

#path parameters
@app.get('/items/{item_id}')
async def read_item(item_id:int):
  return {'item_id':item_id}

@app.get('/users/me')
async def read_user_me():
  return {'user_id':'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id:str):
  return {'user_id':user_id}

@app.get('/users')
async def read_users():
  return ['Rich','Friend']

@app.get('/users')
async def read_users2():
  return ['Bean', 'English']