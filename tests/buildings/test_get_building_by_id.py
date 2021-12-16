import pytest


def test_positive(base_fixture):
    session_token = base_fixture.token_admin
    house_id = base_fixture.configs.house_id

    response = base_fixture.api.buildings.get_building_by_id(session_token, house_id)
    check_resp = base_fixture.h

    assert response.status_code == 202
