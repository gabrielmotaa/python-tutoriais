from unittest.mock import patch, Mock

import pytest

from snps_util import get_rsid_info, get_maf_info


@patch('snps_util.ensembl.requests')
def test_get_rsid_info_success(requests_mock):
    my_mock = Mock()
    my_mock.status_code = 200
    requests_mock.get.return_value = my_mock

    get_rsid_info('rs123')

    requests_mock.get.assert_called_once()
    my_mock.json.assert_called_once()


@patch('snps_util.ensembl.requests')
def test_get_rsid_info_error(requests_mock):
    my_mock = Mock()
    my_mock.status_code = 400

    requests_mock.get.return_value = my_mock

    with pytest.raises(Exception):
        get_rsid_info('rs123')
        requests_mock.get.assert_called_once()


@patch('snps_util.ensembl.get_rsid_info')
def test_get_maf_info_success(rsid_info_mock):
    rsid_info_mock.return_value = {'MAF': 0.40, 'minor_allele': 'A'}

    maf, minor_allele = get_maf_info('rs123')

    rsid_info_mock.assert_called_once_with('rs123')

    assert maf == 0.40
    assert minor_allele == 'A'


@pytest.mark.parametrize("rsid,data", [
    ('rs123', {'MAF': 0.4}),
    ('rs123', {'minor_allele': 'T'}),
    ('rs123', {}),
])
def test_get_maf_info_error(rsid, data):
    with patch('snps_util.ensembl.get_rsid_info') as rsid_info_mock:
        rsid_info_mock.return_value = data
        pytest.raises(Exception, get_maf_info, rsid)