def analyze_dna(sequence):
    length = len(sequence)

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = (g_count + c_count) / length * 100

    print("Sequence length:", length)
    print("A:", a_count)
    print("T:", t_count)
    print("G:", g_count)
    print("C:", c_count)
    print("GC content:", gc_content, "%")


sequence="ATATATGGCC"

analyze_dna(sequence)
