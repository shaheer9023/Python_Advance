from four import Session, User, Address
from three import engine
from sqlalchemy import delete, text

session = Session(engine)

# Step 1: Delete address records (child table)
session.execute(delete(Address))

# Step 2: Delete user records (parent table)
session.execute(delete(User))

# Step 3: Reset auto-increment for both tables (use actual table names in MySQL)
session.execute(text("ALTER TABLE address AUTO_INCREMENT = 1"))
session.execute(text("ALTER TABLE user_account AUTO_INCREMENT = 1"))

session.commit()
session.close()

print("Users and addresses deleted. Auto-increment reset.")
