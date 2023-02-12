from fastapi import APIRouter, Depends, status
from .. import crud, schemas, dependencies
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    dependencies=[Depends(dependencies.get_db), Depends(dependencies.get_current_user)],
    responses={404: {"Description": "Not found"}}
)


@router.get("/", response_model=list[schemas.Item], status_code=status.HTTP_200_OK, tags=["Items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int, db: Session=Depends(dependencies.get_db)):
    item_delete = crud.delete_user_item(db, item_id)
    return item_delete

@router.patch("/{item_id}/update", status_code=status.HTTP_202_ACCEPTED, tags=["Items"])
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(dependencies.get_db)):
    crud.update_item(db=db, item_id=item_id, item=item)
    return {"message": "Updated"}