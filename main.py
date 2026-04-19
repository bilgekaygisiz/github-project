import argparse

from src.analysis import analyze_dna
from src.sequence_tools import reverse_complement, transcribe_dna_to_rna
from src.fasta_reader import read_fasta
from src.protein_translation import translate_rna_orf
from src.visualization import plot_gc_content


def main():
    parser = argparse.ArgumentParser(description="DNA Analysis Toolkit")
    parser.add_argument("--file", required=True, help="FASTA file path")

    args = parser.parse_args()

    sequences = read_fasta(args.file)

    print("\n=== BIOINFORMATICS PIPELINE ===")

    output_lines = []

    for name, dna in sequences.items():

        result = analyze_dna(dna)
        rev = reverse_complement(dna)
        rna = transcribe_dna_to_rna(dna)
        protein = translate_rna_orf(rna)

        print(f"\nSequence: {name}")
        print(f"DNA: {dna}")
        print(f"Length: {result['length']}")
        print(f"GC Content: {result['GC']}%")
        print(f"RNA: {rna}")
        print(f"Protein: {protein}")
        print(f"Reverse Complement: {rev}")

        output_lines.append(f"Sequence: {name}")
        output_lines.append(f"DNA: {dna}")
        output_lines.append(f"Length: {result['length']}")
        output_lines.append(f"GC Content: {result['GC']}%")
        output_lines.append(f"RNA: {rna}")
        output_lines.append(f"Protein: {protein}")
        output_lines.append(f"Reverse Complement: {rev}")
        output_lines.append("")

    with open("results.txt", "w") as f:
        for line in output_lines:
            f.write(line + "\n")

    plot_gc_content(sequences)


if __name__ == "__main__":
    main()