from four import Session,User
from three import engine
from sqlalchemy import select
from rich import print
session=Session(engine)
statement=select(User).where(User.id.in_([1,3]))
for user in session.scalars(statement):
    print(user)


