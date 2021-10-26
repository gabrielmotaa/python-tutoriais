def complementary_strand(sequence):
    """Recebe uma sequência de DNA e retorna a fita complementar."""
    translator = str.maketrans('ATCG', 'TAGC')
    return sequence.translate(translator)