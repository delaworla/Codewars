





def DNA_strand(strand):
    '''
    Returns the complementary strand of DNA for a given strand.
    '''
    complementary_strand = ""
    for symbol in strand:
        if symbol == 'A':
            complementary_strand += 'T'
            continue
        if symbol == 'T':
            complementary_strand += 'A'
            continue
        if symbol == 'C':
            complementary_strand += 'G'
            continue
        if symbol == 'G':
            complementary_strand += 'C'
            continue
    return complementary_strand


print(DNA_strand("ATTGC"))
print(DNA_strand("GTTAAC"))
