# world.py
# This module defines the structure and relationships of the game world, including its layers, bots, and events.
# It provides a hierarchical representation of arcs, meta-arcs, subplots, and the interactions of bots within this world.

from app.models.database import db

# World Model
class World(db.Model):
    __tablename__ = 'worlds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    layers = db.relationship('WorldLayer', backref='world', lazy=True)
    bots = db.relationship('Bot', backref='world', lazy=True)

# World Layers Model
class WorldLayer(db.Model):
    __tablename__ = 'world_layers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    layer = db.Column(db.String(50), nullable=False)  # Values can be 'Arc', 'MetaArc', 'Subplot'
    parent_id = db.Column(db.Integer, db.ForeignKey('world_layers.id'), nullable=True)  # For hierarchical relationships
    world_id = db.Column(db.Integer, db.ForeignKey('worlds.id'), nullable=False)
    children = db.relationship('WorldLayer', backref=db.backref('parent', remote_side=[id]), lazy=True)
    events = db.relationship('Event', backref='world_layer', lazy=True)

# Bot Model
class Bot(db.Model):
    __tablename__ = 'bots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=True)  # Role or backstory of the bot
    world_id = db.Column(db.Integer, db.ForeignKey('worlds.id'), nullable=False)
    events = db.relationship('Event', backref='bot', lazy=True)