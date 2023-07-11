import datetime
import hashlib


class Block:
    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.hash = self.calculate_hash()
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0

    def get_index(self):
        return self.index

    def get_timestamp(self):
        return self.timestamp
    
    def get_hash(self):
        return self.hash
    
    def get_previous_hash(self):
        return self.previous_hash
    
    def get_data(self):
        return self.data
    
    def string_hash(self):
        return str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.data) + str(self.nonce)
    
    def block_info(self):
        info = {
            self.index: {
                "previous_hash": self.previous_hash, 
                "timestamp": datetime.datetime.fromtimestamp(self.timestamp), 
                "data": self.data, 
                "hash": self.hash}
                }
        
        return info
    
    def calculate_hash(self):    
        if self is not None:
            try:
                digest = hashlib.sha256()
            except:
                return None
            
            block_data = self.str()
            block_bytes = block_data.encode('utf-8')
            digest.update(block_bytes)
            bytes_hash = digest.digest()
            builder = []
            
            for b in bytes_hash:
                hex_value = format(b, "02x")
                builder.append(hex_value)
            
            return ''.join(builder)
        
        return None
    
    def proof_of_work(self, difficulty):
        zeros = ""
        for _ in range(difficulty):
            zeros += "0"

        while self.get_hash()[:difficulty] != zeros:
            self.nonce += 1
            self.hash = self.calculate_hash()
