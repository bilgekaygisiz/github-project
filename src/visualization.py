import matplotlib.pyplot as plt

def plot_gc_content(sequences):
    names = []
    gc_values = []

    for name, dna in sequences.items():
        names.append(name)

        g = dna.upper().count("G")
        c = dna.upper().count("C")

        gc = (g + c) / len(dna) * 100 if len(dna) > 0 else 0
        gc_values.append(gc)

    plt.figure()

    plt.bar(names, gc_values)
    plt.title("GC Content per DNA Sequence")
    plt.xlabel("Sequences")
    plt.ylabel("GC %")
    plt.ylim(0, 100)

    # 🔥 ARTIK PENCERE YOK — DOSYA VAR
    plt.savefig("gc_content_plot.png", dpi=300, bbox_inches="tight")

    print("\nGraph saved as: gc_content_plot.png")