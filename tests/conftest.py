import os
import tempfile

import pytest

contents = {
    "ftdna": (
        [
            "RSID,CHROMOSOME,POSITION,RESULT\n",
            "rs123,1,12345,GG\n",
            "rs4312,2,453231,AT\n",
        ],
        ".csv",
    ),
    "23andme": (
        [
            "#rsid\tchromosome\tposition\tgenotype\n",
            "rs123\t1\t12345\tGG\n",
            "rs4312\t2\t453231\tAT\n",
        ],
        ".txt",
    ),
}


@pytest.fixture(params=["ftdna", "23andme"])
def snp_file(request):
    content, extension = contents[request.param]

    _, tmp_path = tempfile.mkstemp(suffix=extension)

    with open(tmp_path, "w") as f:
        f.writelines(content)

    yield tmp_path

    os.unlink(tmp_path)
