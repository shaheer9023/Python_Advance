from sqlalchemy import create_engine, text

# Create engine
engine = create_engine("mysql+pymysql://root:4414@127.0.0.1:3306/mydb",echo=True)

# Connect and execute SQL statements
with engine.connect() as connect:
    # Create table if not exists
    # connect.execute(text("CREATE TABLE IF NOT EXISTS table2 (id INT, age INT)"))

    # Insert a row
    # connect.execute(text("INSERT INTO table2 (id, age) VALUES (2, 22),(3,23)"))

    # Commit the transaction (only needed in some cases)
    connect.commit()
