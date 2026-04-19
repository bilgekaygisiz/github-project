def reverse_complement(sequence):
    mapping = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    return "".join(mapping.get(base, base) for base in reversed(sequence.upper()))