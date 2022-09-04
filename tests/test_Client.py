import unittest

from clients.Client import Client
from tests.test_data import ID_TYPE_LIST, SUBSET_LIST


class TestClient(unittest.TestCase):
    def test_get_json(self):
        self.assertRaises(Exception, Client.get_json)
        self.assertRaises(Exception, Client.get_json, url="invalid_url")
        self.assertRaises(Exception, Client.get_json, headers="invalid_header")
        self.assertRaises(Exception, Client.get_json, "invalid_url", "invalid_header")
        self.assertRaises(Exception, Client.get_json, "invalid_url", {"header": "is_ok"})

        response = Client.get_json('https://api.coingecko.com/api/v3/ping')

    def test_get_asset_map(self):
        self.assertRaises(Exception, Client.get_asset_map)
        self.assertRaises(Exception, Client.get_asset_map, ["invalid_argument_type"])
        self.assertRaises(Exception, Client.get_asset_map, "invalid_id")
        
        for valid_id in ID_TYPE_LIST:
            self.assertRaises(Exception, Client.get_asset_map, valid_id, ["invalid_subset_id_type"])
            self.assertRaises(Exception, Client.get_asset_map, valid_id, "invalid_subset_id")

            for subset_id in SUBSET_LIST:
                self.assertIsInstance(Client.get_asset_map(valid_id, subset_id), dict)


if __name__ == '__main__':
    unittest.main()
