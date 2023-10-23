import os
import unittest
from dataProcessor import read_json_file


class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        # Ajustar o número esperado de registros
        self.assertEqual(len(data), 10)
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['age'], 25)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")


if __name__ == '__main__':
    unittest.main()
