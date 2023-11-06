from .init import curs

def get_word() -> str:
    qry = "select name from creature order by random() limit 1"
    curs.execute(qry)
    row = curs.fetchone()
    if row:
        print(f"{row=}")
        name = row[0]
    else:
        name = "bigfoot"
    return name
