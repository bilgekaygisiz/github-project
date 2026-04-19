from src.analysis import analyze_dna
from src.sequence_tools import reverse_complement
from src.fasta_reader import read_fasta

def main():
    sequences = read_fasta("data/sample.fasta")

    print("\n=== DNA ANALYSIS REPORT ===")

    for name, dna in sequences.items():
        result = analyze_dna(dna)
        rev = reverse_complement(dna)

        print(f"\nSequence: {name}")
        print(f"Length: {result['length']}")
        print(f"A: {result['A']}")
        print(f"T: {result['T']}")
        print(f"G: {result['G']}")
        print(f"C: {result['C']}")
        print(f"GC Content: {result['GC']}%")
        print(f"Reverse Complement: {rev}")


if __name__ == "__main__":
    main()