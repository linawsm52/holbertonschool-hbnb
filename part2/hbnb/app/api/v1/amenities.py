from flask import request # access data sent in the HTTP reques
from flask_restx import Namespace, Resource, fields
from app.services.facade import facade # HBnBFacade instance

api = Namespace("amenities", description="Amenity operations")

amenity_model = api.model(
    "Amenity",
    {
        "id": fields.String(readonly=True),
        "name": fields.String(required=True),
        "created_at": fields.String(readonly=True),
        "updated_at": fields.String(readonly=True),
    },
)

amenity_create_model = api.model(
    "AmenityCreate",
    {
        "name": fields.String(required=True),
    },
)


@api.route("/")
class AmenityList(Resource):
    # GET and POST
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return [a for a in facade.get_all_amenities()], 200

    @api.expect(amenity_create_model, validate=True) # validates incoming data
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.get_json()
        try:
            amenity = facade.create_amenity(data)
            return amenity, 201
        except ValueError:
            return {"error": "Invalid amenity name"}, 400


@api.route("/<string:amenity_id>")
class AmenityItem(Resource):

    @api.marshal_with(amenity_model)
    @api.response(200, "Amenity found")
    @api.response(404, "Amenity not found")
    def get(self, amenity_id):
        """Get amenity by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity


    @api.expect(amenity_create_model, validate=True)
    @api.marshal_with(amenity_model)
    @api.response(200, "Amenity updated successfully")
    @api.response(404, "Amenity not found")
    def put(self, amenity_id):
        """Update amenity by ID"""
        amenity = facade.update_amenity(amenity_id, request.get_json())
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity
