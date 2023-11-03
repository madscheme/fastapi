from .init import curs

def get_word() -> str:
    print("---data/game/get_word")
    qry = "select name from creature order by random() limit 1"
    curs.execute(qry)
    rows = curs.fetchall()
    if rows:
        print(f"{rows=}")
        name = rows[0][0]
    else:
        name = "bigfoot"
    return name
