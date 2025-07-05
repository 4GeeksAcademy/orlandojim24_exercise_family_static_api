"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members/<int:member_id>', methods=['GET'])
def get_family_member(member_id):
    member = jackson_family.get_member(member_id)

    if member is None:
        return jsonify({"error": "Member not found"}), 404

    return jsonify(member), 200


@app.route('/members', methods=['POST'])
def add_family_member():
    # Get the JSON body from the request
    member = request.get_json()

    # Check if it's missing or invalid
    if not member:
        return jsonify({"error": "Missing or invalid request body"}), 400

    # Add the member using your FamilyStructure class
    added_member = jackson_family.add_member(member)

    # Return the newly added member
    return jsonify(added_member), 200
    
@app.route('/members', methods=['GET'])
def get_all_family_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    was_deleted = jackson_family.delete_member(member_id)

    if was_deleted:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_family_member(member_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    updated_member = jackson_family.update_member(member_id, updated_data)

    if updated_member:
        return jsonify(updated_member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
