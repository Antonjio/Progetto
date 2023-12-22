import os
import sqlite3
from flask import Blueprint, g, render_template, request, redirect, session, make_response, jsonify
import stripe
from server.auth import connect_db
from server.cart import empty_cart

# Create a Blueprint named 'checkout'
checkout = Blueprint('checkout', __name__)

# Set up the Stripe API key
stripe.api_key = 'sk_test_51OMpXoHvvZmuUjygCBO7ymXz1pc4kdkQrODcZOyyIdUzGhce4b9rYPMZGebqhmQ1oTwzLj7LAv4Ox4wf3a1LDLCm00jQlRwgYf'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "database.db")
connection = sqlite3.connect(DB_PATH, check_same_thread=False)
db = connection.cursor()


# Route for creating a checkout session
@checkout.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.json
    amount = data.get('amount')

    # Create a checkout session using the Stripe API
    session = stripe.checkout.Session.create(
        # Specify shipping options and restrictions
        shipping_address_collection={"allowed_countries": ["IT"]},
        shipping_options=[
            {
                "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 0, "currency": "eur"},
                    "display_name": "Free shipping",
                    "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 3},
                        "maximum": {"unit": "business_day", "value": 7},
                    },
                },
            },
            {
                "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 500, "currency": "eur"},
                    "display_name": "Premium",
                    "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 1},
                        "maximum": {"unit": "business_day", "value": 3},
                    },
                },
            },
        ],
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'Payment Amount',
                },
                'unit_amount': int(amount)
            },
            'quantity': 1,
        }],
        payment_intent_data={
            'description': 'Order Payment',
        },
        mode='payment',
        success_url='http://localhost:5000/success',
        cancel_url='http://localhost:5000/cancel',
    )

    return jsonify({'redirect': session.url})


# Route for handling successful payment
@checkout.route('/success')
def successPayment():
    # Empty the cart and render the success template
    empty_cart()
    return render_template('cart/success.html')


# Route for handling canceled payment
@checkout.route('/cancel')
def cancelPayment():
    # Render the cancel template
    return render_template('cart/cancel.html')

@checkout.teardown_request
def close_db(error):
  db = g.pop('db', None)
  if db is not None:
    db.close()