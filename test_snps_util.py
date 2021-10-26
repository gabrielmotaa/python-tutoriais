from snps_util import complementary_strand


def test_complementary_strand_success():
    """Deve retornar sequências de DNA invertidas corretamente"""
    seq1, res1 = 'AAATTTCCGG', 'TTTAAAGGCC'
    seq2, res2 = 'A','T'
    seq3, res3 = 'CATCATGATACC', 'GTAGTACTATGG'

    assert complementary_strand(seq1) == res1
    assert complementary_strand(seq2) == res2
    assert complementary_strand(seq3) == res3