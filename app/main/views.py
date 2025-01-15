from flask import make_response, request
from app import db
from app.main.models import Item
from datetime import datetime

from . import main

@main.route('/')
def index():
    """
    Index route for the API.
    """
    return make_response({
        "message": "Welcome to the Kitchen Inventory API!",
    }, 200)


@main.route('/items')
def get_items():
    """
    Get all kitchen items in the database.
    """
    items = db.session.query(Item).all()
    if not items:
        return make_response({
            "message": "No items found in the database.",
        }, 404)
    return make_response({
        "message": "Here are all the kitchen items in the database.",
        "data": [item.to_json() for item in items]
    }, 200)


@main.route('/items/create', methods=['POST'])
def create_item():
    """
    Create a new kitchen item.
    """
    # Get the request data
    data = request.get_json()
    item = db.session.query(Item).filter_by(name=data.get('name')).first()
    if item:
        return make_response({
            "message": "Item with the name already exists.",
        }, 400)
    # Create item if it doesn't exist
    new_item = Item(
        name=data.get('name'),
        quantity=data.get('quantity'),
        unit=data.get('unit'),
        category=data.get('category'),
        location=data.get('location'),
        expiry_date=datetime.strptime(data.get('expiry_date'), '%Y-%m-%d'),
        notes=data.get('notes')
    )
    # Save the item to the database
    db.session.add(new_item)
    db.session.commit()
    if not new_item.id:
        return make_response({
            "message": "Failed to create item.",
        }, 400)
    return make_response({
        "message": "Item created successfully.",
    }, 201)


@main.route('/items/<int:id>')
def get_item_by_id(id):
    """
    Get a kitchen item by its id.
    """
    item = db.session.query(Item).filter_by(id=id).first()
    if not item:
        return make_response({
            "message": "Item not found.",
        }, 404)
    return make_response({
        "message": "Here is the kitchen item with the id.",
        "data": item.to_json()
    }, 200)


@main.route('/items/update/<int:id>', methods=['PUT'])
def update_item(id):
    """
    Update a kitchen item by its id.
    """
    data = request.get_json()
    item = db.session.query(Item).filter_by(id=id).first()
    if not item:
        return make_response({
            "message": "Item not found.",
        }, 404)

    # Update the item if it exists
    TO_BE_IGNORED = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if hasattr(item, key) and not key in TO_BE_IGNORED:
            setattr(item, key, value)
    db.session.commit()
    return make_response({
        "message": "Item updated successfully.",
        "data": item.to_json()
    }, 200)


@main.route('/items/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    """
    Delete a kitchen item by its id.
    """
    item = db.session.query(Item).filter_by(id=id).first()
    if not item:
        return make_response({
            "message": "Item not found.",
        }, 404)
    db.session.delete(item)
    db.session.commit()
    return make_response({
        "message": "Item deleted successfully.",
    }, 200)
