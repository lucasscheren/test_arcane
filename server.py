from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///arcane.db')
app = Flask(__name__)
api = Api(app)

class City_Properties(Resource):
    def get(self, city):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM properties WHERE city =%s "  %str(city))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Properties(Resource):
    def post(self):
        conn = db_connect.connect()
        json_data = request.get_json()
        name = json_data['name']
        description = json_data['description']
        city = json_data['city']
        room = json_data['room']
        room_desc = json_data['room_desc']
        owner = json_data['owner']
        property_type = json_data['property_type']
        result = "INSERT INTO properties (name, description, city, room, room_desc, owner, property_type) VALUES ('" + str(name) + "', '" + str(description) + "', '" + str(city) + "', '" + str(room) +"', '" + str(room_desc) +"', '" + str(owner) + "', '" + str(property_type) +"')"
        conn.execute(result)
        return (result)
    def put(self):
        conn = db_connect.connect()
        json_data = request.get_json()
        column = json_data['column']
        value = json_data['value']
        id_property = json_data['id_property']
        result = "UPDATE properties SET "+ column +" ='" + value + "' WHERE id_property = "+ str(id_property)
        conn.execute(result)
        return (result)
    
class Users(Resource):
    def post(self):
        conn = db_connect.connect()
        json_data = request.get_json()
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        birthday = json_data['birthday']
        result = "INSERT INTO users (first_name, last_name, birthday) VALUES ('" + str(first_name) + "', '" + str(last_name) + "', '" + str(birthday) + "')"
        conn.execute(result)
        return (result)
    def put(self):
        conn = db_connect.connect()
        json_data = request.get_json()
        column = json_data['column']
        value = json_data['value']
        id_user = json_data['id_user']
        result = "UPDATE users SET "+ column +" ='" + value + "' WHERE id_user = "+ str(id_user)
        conn.execute(result)
        return (result)

api.add_resource(City_Properties, '/properties/<city>')
api.add_resource(Properties, '/properties')
api.add_resource(Users, '/user')
                
if __name__ == '__main__':
     app.run(port='5002')