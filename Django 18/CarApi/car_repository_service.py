from http.client import HTTPException

from models import CarCreate, CarUpdate, CarRead, Car
from in_memory_data import _next_id, _lock, _store

def _create_car(payload: CarCreate) -> CarRead:
    global _next_id
    with _lock:
        cid = _next_id
        _next_id += 1
        car = CarRead(id=cid,**payload.model_dump())
        _store[cid] = car
        return car

def _get_car_by_id(cid:int) -> CarRead:
    car = _store.get(cid)
    if not car:
        raise HTTPException(404, "Car not found")
    return car

def _delete_car(cid:int) -> None:
    del _store[cid]


def _patch_car(cid:int, payload: CarUpdate) -> CarRead:
    car = _get_car_by_id(cid)
    data = car.model_dump()
    updates = payload.model_dump(exclude_unset=True)
    data.update(updates)
    updated = CarRead(**data)
    _store[cid] = updated
    return updated


def _replace_car(cid:int, payload: CarCreate) -> CarRead:
    current = _get_car_by_id(cid)
    car = CarRead(id=cid,**payload.model_dump())
    _store[cid] = car
    return car

