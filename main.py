from utils import analyze_dna, reverse_complement

def main():
    dna = input("Enter DNA sequence: ")

    result = analyze_dna(dna)
    rev_comp = reverse_complement(dna)

    print("\nDNA Analysis Result")
    print("-------------------")
    print(f"Length: {result['length']}")
    print(f"A: {result['A']}")
    print(f"T: {result['T']}")
    print(f"G: {result['G']}")
    print(f"C: {result['C']}")
    print(f"GC Content: {result['GC']}%")
    print(f"Reverse Complement: {rev_comp}")


if __name__ == "__main__":
    main()