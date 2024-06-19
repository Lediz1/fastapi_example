from database import db_context
# , es
from models import Prod
from schemas import ProdIn, ProdOut
from typing import Dict


def crud_add_prod(prod: ProdIn):
    db_prod = Prod(**prod.dict())

    with db_context() as db:
        db.add(db_prod)
        db.commit()
        db.refresh(db_prod)


def crud_get_prod(prod_id: int):
    with db_context() as db:
        prod = db.query(Prod).filter(Prod.id == prod_id).first()
    if prod:
        return ProdOut(**prod.__dict__)

        # query = {
        #     "query": {
        #         "bool": {
        #             "must": {
        #                 "term": {
        #                     "id": prod_id
        #                 }
        #             }
        #         }
        #     }
        # }

        # results = es.search(index="prod", body=query)
        # return results
    return prod


def crud_delete_prod(prod_id: int):
    with db_context() as db:
        db.query(Prod).filter(Prod.id == prod_id).delete()
        db.commit()
        return {"sucess": "prod deleted"}
    return None


def crud_get_prods():
    result = []
    with db_context() as db:
        prods = db.query(Prod).all()

        for prod in prods:
            result.append(prod)

    return result


def crud_update_prod(prod_id: int, prod: Dict):

    with db_context() as db:
        db.query(Prod).filter(
            Prod.id == prod_id).update(prod)

        db.commit()
    return prod


def crud_get_prod_name(prod_name: str):
    with db_context() as db:
        prod = db.query(Prod).filter(Prod.name == prod_name).first()
    return prod


def crud_error_message(message):
    return {"error": message}
