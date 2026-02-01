def nucleotide_count(dna):
    dna = dna.upper()

    counts = {
        'A': 0,
        'T': 0,
        'G': 0,
        'C': 0
    }

    for base in dna:
        if base in counts:
            counts[base] += 1

    return counts


sequence = "ATGCGTACGTTAGC"
result = nucleotide_count(sequence)

print("DNA Sequence:", sequence)
print("Nucleotide Counts:")
print("A:", result['A'])
print("T:", result['T'])
print("G:", result['G'])
print("C:", result['C'])

