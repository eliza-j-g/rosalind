def count_nucleotides(dna_string):
    nucleotides = [*dna_string]
    nucleotide_counts = {base: nucleotides.count(base) for base in nucleotides}
    return nucleotide_counts

DNA_STRING = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

if __name__ == "__main__":
    print(count_nucleotides(DNA_STRING))