from typing import List

from block import Block


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.unconfirmed_transactions: List[Block] = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)

    def add_block(self, transactions: dict):
        previous_hash = self.chain[len(self.chain) - 1].hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f'Block {i} {current_block}')
            current_block.print_contents()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current, previous = self.chain[i], self.chain[i - 1]
            if current.hash != current.generate_hash():
                return False

            if previous.hash != previous.generate_hash():
                return False

        return True

    @staticmethod
    def proof_of_work(block: Block, difficulty=2):
        proof = block.generate_hash()
        while proof[:2] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()

        block.nonce = 0

        return proof


if __name__ == '__main__':
    # initial data
    block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
    block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
    block_three_transactions = {"sender": "Alice", "receiver": "Cole", "amount": "35"}
    fake_transactions = {"sender": "Bob", "receiver": "Cole, Alice", "amount": "25"}

    # Prepare a local blockchain
    print("========== initial the local blockchain ==========")
    local_blockchain = Blockchain()
    local_blockchain.print_blocks()

    print("========== add blocks to blockchain ==========")
    local_blockchain.add_block(block_one_transactions)
    local_blockchain.add_block(block_two_transactions)
    local_blockchain.add_block(block_three_transactions)

    local_blockchain.print_blocks()

    # Try to tamper the block
    local_blockchain.chain[2].transactions = fake_transactions
    local_blockchain.validate_chain()
