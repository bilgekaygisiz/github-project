from utils import analyze_dna, reverse_complement

def main():
    dna = input("DNA sequence gir: ")

    result = analyze_dna(dna)
    rev = reverse_complement(dna)

    print("\nRESULT")
    print("------")
    print("Length:", result["length"])
    print("A:", result["A"])
    print("T:", result["T"])
    print("G:", result["G"])
    print("C:", result["C"])
    print("GC%:", result["GC"])
    print("Reverse complement:", rev)


if __name__ == "__main__":
    main()