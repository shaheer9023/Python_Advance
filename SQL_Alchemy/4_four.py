from three import *
from three import User,Address
from sqlalchemy.orm import Session

# with Session(engine) as session:
#     user1=User(
#         name="shaheer",
#         fullname="shaheer ahmad",
#         addresses=[Address(email_address="shaheerahmad9023@gmail.com")]
#     )
#     user2=User(
#         name="Hoorab",
#         fullname="Hoorab Zahra",
#         addresses=[
#             Address(email_address="hoorabzahra@gmail.com"),
#             Address(email_address="hoorabzahra9023@gmail.com"),
#             ]
#     )
#     user3=User(
#         name="Anas",
#         fullname="Anas Ahmad",

#     )
#     session.add_all([user1,user2,user3])
#     session.commit()    
