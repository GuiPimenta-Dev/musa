import pytest
import requests
from lambda_forge.constants import BASE_URL

@pytest.mark.integration(method="GET", endpoint="/musa")
def test_musa_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/musa")

    assert response.status_code == 200 
