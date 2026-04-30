from typing import Dict
from models import *
from threading import Lock


_store: Dict[int, CarRead] = {}
_next_id = 1
_lock: Lock = Lock()

