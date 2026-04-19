codon_table = {
    "AUG":"M",
    "UUU":"F", "UUC":"F",
    "UUA":"L", "UUG":"L",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "AUU":"I", "AUC":"I", "AUA":"I",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "UAA":"Stop", "UAG":"Stop", "UGA":"Stop"
}

def translate_rna_orf(rna):
    protein = []
    start = False

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]

        # START codon bul
        if codon == "AUG":
            start = True
            protein.append("M")
            continue

        if not start:
            continue

        amino_acid = codon_table.get(codon, "?")

        if amino_acid == "Stop":
            break

        protein.append(amino_acid)

    return "".join(protein)