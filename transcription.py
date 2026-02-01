def transcribe_dna_to_rna(dna):
    dna = dna.upper()

    transcription_map = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    rna = ""

    for base in dna:
        # YOU fill this line
        pass

    return rna


sequence = "ATGCGTACGTTAGC"
result = transcribe_dna_to_rna(sequence)

print("DNA:", sequence)
print("RNA:", result)
