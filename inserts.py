from datetime import date

from base import Session, engine, Base
from actor import Actor
from contact_details import ContactDetails
from stuntman import Stuntman
from movie import Movie

# tells SQLAlchemy to create the database schema
Base.metadata.create_all(engine)

# creates a new session
session = Session()

# creates movies
bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie("Furious 7", date(2015, 4, 2))
no_pain_no_gain = Movie("No Pain No Gain", date(2013, 8, 23))

# creates actors
matt_damon = Actor("Matt Damon", date(1970, 10, 8))
dwayne_johnson = Actor("Dwayne Johnson", date(1972, 5, 2))
mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))

# add actors to movies
bourne_identity.actors = [matt_damon]
furious_7.actors = [dwayne_johnson]
no_pain_no_gain.actors = [dwayne_johnson, mark_wahlberg]

# add contact details to actors
matt_contact = ContactDetails("415 555 2671", "Burbank, CA", matt_damon)
dwayne_contact = ContactDetails("423 555 5623", "Glendale, CA", dwayne_johnson)
dwayne_contact_2 = ContactDetails("421 444 2323", "West Hollywood, CA", dwayne_johnson)
mark_contact = ContactDetails("421 333 9428", "Glendale, CA", mark_wahlberg)

# create stuntmen
matt_stuntman = Stuntman("John Doe", True, matt_damon)
dwayne_stuntman = Stuntman("John Roe", True, dwayne_johnson)
mark_stuntman = Stuntman("Richard Roe", True, mark_wahlberg)

# persists movie data in the database
session.add(bourne_identity)
session.add(furious_7)
session.add(no_pain_no_gain)

# persist contact details
session.add(matt_contact)
session.add(dwayne_contact)
session.add(dwayne_contact_2)
session.add(mark_contact)

# persist stuntmen
session.add(matt_stuntman)
session.add(dwayne_stuntman)
session.add(mark_stuntman)

# commit and close session
session.commit()
session.close()
