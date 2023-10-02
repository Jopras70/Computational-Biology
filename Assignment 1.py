def complement(dna):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence = ''.join(complement_dict[base] for base in dna)
    return sequence 

def mrna_to_protein(mrna_sequence):
    codon = {
    "UUU": "Phe (F)", "UUC": "Phe (F)", "UUA": "Leu (L)", "UUG": "Leu (L)",
    "CUU": "Leu (L)", "CUC": "Leu (L)", "CUA": "Leu (L)", "CUG": "Leu (L)",
    "AUU": "Ile (I)", "AUC": "Ile (I)", "AUA": "Ile (I)", "AUG": "Met (M)",
    "GUU": "Val (V)", "GUC": "Val (V)", "GUA": "Val (V)", "GUG": "Val (V)",
    "UCU": "Ser (S)", "UCC": "Ser (S)", "UCA": "Ser (S)", "UCG": "Ser (S)",
    "CCU": "Pro (P)", "CCC": "Pro (P)", "CCA": "Pro (P)", "CCG": "Pro (P)",
    "ACU": "Thr (T)", "ACC": "Thr (T)", "ACA": "Thr (T)", "ACG": "Thr (T)",
    "GCU": "Ala (A)", "GCC": "Ala (A)", "GCA": "Ala (A)", "GCG": "Ala (A)",
    "UAU": "Tyr (Y)", "UAC": "Tyr (Y)", "UAA": "Stop ()", "UAG": "Stop ()",
    "CAU": "His (H)", "CAC": "His (H)", "CAA": "Gln (Q)", "CAG": "Gln (Q)",
    "AAU": "Asn (N)", "AAC": "Asn (N)", "AAA": "Lys (K)", "AAG": "Lys (K)",
    "GAU": "Asp (D)", "GAC": "Asp (D)", "GAA": "Glu (E)", "GAG": "Glu (E)",
    "UGU": "Cys (C)", "UGC": "Cys (C)", "UGA": "Stop (*)", "UGG": "Trp (W)",
    "CGU": "Arg (R)", "CGC": "Arg (R)", "CGA": "Arg (R)", "CGG": "Arg (R)",
    "AGU": "Ser (S)", "AGC": "Ser (S)", "AGA": "Arg (R)", "AGG": "Arg (R)",
    "GGU": "Gly (G)", "GGC": "Gly (G)", "GGA": "Gly (G)", "GGG": "Gly (G)"
    }

    protein_sequence = ""
    for i in range(0, len(mrna_sequence), 3):
        codons = mrna_sequence[i:i+3]
        amino_acid = codon.get(codons, "X")
        if i == len(mrna_sequence) - 3:
            pass
        else:
            amino_acid = amino_acid + " - "
        protein_sequence += amino_acid
    return protein_sequence

# To transcribe DNA to mRNA
def dna_to_mrna(sequence):
    return sequence.replace('T', 'U')

dna = input("DNA : ")
complement = complement(dna)
mrna_sequence = dna_to_mrna(complement)
protein_sequence = mrna_to_protein(mrna_sequence)

print("Complement :", complement)
print("mRNA Sequence :", mrna_sequence)
print("Protein Sequence :", protein_sequence)
