from .init import (curs, IntegrityError)
from model.creature import Creature
from error import Missing, Duplicate

curs.execute("""create table if not exists creature(
                name text primary key,
                country text,
                area text,
                description text,
                aka text)""")

def row_to_model(row: tuple) -> Creature:
    name, country, area, description, aka = row
    return Creature(name=name,
        country=country,
        area=area,
        description=description,
        aka=aka)

def model_to_dict(creature: Creature) -> dict:
    return creature.dict()

def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Creature {name} not found")

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]
    
def get_random_name() -> str:
    qry = "select name from creature order by random() limit 1"
    curs.execute(qry)
    row = curs.fetchone()
    name = row[0]
    return name

def create(creature: Creature) -> Creature:
    qry = """insert into creature
        (name, country, area, description, aka)
        values
        (:name, :country, :area, :description, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
        return get_one(creature.name)
    except IntegrityError:
        raise Duplicate(msg=
            f"Creature {creature.name} already exists")

def modify(name: str, creature: Creature) -> Creature:
    qry = """update creature set
             name=:name,
             country=:country,
             area=:area,
             description=:description,
             aka=:aka
             where name=:orig_name"""
    params = model_to_dict(creature)
    params["orig_name"] = name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(msg=f"Creature {name} not found")

def delete(name: str):
    qry = "delete from creature where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")
