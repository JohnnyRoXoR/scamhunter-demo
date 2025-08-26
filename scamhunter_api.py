from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load scam addresses from the JSON file
with open('scammers.json', 'r') as file:
    SCAMMERS = set(json.load(file))


@app.route('/check', methods=['GET'])
def check_address():
    # Check if an address is in the scam database
    address = request.args.get('address')
    if not address:
        return jsonify({'error': 'Address parameter is required.'}), 400
    return jsonify({'address': address, 'is_scammer': address in SCAMMERS})


if __name__ == '__main__':
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000)
