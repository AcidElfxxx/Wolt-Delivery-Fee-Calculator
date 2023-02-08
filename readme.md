This app uses flask, datetime and dateutil.parser libraries. The code is written in Python. 

There is a file called req.http which can be used to test the app by sending post requests with the appropriate json payload.

We need to run the server by using the commant 'python delivery.py'. Flask should be installed.

Test the app using this POST request in the req.http file:


POST http://127.0.0.1:5000//calculate_delivery_fee
Content-Type: application/json

{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
