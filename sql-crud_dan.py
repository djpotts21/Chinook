from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# exceting the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    place_name = Column(String)
    place_county = Column(String)
    why_liked = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sesionmaker, then point our engine (the db)
Session = sessionmaker(db)


# opens a action session by calling the Session() subclass defined above
session = Session()


# creating the database using declarative_base subsclass
base.metadata.create_all(db)


# creating records on our Programmer table
bedlington = Places(
    place_name="ABC",
    place_county="UK",
    why_liked="World's best programmer live here",
)


# add each instance of our programmers to our session
# session.add(bedlington)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(daniel_potts)


# upding a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
ID = input("Enter record ID: ")
place = session.query(Places).filter_by(
    id=ID
    ).first()
# defensive programming
if place is not None:
    print(
        "Place: ",
        place.place_name
    )
    confirmation = input(
      "Are you sure you want to delete this record? (y/n)"
      )
    if confirmation.lower() == "y":
        session.delete(place)
        session.commit()
        print("Place has been deleted")
    else:
        print("Place not deleted")
else:
    print("No records found!")

# commit our session to the database
session.commit()


# query the database to find all Programmers
places = session.query(Places)
for place in places:
    print(
        place.id,
        place.place_name,
        place.place_county,
        place.why_liked,
        sep=" | "
        )
