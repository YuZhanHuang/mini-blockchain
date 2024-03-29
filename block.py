from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = f'{self.time_stamp}{str(self.transactions)}{self.previous_hash}{self.nonce}'
        block_hash = sha256(block_header.encode())

        return block_hash.hexdigest()

    def print_contents(self):
        print("Block contents")
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)