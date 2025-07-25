
from three import User,  engine
from sqlalchemy.orm import Session

# Session create karein
session = Session(engine)

# Step 1: User ID 3 fetch karein
user = session.get(User, 3)

if user:
    # Step 2: Uske sabhi addresses delete karein
    for address in user.addresses:
        session.delete(address)

    # Step 3: Commit changes
    session.commit()
    print("Email address deleted successfully.")
else:
    print("User with ID 3 not found.")
