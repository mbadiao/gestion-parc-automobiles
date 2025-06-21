import os

class Config:
    SECRET_KEY = "change-this-secret-key"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:passer@localhost:5432/gestion_parc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
