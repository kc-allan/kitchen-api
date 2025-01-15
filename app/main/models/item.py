from app import db
from datetime import datetime


class Item(db.Model):
    """
    Model for an item in the kitchen.
    """
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    unit = db.Column(db.String(64), nullable=False)  # kg, g, l, ml etc.
    category = db.Column(db.String(64))  # fruit, vegetable, meat etc.
    location = db.Column(db.String(64))  # fridge, cabinet, store etc.
    expiry_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_json(self):
        """
        Return the item as a JSON object.
        - This approach on a big scale can be inefficient.
        - Therefore I usually use a base class with a to_json method, inherited by all other models.
		"""
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit,
            "category": self.category,
            "location": self.location,
            "expiry_date": self.expiry_date.strftime('%Y-%m-%d') if self.expiry_date else None,
            "notes": self.notes,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def __repr__(self):
        """
        Return a string representation of the item.
        """
        return f'<Item {self.name}>'
