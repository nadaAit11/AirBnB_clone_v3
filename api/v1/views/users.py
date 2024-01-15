# api/v1/views/users.py
from flask import jsonify, request, abort
from . import app_views
from models.user import User  # Import your User model
from models import storage

def to_dict(user):
    """Converts a User instance to a dictionary."""
    return {
        'id': user.id,
        'email': user.email,
        'password': user.password,  # Note: This is just an example; handle password securely in your application
        'first_name': user.first_name,
        'last_name': user.last_name,
        'created_at': user.created_at.isoformat(),
        'updated_at': user.updated_at.isoformat(),
        # Add more fields as needed
    }

@app_views.route('/users', methods=['GET'])
def get_users():
    users = storage.all(User).values()
    return jsonify([to_dict(user) for user in users])

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(to_dict(user))

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@app_views.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')

    user = User(**data)
    user.save()

    return jsonify(to_dict(user)), 201

@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')

    # Update user with all key-value pairs from data, ignoring specified keys
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)

    user.save()

    return jsonify(to_dict(user)), 200
