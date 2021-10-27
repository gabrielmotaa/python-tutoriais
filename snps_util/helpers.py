def complementary_strand(sequence):
    """Recebe uma sequência de DNA e retorna a fita complementar."""
    if not isinstance(sequence, str):
        raise TypeError("Apenas strings podem ser passadas como argumento.")
    translator = str.maketrans("ATCG", "TAGC")
    return sequence.translate(translator)
