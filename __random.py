import random
import time
import os
import hashlib

class CustomRandom:
    def __init__(self):
        self.seed = self._generate_seed()

    def _generate_seed(self):
        # Combine multiple sources of entropy
        entropy = str(time.time()) + str(os.urandom(16)) + str(random.random())
        seed = int(hashlib.sha256(entropy.encode('utf-8')).hexdigest(), 16)
        return seed

    def random(self):
        # Update seed with more entropy
        entropy = str(time.time()) + str(os.urandom(16)) + str(random.random())
        self.seed ^= int(hashlib.sha256(entropy.encode('utf-8')).hexdigest(), 16)
        random.seed(self.seed)
        return random.random()

    def randint(self, a, b):
        # Generate a random integer in the range [a, b]
        entropy = str(time.time()) + str(os.urandom(16)) + str(random.random())
        self.seed ^= int(hashlib.sha256(entropy.encode('utf-8')).hexdigest(), 16)
        random.seed(self.seed)
        return random.randint(a, b)

# Example usage
