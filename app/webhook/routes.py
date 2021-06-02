from flask import Blueprint, json, request
from run import mongodb_client
webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.route('/')
def root():
    return "this is the webhook page"

@webhook.route('/receiver', methods=["GET","POST"])
def receiver():
    req = mongodb_client.db.requests
    if request.headers['content-type']=='application/json':
        data = json.dumps(request.json,indent= 4)
        json_object = json.loads(data)
        print(data)
    return "wow"
