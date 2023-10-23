import json


def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")


def avgAgeCountry(data, age_transform=None):
    country_ages = {}
    for person in data:
        country = person.get('country')
        age = person.get('age')
        if country is not None and age is not None:
            if age_transform:
                age = age_transform(age)
            if country in country_ages:
                country_ages[country].append(age)
            else:
                country_ages[country] = [age]

    avg_ages = {}
    for country, ages in country_ages.items():
        avg_ages[country] = sum(ages) / len(ages)

    return avg_ages
