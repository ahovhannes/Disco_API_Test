#
# Collection of functions generating random numbers
#

import random

class bddRandom:

    def generate_random_number(self, beginNumber, endNumber, seedValue=None):
        """
        Generate random number between given numbers
        
        Args:
            beginNumber : Start number
            endNumber   : End number
            seedValue   : Optional seed value

        Returns:
            Generated random number
        """
        n = None
        if seedValue:
            random.seed(seedValue)
        n = random.randint(beginNumber, endNumber)
        return n

