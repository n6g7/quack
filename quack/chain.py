from block import Block


class Chain(list):
    def __init__(self):
        self.append(Block.genesis())

    def get_credit(self, address):
        credit = 0

        for block in self:
            for tx in block.data['transactions']:
                if tx['from'] == address:
                    credit -= tx['amount']
                if tx['to'] == address:
                    credit += tx['amount']

        return credit

    def proove(self, proof, transactions):
        last_block = self[-1]
        new_block = last_block.next({
            "proof_of_work": proof,
            "transactions": list(transactions)
        })

        self.append(new_block)
        return new_block

    @property
    def dict(self):
        return list(map(lambda block: block.dict, self))

    @classmethod
    def from_list(cls, lst):
        chain = cls()
        chain[:] = lst
        return chain
