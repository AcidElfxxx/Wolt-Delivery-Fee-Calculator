from flask import Flask, request, jsonify
import datetime
from dateutil.parser import parse

app = Flask(__name__)

@app.route('/calculate_delivery_fee', methods=['POST'])
def calculate_delivery_fee():
    data = request.get_json()
    cart_value = data['cart_value']
    delivery_distance = data['delivery_distance']
    item_count = data['number_of_items']
    delivery_time = parse(data['time'])
    
    base_fee = 200
    surcharge = 0
    bulk_fee = 0
    
    # Small order surcharge
    if cart_value < 1000:
        surcharge = 1000 - cart_value
    
    # Delivery distance fee
    if delivery_distance > 1000:
        additional_distance = delivery_distance - 1000
        additional_fee = additional_distance / 500
        additional_fee = int(additional_fee)
        if additional_distance % 500 != 0:
            additional_fee += 1
        base_fee += additional_fee * 100

    
    # Item count fee
    if item_count >= 5:
        additional_items = item_count - 4
        bulk_fee = additional_items * 50
        if item_count > 12:
            bulk_fee += 120
    
    # Friday rush fee
    if delivery_time.weekday() == 4 and delivery_time.hour >= 15 and delivery_time.hour < 19:
        base_fee *= 1.2
    
    # Maximum delivery fee
    if (base_fee + surcharge + bulk_fee) > 1500:
        total_fee = 1500
    else:
        total_fee = base_fee + surcharge + bulk_fee
    
    # Free delivery for cart value >= 100€
    if cart_value >= 10000:
        total_fee = 0
    
    return jsonify({'delivery_fee': total_fee})

if __name__ == '__main__':
    app.run(debug=True)

