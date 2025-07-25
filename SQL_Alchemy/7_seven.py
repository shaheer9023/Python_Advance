from sqlalchemy import select
from three import User,Address,engine
from sqlalchemy.orm import Session
session=Session(engine)


statement = select(User).where(User.name == "anas")
anas=session.scalars(statement).one()
anas.addresses.append(Address(email_address="anasshmad9023@gmail.com"))

session.commit()