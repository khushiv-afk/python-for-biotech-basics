def reverse_complement(dna):
    dna = dna.upper()

    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    rev_comp = ""

    for base in reversed(dna):
        rev_comp += complement[base]

    return rev_comp


sequence = "ATGCGTACGTTAGC"
result = reverse_complement(sequence)

print("Original DNA:", sequence)
print("Reverse Complement:", result)
