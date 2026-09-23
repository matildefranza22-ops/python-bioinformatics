import sys

seq=input("Insert your DNA sequence:").upper()

#Validation
def validation(seq):
    for i in seq[:]:
        if i not in ("A", "T", "C", "G"):
            return "The sequence is NOT valid!"
            sys.exit()
    return "The sequence is valid!"
print(validation(seq))

#Length and base count
def length_dna(seq):
    return len(seq)

print("Length:",length_dna(seq))

def count_bases(seq):
    a_count=seq.count("A")
    t_count=seq.count("T")
    c_count=seq.count("C")
    g_count=seq.count("G")
    return "A count:", a_count, "T count:", t_count, "C_count:", c_count, "G_count:", g_count

print("Base count:", count_bases(seq))

#GC%
def GC_content(seq):
    c_count=seq.count("C")
    g_count=seq.count("G")
    gc_content=((c_count+g_count)/len(seq))*100
    return round(gc_content,2)

print("GC%", GC_content(seq))

#Reverse complement
def reverse_complement(seq):
    rc=""
    for i in seq[::-1]:
        if i=="A":
            rc+="T"
        elif i=="T":
            rc+="A"
        elif i=="C":
            rc+="G"
        else:
            rc+="C"
    return rc

print ("Reverse Complement:", reverse_complement(seq))

#DNA to RNA
def dna_to_rna(seq):
    rna=seq.replace("T", "U")
    return rna

print("Rna sequence:", dna_to_rna(seq))

#RNA to protein
rna=dna_to_rna(seq)

def translate_rna(rna):
    frame = int(input("Insert the reading frame (+1, +2, +3, -1, -2, -3): "))

    protein = ""

    genetic_code = {
        "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu","CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "AUU": "Ile","AUC": "Ile","AUA": "Ile",
        "AUG": "Met",
        "GUU": "Val","GUC": "Val","GUA": "Val","GUG": "Val",
        "UCU": "Ser","UCC": "Ser","UCA": "Ser","UCG": "Ser","AGU": "Ser", "AGC": "Ser",
        "CCU": "Pro","CCC": "Pro","CCA": "Pro","CCG": "Pro","ACU": "Thr","ACC": "Thr","ACA": "Thr","ACG": "Thr",
        "GCU": "Ala","GCC": "Ala","GCA": "Ala","GCG": "Ala",
        "UAU": "Tyr","UAC": "Tyr",
        "UAA": "STOP","UAG": "STOP","UGA": "STOP",
        "CAU": "His","CAC": "His","CAA": "Gln","CAG": "Gln",
        "AAU": "Asn","AAC": "Asn",
        "AAA": "Lys","AAG": "Lys",
        "GAU": "Asp","GAC": "Asp",
        "GAA": "Glu", "GAG": "Glu",
        "UGU": "Cys","UGC": "Cys",
        "UGG": "Trp",
        "CGU": "Arg","CGC": "Arg","CGA": "Arg","CGG": "Arg","AGA": "Arg","AGG": "Arg",
        "GGU": "Gly","GGC": "Gly","GGA": "Gly","GGG": "Gly",
    }

    if frame in (1, 2, 3):
        start = frame - 1
    elif frame in (-1, -2, -3):
        complement = {
            "A": "U",
            "U": "A",
            "C": "G",
            "G": "C"
        }
        reverse_complement_rna = ""
        for nucleotide in rna[::-1]:
            reverse_complement_rna += complement[nucleotide]
        rna = reverse_complement_rna
        start = abs(frame) - 1
    else:
        print("The frame is NOT valid!")
        sys.exit()

    for i in range(start, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if genetic_code[codon] == "STOP":
            break
        protein += genetic_code[codon]
    return protein

print("Protein:", translate_rna(rna))

#Main 
def main():
    seq = input("Insert your DNA sequence: ").upper()

    if not validation(seq):
        print("The sequence is NOT valid!")
        return

    print("The sequence is valid!")

    print(length_dna(seq))
    print(count_bases(seq))
    print(GC_content(seq))
    print(reverse_complement(seq))

    rna = dna_to_rna(seq)
    print("RNA sequence:", rna)

    print(translate_rna(rna))


if __name__ == "__main__":
    main()
