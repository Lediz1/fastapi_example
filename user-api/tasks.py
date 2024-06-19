import time

import requests
from celery import Celery
from crud import crud_add_prod, crud_delete_prod, crud_get_prod, crud_update_prod, crud_get_prods, crud_get_prod_name
from schemas import ProdIn, ProdOut
from typing import Dict
import datetime
from celery.result import AsyncResult
# from . import task

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",


    backend="sqla+postgresql://prod:password@database:5432/alpha",

)
app.conf.result_expires = 1


@app.task
def task_add_prod(prod: Dict):
    # url = "https://randomprod.me/api"
    # response = requests.get(f"{url}?results={count}").json()["results"]
    # time.sleep(delay)

    
    result = []
    prod_name = crud_get_prod_name(prod["name"])
    if not prod_name:
        prod = ProdIn(
            name=prod['name'],
            description=prod["description"],
            pricing=f'{prod["pricing"]}',
            availability=f'{prod["availability"]}',
            category=prod["category"],
            
        )
        crud_add_prod(prod)
        return {"data": prod}
    return {"status_code": "403",  "message": "prod already exists "}


@app.task
def task_get_prod(prod_id: int):
    prod = crud_get_prod(prod_id)
    if prod:
        return ProdOut(**prod.__dict__).dict()
    return {"message": "prod not found "}


@app.task
def task_delete_prod(prod_id: int):
    prod = crud_get_prod(prod_id)
    if prod:
        crud_delete_prod(prod_id)

        return {"message": "prod deleted"}
    return {"message": "prod not found "}


@app.task
def task_get_prods():
    prods = crud_get_prods()
    return {"data": prods}


@app.task
def task_update_prod(prod_id: int, prod: Dict):
    prod_exists = crud_get_prod(prod_id)
    if prod_exists:
        prod["pricing"]=f'{prod["pricing"]}',
        prod["availability"]=f'{prod["availability"]}',
        prod = crud_update_prod(prod_id, prod)
        return prod
    return {"message": "prod not found "}


@app.task
def task_get_id_status(task_id: int):
    task = AsyncResult(task_id)

    state = task.state
    result = task.result

    if state == "FAILURE":
        error = str(task.result)
        response = {
            "state": state,
            "error": error,
        }
    else:
        response = {
            "state": state,
            "result": result,



        }

    return response
