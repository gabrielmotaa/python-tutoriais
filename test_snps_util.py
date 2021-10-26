from snps_util import complementary_strand

import pytest


@pytest.mark.parametrize(
    "sequence,result",
    [
        ('AAATTTCCGG', 'TTTAAAGGCC'),
        ('A','T'),
        ('CATCATGATACC', 'GTAGTACTATGG')
    ]
)
def test_complementary_strand_success(sequence, result):
    """Deve retornar sequências de DNA invertidas corretamente"""
    assert complementary_strand(sequence) == result


@pytest.mark.parametrize(
    "incorrect_sequence",
    [(1,), (True,), ([],)]
)
def test_complementary_strand_failure(incorrect_sequence):
    """Deve estourar um TypeError se uma string não for passada."""
    pytest.raises(TypeError, complementary_strand, incorrect_sequence)
