import random
import requests
import pytest
from hamcrest import *

base_url = "https://restful-booker.herokuapp.com"


class TestSampleExternal:
    """ Docs: https://restful-booker.herokuapp.com/apidoc/index.html """

    def test_get_all_booking_ids(self):
        res = requests.get(url=f"{base_url}/booking")
        assert_that(res.json(), has_length(greater_than(0)))

    def test_get_booking_by_id(self, get_booking_id):
        res = requests.get(url=f"{base_url}/booking/{get_booking_id}")
        assert_that(res.json(), has_entries(
            firstname=is_(str),
            lastname=is_(str),
            totalprice=is_(int),
            depositpaid=is_(bool),
            bookingdates=has_entries(checkin=is_(str), checkout=is_(str)),
            additionalneeds=is_(str),
        ))


@pytest.fixture
def get_booking_id():
    res = requests.get(url=f"{base_url}/booking")
    if not res.json():
        raise ValueError
    booking_id = random.choice(res.json())["bookingid"]
    print("test id", booking_id)
    return booking_id
