# from flask import Flask, jsonify, request, render_template, request
# from fastapi import FastAPI
# # from app.database import init_db
# # from app.auth import auth_routes


# app = Flask(__name__)

# # Endpoint to search for a character by name
# @app.route('/search', methods=['GET'])
# def search_character():
#     name = request.args.get('name')
   
#     if not name:
#         return jsonify({"error": "Name parameter is required"}), 400
   
#     try:
#         # Use SWAPI's search endpoint to find character by name
#         response = request.get(f'https://swapi.dev/api/people/?search={name}')
#         # response = requests.get(f'https://swapi.dev/api/people/search?={name}')
#         # find out what is not working on 126 
#         print(response.json())
#         response.raise_for_status()
       
#         # Parse the response JSON
#         search_results = response.json().get("results")
       
#         if not search_results:
#             return jsonify({"message": "No characters found"}), 404
       
#         # Return details of the first matching character
#         character_data = search_results[0]
#         # character_name = search_results[0]
#         return jsonify({
#             "name": character_data.get("name"),
#             "height": character_data.get("height"),
#             "mass": character_data.get("mass"),
#             "hair_color": character_data.get("hair_color"),
#             "skin_color": character_data.get("skin_color"),
#             "eye_color": character_data.get("eye_color"),
#             "birth_year": character_data.get("birth_year"),
#             "gender": character_data.get("gender"),
#         })

#     except request.exceptions.RequestException:
#         return jsonify({"error": "Could not perform search"}), 500
    