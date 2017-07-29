from flask import Flask, request
from node import Node
import json
import uuid


app = Flask(__name__)
node = Node(str(uuid.uuid4()))


@app.route('/blocks', methods=['GET'])
def list_blocks():
    return json.dumps(node.chain.dict)


@app.route('/credit/<string:address>', methods=['GET'])
def credit(address):
    return json.dumps({
        'credit': node.chain.get_credit(address)
    })


@app.route('/transactions', methods=['GET'])
def list_transactions():
    return json.dumps(node.transactions)


@app.route('/transactions', methods=['POST'])
def create_transaction():
    node.add_transaction(**request.get_json())

    return 'Transaction submission successful'


@app.route('/mine', methods=['GET'])
def mine():
    node.mine()
    app.logger.info('Mined a new block')

    return json.dumps(node.chain[-1].dict)

