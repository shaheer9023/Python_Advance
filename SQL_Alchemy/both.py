#  user or address donon ka data 
from sqlalchemy import select
from three import User, Address, engine
from sqlalchemy.orm import Session
from rich import print

session = Session(engine)

# Build query: join User + Address with filters
statement = (
    select(Address, User)
    .join(Address.user)
    .where(User.name == "hooRab")
    .where(Address.email_address == "hoorabzahra@gmail.com")
)

# Use .execute().all() to get both models
results = session.execute(statement).all()

# Print both user and address from each result
for address, user in results:
    print("[bold cyan]User:[/bold cyan]", user)
    print("[bold green]Address:[/bold green]", address)
