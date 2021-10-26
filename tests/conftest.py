import os
import tempfile

import pytest


@pytest.fixture
def ftdna_file():
    content = [
        "RSID,CHROMOSOME,POSITION,RESULT\n",
        "rs123,1,12345,GG\n",
        "rs4312,2,453231,AT\n",
    ]
    _, tmp_path = tempfile.mkstemp(suffix='.csv')

    with open(tmp_path, 'w') as f:
        f.writelines(content)

    yield tmp_path

    os.unlink(tmp_path)


@pytest.fixture
def twentythreeandme_file():
    content = [
        "#rsid\tchromosome\tposition\tgenotype\n",
        "rs123\t1\t12345\tGG\n",
        "rs4312\t2\t453231\tAT\n",
    ]

    _, tmp_path = tempfile.mkstemp(suffix='.txt')

    with open(tmp_path, 'w') as f:
        f.writelines(content)

    yield tmp_path

    os.unlink(tmp_path)
