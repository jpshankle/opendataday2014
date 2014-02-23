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
	source_type = db.StringField()
	name = db.StringField()
	url = db.StringField()
	country = db.StringField()
	region = db.StringField()
	language = db.StringField()
	currency = db.StringField()
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
  #	thePost = Contract()
  #   for postProperty in postData:
		# thePost[postProperty] = postData[postProperty]
  #   thePost.save();
  return json.dumps([{"message":'success'}])

@app.route('/api/source', methods=['POST', 'GET'])
def sourceApi():
	if request.args.get('importSource'):
		return Source.objects(id=request.args.get('importSource'))[0].to_json()
	elif request.method == 'POST':
		the_source = json.loads(request.data)
		source_doc = Source()
		for prop in the_source:
			source_doc[prop] = the_source[prop]
		source_doc.save()
		return json.dumps({"things": "things"})
	else:
		return Source.objects.to_json()

if __name__ == "__main__":
	app.run()
