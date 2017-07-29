import datetime as date
import hashlib as hasher
import random


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def __str__(self):
        return self.hash[:8]

    def compute_hash(self):
        data = '%s%s%s%s' % (
            self.index,
            self.timestamp,
            self.data,
            self.previous_hash
        )
        sha = hasher.sha256()
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()

    def next(self, data):
        next_index = self.index + 1

        return self.__class__(
            next_index,
            date.datetime.now(),
            data,
            self.hash
        )

    @property
    def dict(self):
        return {
            'index': self.index,
            'timestamp': str(self.timestamp),
            'data': self.data,
            'hash': self.hash
        }

    @classmethod
    def genesis(cls):
        genesis_proof = random.randint(1, 100)
        data = {
            'proof_of_work': genesis_proof,
            'transactions': []
        }
        return cls(0, date.datetime.now(), data, '0')
