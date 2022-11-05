from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
connector = Connector()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from google.cloud.sql.connector import Connector, IPTypes

'''def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "team14-t3:us-central1:t3",
        "pymysql",
        user="victoria",
        password="Tabboule7",
        db="t3_team14"
    )
    return conn'''

# create connection pool
''''pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
'''
def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "team14-t3:us-central1:t3", # Cloud SQL Instance Connection Name
            "pg8000",
            user="victoria",
            password="Tabboule7",
            db="t3_team14",
            ip_type= IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
        )
        return conn


app = Flask(__name__)

# configure Flask-SQLAlchemy to use Python Connector
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "creator": getconn
}

db = SQLAlchemy(app)

