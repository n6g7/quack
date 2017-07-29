from chain import Chain
from work import compute_proof


class Node:
    def __init__(self, address, peers=[]):
        self.address = address
        self.chain = Chain()
        self.transactions = []

    def add_transaction(self, from_address, to, amount):
        self.transactions.append({
            'amount': amount,
            'from': from_address,
            'to': to
        })

    def mine(self):
        last_proof = self.chain[-1].data['proof_of_work']
        proof = compute_proof(last_proof)

        self.add_transaction(
            'network',
            self.address,
            1
        )

        self.chain.proove(proof, self.transactions)
        self.transactions[:] = []
