from flask_restx import Namespace

# Create the namespace; routes will attach to this
api = Namespace('users', description='User operations')
