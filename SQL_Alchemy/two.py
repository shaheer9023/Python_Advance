from one import engine,text

# with engine.connect() as connect:
#     result=connect.execute(text("select id,age from table1"))
#     for id,age in result:
#         print(f"id : {id} === age : {age}")


with engine.connect() as connect:
    connect.execute(text("UPDATE table2 SET id = 100 WHERE id = 3"))
    connect.commit()
