from app import app
from models import db, Bird

with app.app_context():
    db.drop_all()
    db.create_all()

    birds = [
        Bird(name="Eagle", species="Aquila"),
        Bird(name="Parrot", species="Psittaciformes"),
        Bird(name="Owl", species="Strigiformes")
    ]

    db.session.add_all(birds)
    db.session.commit()

    print("Seed complete")
