import time
from objprint import op
from blockchain_code.block import Block


class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []

        # Create the genesis block
        self.create_block_genesis()

    def create_block_genesis(self):
        genesis_block = Block(0, time.time(), None, "GENESIS BLOCK")
        self.blocks.append(genesis_block)

        print("\nGENESIS BLOCK CREATED")
        op(self.blocks)
        print()

    def get_difficulty(self):
        return self.difficulty

    def latest_block(self):
        return self.blocks[-1]

    def new_block(self, data):
        latest_block = self.latest_block()
        new_block = Block(latest_block.get_index() + 1, time.time(), latest_block.get_hash(), data)
        
        print("\nNEW BLOCK WAS GENERATED")
        
        return new_block

    def add_block(self, block):
        if block is not None:
            block.proof_of_work(self.difficulty)
            self.blocks.append(block)

            print("\nNEW BLOCK ADDED")

    def is_first_block_valid(self):
        first_block = self.blocks[0]

        if first_block.get_index() != 0:
            return False

        if first_block.get_previous_hash() is not None:
            return False

        if first_block.get_hash() is None or first_block.get_hash() != first_block.calculate_hash():
            return False

        return True

    def is_valid_new_block(self, new_block, previous_block):
        if new_block is not None and previous_block is not None:
            if previous_block.get_index() + 1 != new_block.get_index():
                return False

            if new_block.get_previous_hash() is None or new_block.get_previous_hash() != previous_block.get_hash():
                return False

            if new_block.get_hash() is None or new_block.get_hash() != new_block.calculate_hash():
                return False

            return True

        return False

    def is_blockchain_valid(self):
        if not self.is_first_block_valid():
            return False

        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]

            if not self.is_valid_new_block(current_block, previous_block):
                return False

        return True

    def __str__(self):
        builder = []
        for block in self.blocks:
            builder.append(str(block))

        return "\n".join(builder)
