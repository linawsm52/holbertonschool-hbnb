#!/usr/bin/python3
from flask import request
from flask_restx import Namespace, Resource, fields

from app import facade


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


@api.route("/amenities/")
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return [a.to_dict() for a in facade.get_all_amenities()], 200

    @api.expect(amenity_create_model, validate=True)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.get_json(silent=True)
        if not data:
            return {"error": "Invalid JSON"}, 400

        try:
            amenity = facade.create_amenity(data)
            return amenity.to_dict(), 201
        except ValueError:
            return {"error": "Invalid amenity name"}, 400


@api.route("/amenities/<string:amenity_id>")
class AmenityItem(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Get amenity by ID"""
        amenity = facade.get_amenity(amenity_id)
        if amenity is None:
            return {"error": "Amenity not found"}, 404
        return amenity.to_dict(), 200

    @api.expect(amenity_create_model, validate=True)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update amenity by ID"""
        data = request.get_json(silent=True)
        if not data:
            return {"error": "Invalid JSON"}, 400

        try:
            amenity = facade.update_amenity(amenity_id, data)
            if amenity is None:
                return {"error": "Amenity not found"}, 404
            return amenity.to_dict(), 200
        except ValueError:
            return {"error": "Invalid amenity name"}, 400
