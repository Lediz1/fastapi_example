from celery.result import AsyncResult
from database import engine
# , es
from fastapi import FastAPI
from models import Base
from tasks import task_add_prod, task_delete_prod, task_get_prod, task_update_prod, task_get_prods, task_get_id_status
from schemas import ProdIn, Message,ProdDict


Base.metadata.create_all(bind=engine)

# index_name = 'prod'
# index_exists = es.indices.exists(index=index_name)
# if not index_exists:
#     es.indices.create(index=index_name, body=mapping)

app = FastAPI()


@app.post("/prods", status_code=201, #response_model=Message
          )
def add_prod(prod: ProdDict):
    """
    Add a prod to database using Celery. Uses Redis as Broker
    and Postgres as Backend.
    """

  
    task = task_add_prod.delay(prod.dict())
    out = task.get()

    return {"tag": task.id}


@app.get("/prods/{prod_id}", status_code=200, response_model=Message)
def get_prod(prod_id: int):
    """
    Get prod from database.
    """
    task = task_get_prod.delay(prod_id)
    return {"tag": task.id}


@app.delete("/prods/{prod_id}", status_code=200, response_model=Message)
def delete_prod(prod_id: int):
    """
    Erase a prod data from postgresql using Celery. 
    """
    task = task_delete_prod.delay(prod_id)
    return {"tag": task.id}


@app.get("/prods", status_code=201)
def get_prods():
    """
    Get all prods from database.
    """

    task = task_get_prods()
    return task


@app.put("/prods/{prod_id}", status_code=201, response_model=Message)
def update_prod(prod_id: int, prod: ProdDict):
    """
    Update a prod database.
    """

    task = task_update_prod.delay(prod_id, prod.dict())
    return {"tag": task.id}


@app.get("/tasks/{task_id}")
def task_status(task_id: str):
    """
    Get task status.
    PENDING (waiting for execution or unknown task id)
    STARTED (task has been started)
    SUCCESS (task executed successfully)
    FAILURE (task execution resulted in exception)
    RETRY (task is being retried)
    REVOKED (task has been revoked)
    """
    # task = AsyncResult(task_id)
    # state = task.state
    # result = task.result

    # if state == "FAILURE":
    #     error = str(task.result)
    #     response = {
    #         "state": state,
    #         "error": error,
    #     }
    # else:
    #     response = {
    #         "state": state,
    #         "data": result,

    #     }

    response = task_get_id_status(task_id)
    return response
