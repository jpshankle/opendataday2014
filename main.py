from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import pymongo

app = Flask(__name__, static_folder='static', static_url_path='')

app.config["MONGODB_SETTINGS"] = {
    'DB': 'stop_corruption'
}

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

class MapField(db.Document):
    source_field = db.StringField()
    dest_field = db.StringField()

class Source(db.Document):
    url = db.StringField()
    country = db.StringField(required=True)
    region = db.StringField(required=True)
    language = db.StringField(required=True)
    currency = db.StringField(required=True)
    field_mappings = db.ListField(db.ReferenceField(MapField))

class Contract(db.Document):
    source = db.StringField(required=True)
    project_name = db.StringField(required=True)
    description = db.StringField()
    procument_method = db.StringField()
    procument_category = db.StringField()
    organization = db.StringField()
    sector = db.StringField()
    supplier = db.StringField()
    supplier_country = db.StringField()
    fiscal_year = db.StringField()
    contract_signed = db.StringField()
    tender_issued = db.StringField()
    region = db.StringField()
    date = db.DateTimeField()
    amount = db.IntField()

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
