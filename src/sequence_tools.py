def reverse_complement(sequence):
    mapping = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    return "".join(mapping.get(base, base) for base in reversed(sequence.upper()))


def transcribe_dna_to_rna(sequence):
    return sequence.upper().replace("T", "U")