import pytest


def test_positive(base_fixture):
    session_token = base_fixture.token_admin
    response = base_fixture.api.regions.get_configs_regions(session_token)

    check_resp = base_fixture.checkers.general.validate_json(response.json()["data"],
                                                             "schemas/regions.json")

    assert response.status_code == 200
    assert check_resp is True, "comment"

