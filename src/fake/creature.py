from model.creature import Creature
from error import Missing, Duplicate

fakes = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             description="Hirsute Himalayan",
             country="CN",
             area="Himalayas"),
    Creature(name="Bigfoot",
             aka="Sasquatch",
             description="New world Cousin Eddie of the yeti",
             country="US",
             area="*"),
    ]

def find(name: str) -> Creature | None:
    for c in fakes:
        if c.name == name:
            return c
    return None

def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing creature {name}")
    
def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate creature {name}")

def get_all() -> list[Creature]:
    """Return all creatures"""
    return fakes

def get_one(name: str) -> Creature:
    """Return one creature"""
    check_missing(name)
    return find(name)

# The following are non-functional for now,
# so they just act like they work, without modifying
# the actual fakes list:
def create(creature: Creature) -> Creature:
    """Add a creature"""
    check_duplicate(creature.name)
    return creature

def modify(name: str, creature: Creature) -> Creature:
    """Partially modify a creature"""
    check_missing(creature.name)
    return creature

def delete(name: str) -> None:
    """Delete a creature"""
    check_missing(name)
    return None
