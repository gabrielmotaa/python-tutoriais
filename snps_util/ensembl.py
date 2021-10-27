import requests

URL = "https://rest.ensembl.org/variation/human/{rsid}?content-type=application/json"


def get_rsid_info(rsid):
    """Faz uma requição ao Ensembl REST API e retorna informações sobre o rsID."""
    request = requests.get(URL.format(rsid=rsid))

    if request.status_code != 200:
        raise Exception(f"Erro na requisição ao Ensembl: Status {request.status_code}")

    return request.json()


def get_maf_info(rsid):
    """Retorna o valor do MAF e o alelo minor do rsID informado do Ensembl REST API."""
    data = get_rsid_info(rsid)

    maf = data.get("MAF")
    minor_allele = data.get("minor_allele")

    if maf is None or minor_allele is None:
        raise Exception("Informações de MAF incompletas")

    return maf, minor_allele
