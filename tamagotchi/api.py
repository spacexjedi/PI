# pip install flask-rest-jsonapi flask-sqlalchemy
# touch application.py pets.db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////pets.db'
db = SQLAlchemy(app)

# Define a class for the Pet table
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    saude = db.Column(db.Integer)
    tipo = db.Column(db.String)

# Create the table
db.create_all()



from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Create data abstraction layer
class PetSchema(Schema):
    class Meta:
        type_ = 'pet'
        self_view = 'pet_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'pet_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    saude = fields.Integer(load_only=True)
    tipo = fields.Str()


 # Create resource managers and endpoints

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

class PetMany(ResourceList):
    schema = PetSchema
    data_layer = {'session': db.session,
                  'model': Pet}

class PetOne(ResourceDetail):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Pet}

api = Api(app)
api.route(PetMany, 'pet_many', '/pets')
api.route(PetOne, 'pet_one', '/pets/<int:id>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)


   # curl -i -X POST -H 'Content-Type: application/json' -d '{"data":{"type":"artist", "attributes":{"name":"Salvador Dali", "birth_year":1904, "genre":"Surrealism"}}}' http://localhost:5000/artists



from marshmallow_jsonapi.flask import Relationship
from flask_rest_jsonapi import ResourceRelationship


# Define the Artwork table
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist_id = db.Column(db.Integer, 
        db.ForeignKey('artist.id'))
    artist = db.relationship('Artist',
        backref=db.backref('artworks'))


 # Create data abstraction 
class ArtistSchema(Schema):
    class Meta:
        type_ = 'artist'
        self_view = 'artist_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artist_many'

    id = fields.Integer()
    name = fields.Str(required=True)
    birth_year = fields.Integer(load_only=True)
    genre = fields.Str()
    artworks = Relationship(self_view = 'artist_artworks',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'artwork_many',
        many = True,
        schema = 'ArtworkSchema',
        type_ = 'artwork')

class ArtworkSchema(Schema):
    class Meta:
        type_ = 'artwork'
        self_view = 'artwork_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'artwork_many'

    id = fields.Integer()
    title = fields.Str(required=True)
    artist_id = fields.Integer(required=True)





# a parte do app flask com endpoints 
class ArtworkMany(ResourceList):
    schema = ArtworkSchema
    data_layer = {'session': db.session,
                  'model': Artwork}

class ArtworkOne(ResourceDetail):
    schema = ArtworkSchema
    data_layer = {'session': db.session,
                  'model': Artwork}

class ArtistArtwork(ResourceRelationship):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}


api.route(ArtworkOne, 'artwork_one', '/artworks/<int:id>')
api.route(ArtworkMany, 'artwork_many', '/artworks')
api.route(ArtistArtwork, 'artist_artworks',
    '/artists/<int:id>/relationships/artworks')


#curl -i -X POST -H 'Content-Type: application/json' -d '{"data":{"type":"artwork", "attributes":{"title":"The Persistance of Memory", "artist_id":1}}}' http://localhost:5000/artworks