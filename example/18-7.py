from .init import curs

def get_word() -> str:
    qry = "select name from creature order by random() limit 1"
    curs.execute(qry)
    rows = curs.fetchall()
    name = rows[0]
    return name
