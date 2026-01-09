from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.facade import facade

api = Namespace("places", description="Place operations")

# Output model (what we return)
owner_brief = api.model("OwnerBrief", {
    "id": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
})

amenity_brief = api.model("AmenityBrief", {
    "id": fields.String,
    "name": fields.String,
})

place_model = api.model("Place", {
    "id": fields.String(readonly=True),
    "title": fields.String(required=True),
    "description": fields.String,
    "price": fields.Integer(required=True),
    "latitude": fields.Float(required=True),
    "longitude": fields.Float(required=True),
    "owner_id": fields.String(required=True),
    "owner": fields.Nested(owner_brief),
    "amenity_ids": fields.List(fields.String),
    "amenities": fields.List(fields.Nested(amenity_brief)),
})

# Input model (what we expect in POST/PUT)
place_input = api.model("PlaceInput", {
    "title": fields.String(required=True),
    "description": fields.String,
    "price": fields.Integer(required=True),
    "latitude": fields.Float(required=True),
    "longitude": fields.Float(required=True),
    "owner_id": fields.String(required=True),
    "amenity_ids": fields.List(fields.String, required=False),
})


@api.route("/")
class PlaceList(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        places = facade.get_all_places()
        return [p.to_dict_extended(facade) for p in places], 200

    @api.expect(place_input, validate=True)
    @api.marshal_with(place_model, code=201)
    def post(self):
        data = request.get_json(silent=True)
        if not data:
            return {"error": "Invalid JSON"}, 400

        try:
            place = facade.create_place(data)
            return place.to_dict_extended(facade), 201
        except ValueError as e:
            return {"error": str(e)}, 400


@api.route("/<string:place_id>")
class PlaceItem(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if place is None:
            return {"error": "Place not found"}, 404
        return place.to_dict_extended(facade), 200

    @api.expect(place_input, validate=True)
    @api.marshal_with(place_model)
    def put(self, place_id):
        data = request.get_json(silent=True)
        if not data:
            return {"error": "Invalid JSON"}, 400

        try:
            updated = facade.update_place(place_id, data)
            if updated is None:
                return {"error": "Place not found"}, 404
            return updated.to_dict_extended(facade), 200
        except ValueError as e:
            return {"error": str(e)}, 400
