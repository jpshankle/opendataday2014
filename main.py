from flask import Flask, jsonify, request
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from parsers import *
import json

app = Flask(__name__, static_folder='static', static_url_path='')

app.config["MONGODB_SETTINGS"] = {
    'DB': 'stop_corruption'
}

app.debug = True;

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
    source = db.StringField()
    project_name = db.StringField()
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

@app.route('/api/contracts')
def contractsRoute():
	return json.dumps(list(Contract.objects))

@app.route('/api/import', methods=['POST'])
def postImport():
  #   thePost = Contract()
  #   for postProperty in postData:
		# thePost[postProperty] = postData[postProperty]
  #   thePost.save();
  return json.dumps([{"message":'success'}])

@app.route('/api/source', methods=['POST', 'GET'])
def sourceApi():
	if request.method == 'POST':
		return jsonify(path=request.form)
	else:
		return json.dumps(list(Source.objects))

@app.route('/api/source/<source_id>')
def individualSource(source_id):
	return json.dumps(list(Source.objects(id=source_id)))

if __name__ == "__main__":
    app.run()
