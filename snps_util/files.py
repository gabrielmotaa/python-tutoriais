import csv
from pathlib import Path

from .helpers import complementary_strand


def _read_ftdna(filename):
    """Gerador que retorna linhas de um arquivo FTDNA"""
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {
                "rsid": row["RSID"],
                "chrom": row["CHROMOSOME"],
                "pos": row["POSITION"],
                "result": row["RESULT"],
            }


def _read_23andme(filename):
    """Gerador que retorna linhas de um arquivo 23andme"""
    with open(filename) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0].startswith("#"):
                continue
            yield {
                "rsid": row[0],
                "chrom": row[1],
                "pos": row[2],
                "result": row[3],
            }


# Podemos adicionar novos readers sem ter que mexer em SNPFile
_readers = {
    ".csv": _read_ftdna,
    ".txt": _read_23andme,
}


class SNPFile:
    """Processa um arquivo de SNPs e retorna informações."""

    def __init__(self, filename):
        self.filename = filename
        self._reader = self._discover_vendor()

    def _discover_vendor(self):
        """Descobre o vendedor a partir da extensão do arquivo."""
        extension = Path(self.filename).suffix
        reader = _readers.get(extension)
        if reader is None:
            raise Exception(f"Arquivo {self.filename} desconhecido.")

        return reader

    def get_genotype(self, rsid, complementary=False):
        """Retorna o genótipo de um rsid que exista no arquivo.

        É possível retornar na fita complementar. Caso não encontre
        um genótipo levanta uma exceção.
        """
        result = None

        for data in self._reader(self.filename):
            if rsid == data["rsid"]:
                result = data["result"]
                break

        if result is None:
            raise Exception(f"SNP {rsid} não encontrado.")

        if complementary:
            return complementary_strand(result)

        return result
