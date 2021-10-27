import pytest
from snps_util import SNPFile
from snps_util.files import _read_23andme, _read_ftdna


class TestSNPFile:
    """Suíte de testes específicos para o SNPFile."""

    @pytest.mark.parametrize(
        "filename,reader",
        [
            ("arquivo.csv", _read_ftdna),
            ("arquivo.txt", _read_23andme),
        ],
    )
    def test_discover_reader_success(self, filename, reader):
        snp_file = SNPFile(filename)
        assert snp_file._reader == reader

    @pytest.mark.parametrize("filename", ["arquivo.tsv", "arquivo", "arquivo.csv.gz"])
    def test_discover_reader_error(self, filename):
        pytest.raises(Exception, SNPFile, filename)

    def test_get_genotype_success(self, snp_file):
        snp_file = SNPFile(snp_file)
        assert snp_file.get_genotype("rs4312") == "AT"

    def test_get_genotype_non_existent(self, snp_file):
        snp_file = SNPFile(snp_file)
        pytest.raises(Exception, snp_file.get_genotype, "rs11111")

    def test_get_genotype_complementary(self, snp_file):
        snp_file = SNPFile(snp_file)
        assert snp_file.get_genotype("rs123", complementary=True) == "CC"


def test_read_vendor(snp_file):
    if snp_file.endswith(".csv"):
        data = _read_ftdna(snp_file)
    elif snp_file.endswith(".txt"):
        data = _read_23andme(snp_file)

    assert next(data) == {"rsid": "rs123", "chrom": "1", "pos": "12345", "result": "GG"}
    assert next(data) == {
        "rsid": "rs4312",
        "chrom": "2",
        "pos": "453231",
        "result": "AT",
    }
