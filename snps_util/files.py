import csv

from .helpers import complementary_strand


class SNPFile:
    def __init__(self, filename):
        self.filename = filename

    def get_genotype(self, rsid, complementary=False):
        result = None

        for data in _read_ftdna(self.filename):
            if rsid == data['rsid']:
                result = data['result']
                break

        if result is None:
            raise Exception(f"SNP {rsid} não encontrado.")

        if complementary:
            return complementary_strand(result)

        return result


def _read_ftdna(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                'rsid': row['RSID'],
                'chrom': row['CHROMOSOME'],
                'pos': row['POSITION'],
                'result': row['RESULT'],
            }
