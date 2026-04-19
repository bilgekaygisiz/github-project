def analyze_dna(sequence):
    sequence = sequence.upper()

    length = len(sequence)
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = (g + c) / length * 100 if length > 0 else 0

    return {
        "length": length,
        "A": a,
        "T": t,
        "G": g,
        "C": c,
        "GC": round(gc_content, 2)
    }