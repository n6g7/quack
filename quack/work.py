def compute_proof(last_proof):
    """Find the next number divisible by the last proof and nine"""

    incrementor = last_proof + 1

    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    return incrementor
