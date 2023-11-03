@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()
