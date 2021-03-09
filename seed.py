"""Seed file to make sample data for adoption DB"""

from models import db, Pet
from app import app

# Re-create all tables
db.drop_all()
db.create_all()

# Clean up any data that somehow did not get dropped
Pet.query.delete()

# Add sample pets
p1 = Pet(name="Zaghlool", species="Cat", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWuzpPmAvM3i3gCdyPMDRnBHLpY2jt2GtnBg&usqp=CAU", age=8, notes="Due to his old age, zaghlool sometimes gets grumpy and bites", available=True)
p2 = Pet(name="Kiki", species="Dog", photo_url="https://www.rover.com/blog/wp-content/uploads/2020/06/Yorkshire-Terrier.jpg", age=5, notes="Kiki is blind in his left eye", available=True)
p3 = Pet(name="Goldie", species="Dog", photo_url="https://cdn.orvis.com/images/DBS_GoldRetriever_1280.jpg", age=2, notes="Goldie is the goodest of boyz ... It's too bad that he isn't available for adoption at the moment", available=False)

db.session.add_all([p1, p2, p3])
db.session.commit()