def read_fasta(file_path):
    sequences = {}
    current_id = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                current_id = line[1:]
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

    return sequences