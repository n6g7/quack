from chain import Chain


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
