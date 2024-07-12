import requests


class TestAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_methods(self):
        response = requests.get(
            url=f"{self.BASE_URL}/posts"
        )
        