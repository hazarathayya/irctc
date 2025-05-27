from flask import request, jsonify
from .models import Booking, Train, User
from . import db
from .routes import api_blueprint

# Book a seat
@api_blueprint.route('/book', methods=['POST'])
@token_required
def book_seat():
    data = request.get_json()
    
    if not data.get('train_id'):
        return jsonify({'message': 'Missing train_id!'}), 400

    train = Train.query.get(data['train_id'])

    if not train:
        return jsonify({'message': 'Invalid train!'}), 404

    if train.available_seats <= 0:
        return jsonify({'message': 'No available seats!'}), 400

    new_booking = Booking(user_id=g.user['id'], train_id=train.id)
    db.session.add(new_booking)

    train.available_seats -= 1
    db.session.commit()

    return jsonify({'message': 'Seat booked successfully!'}), 201


# Get specific booking details
@api_blueprint.route('/booking/<int:booking_id>', methods=['GET'])
def get_booking_details(booking_id):
    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({'message': 'Booking not found!'}), 404

    booking_data = {
        'user_id': booking.user_id,
        'train_id': booking.train_id,
        'timestamp': booking.timestamp
    }

    return jsonify({'booking': booking_data}), 200
