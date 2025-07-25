from sqlalchemy import select
from three import User,Address,engine
from sqlalchemy.orm import Session
session=Session(engine)
from rich import print


statement = (
    select(Address,User)
    .join(Address.user)
    .where(User.name == "hooRab")
    .where(Address.email_address == "hoorabzahra@gmail.com")
)
user=session.scalars(statement).all()
print(user)