import os
import tempfile

import pytest

from snps_util import SNPFile


class TestSNPFile:
    """Suíte de testes específicos para o SNPFile."""

    def test_get_genotype_success(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp()
        with open(temp_csv, 'w') as f:
            f.writelines([
                "RSID,CHROMSOME,POSITION,RESULT\n",
                "rs123,1,12345,GG\n",
                "rs4312,2,453231,AT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            assert snp_file.get_genotype('rs4312') == 'AT'
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_non_existent(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp()
        with open(temp_csv, 'w') as f:
            f.writelines([
                "RSID,CHROMSOME,POSITION,RESULT\n",
                "rs123,1,12345,GG\n",
                "rs4312,2,453231,AT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            pytest.raises(Exception, snp_file.get_genotype, 'rs11111')
        finally:
            os.unlink(temp_csv)

    def test_get_genotype_complementary(self):
        # criar arquivo temporário como csv ThermoFisher
        _, temp_csv = tempfile.mkstemp()
        with open(temp_csv, 'w') as f:
            f.writelines([
                "RSID,CHROMSOME,POSITION,RESULT\n",
                "rs123,1,12345,GG\n",
                "rs4312,2,453231,AT\n",
            ])

        snp_file = SNPFile(temp_csv)

        try:
            assert snp_file.get_genotype('rs123', complementary=True) == 'CC'
        finally:
            os.unlink(temp_csv)
