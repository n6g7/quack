from block import Block


class Chain(list):
    def __init__(self):
        self.append(Block.genesis())

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
