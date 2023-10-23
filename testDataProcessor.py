import os
import json
import unittest
from dataProcessor import read_json_file
from dataProcessor import avgAgeCountry


class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        # Ajustar o número esperado de registros
        self.assertEqual(len(data), 1000)
        self.assertEqual(data[0]['name'], 'Danielle Collins')
        self.assertEqual(data[1]['age'], 54)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")


class TestAvgAgeCountry(unittest.TestCase):

    def test_avg_age_country(self):
        with open('users.json', 'r') as file:
            data = json.load(file)
        result = avgAgeCountry(data)
        self.assertEqual(result, {'DE': 38.42372881355932, 'AU': 40.090090090090094, 'US': 39.69064748201439, 'UK': 37.74166666666667,
                         'CA': 40.12408759124087, 'BR': 39.085470085470085, 'JP': 38.93043478260869, 'FR': 39.13986013986014})

    def test_avg_age_country_empty_data(self):
        data = []
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avg_age_country_missing_age(self):
        data = [
            {"name": "Alice", "country": "US"},
            {"name": "Lucas", "country": "US"},
        ]
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avg_age_country_missing_country(self):
        data = [
            {"name": "Alice", "age": 25},
            {"name": "Lucas", "age": 30},
        ]
        result = avgAgeCountry(data)
        self.assertEqual(result, {})

    def test_avg_age_country_with_data(self):
        data = [
            {"name": "Alice", "age": 25, "country": "US"},
            {"name": "Lucas", "age": 30, "country": "US"},
            {"name": "Guilherme", "age": 28, "country": "UK"},
        ]
        result = avgAgeCountry(data)
        self.assertEqual(result, {"US": 27.5, "UK": 28.0})

    def test_avg_age_country_age_transformation(self):
        data = [
            {"name": "Alice", "age": 36, "country": "US"},
            {"name": "Lucas", "age": 60, "country": "US"},
            {"name": "GUilherme", "age": 84, "country": "UK"},
        ]

        def age_in_months(age):
            return age * 12

        result = avgAgeCountry(data, age_transform=age_in_months)
        self.assertEqual(
            result, {"US": (36 * 12 + 60 * 12) / 2, "UK": 84 * 12})


if __name__ == '__main__':
    unittest.main()
