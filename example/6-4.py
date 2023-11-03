from fastapi import Depends, APIRouter

def depfunc():
    pass

router = APIRouter(..., dependencies=[Depends(depfunc)])
