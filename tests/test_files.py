import os
import tempfile

import pytest

from snps_util import SNPFile
from snps_util.files import _read_ftdna, _read_23andme


class TestSNPFile:
    """Suíte de testes específicos para o SNPFile."""

    @pytest.mark.parametrize("filename,reader", [
        ('arquivo.csv', _read_ftdna),
        ('arquivo.txt', _read_23andme),
    ])
    def test_discover_reader_success(self, filename, reader):
        snp_file = SNPFile(filename)
        assert snp_file._reader == reader

    @pytest.mark.parametrize("filename", ['arquivo.tsv', 'arquivo', 'arquivo.csv.gz'])
    def test_discover_reader_error(self, filename):
        pytest.raises(Exception, SNPFile, filename)

    def test_get_genotype_success_ftdna(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp(suffix='.csv')
        with open(temp_csv, 'w') as f:
            f.writelines([
                "RSID,CHROMOSOME,POSITION,RESULT\n",
                "rs123,1,12345,GG\n",
                "rs4312,2,453231,AT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            assert snp_file.get_genotype('rs4312') == 'AT'
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_success_23andme(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp(suffix='.txt')
        with open(temp_csv, 'w') as f:
            f.writelines([
                "#rsid\tchromosome\tposition\tgenotype\n",
                "rs123\t1\t12345\tGG\n",
                "rs4312\t2\t453231\tAT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            assert snp_file.get_genotype('rs4312') == 'AT'
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_non_existent_ftdna(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp(suffix='.csv')
        with open(temp_csv, 'w') as f:
            f.writelines([
                "RSID,CHROMOSOME,POSITION,RESULT\n",
                "rs123,1,12345,GG\n",
                "rs4312,2,453231,AT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            pytest.raises(Exception, snp_file.get_genotype, 'rs11111')
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_non_existent_23andme(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp(suffix='.txt')
        with open(temp_csv, 'w') as f:
            f.writelines([
                "#rsid\tchromosome\tposition\tgenotype\n",
                "rs123\t1\t12345\tGG\n",
                "rs4312\t2\t453231\tAT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            pytest.raises(Exception, snp_file.get_genotype, 'rs11111')
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_complementary_ftdna(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp(suffix='.csv')
        with open(temp_csv, 'w') as f:
            f.writelines([
                "RSID,CHROMOSOME,POSITION,RESULT\n",
                "rs123,1,12345,GG\n",
                "rs4312,2,453231,AT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            assert snp_file.get_genotype('rs123', complementary=True) == 'CC'
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_complementary_23andme(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp(suffix='.txt')
        with open(temp_csv, 'w') as f:
            f.writelines([
                "#rsid\tchromosome\tposition\tgenotype\n",
                "rs123\t1\t12345\tGG\n",
                "rs4312\t2\t453231\tAT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            assert snp_file.get_genotype('rs123', complementary=True) == 'CC'
        finally:
            os.unlink(temp_csv)


def test_read_ftdna():
    # criar arquivo temporário como csv ThermoFisher
    _, temp_csv = tempfile.mkstemp(suffix='.csv')
    with open(temp_csv, 'w') as f:
        f.writelines([
            "RSID,CHROMOSOME,POSITION,RESULT\n",
            "rs123,1,12345,GG\n",
            "rs4312,2,453231,AT\n",
        ])

    data = _read_ftdna(temp_csv)

    try:
        assert next(data) == {'rsid': 'rs123', 'chrom': '1', 'pos': '12345', 'result': 'GG'}
        assert next(data) == {'rsid': 'rs4312', 'chrom': '2', 'pos': '453231', 'result': 'AT'}
    finally:
        os.unlink(temp_csv)