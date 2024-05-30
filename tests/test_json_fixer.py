import unittest
from gpt_json_sanitizer.json_fixer import fix_json_response

class TestJsonFixer(unittest.TestCase):
    def test_fix_simple_json(self):
        response = '''{"key": "value"}'''
        expected = {"key": "value"}
        self.assertEqual(fix_json_response(response), expected)

    def test_fix_single_quotes(self):
        response = '''{'key': 'value'}'''
        expected = {"key": "value"}
        self.assertEqual(fix_json_response(response), expected)

    def test_fix_missing_brackets(self):
        response = ''''key': 'value' '''
        expected = {"key": "value"}
        self.assertEqual(fix_json_response(response), expected)

    def test_fix_newlines_and_tabs(self):
        response = '''{
            'key': 'value'\n\t}'''
        expected = {"key": "value"}
        self.assertEqual(fix_json_response(response), expected)

    def test_valid_json_array(self):
        response = '''[{"key": "value"}, {"key2": "value2"}]'''
        expected = [{"key": "value"}, {"key2": "value2"}]
        self.assertEqual(fix_json_response(response), expected)

    def test_wrap_single_object(self):
        response = '''{"key": "value"'''
        expected = {"key": "value"}
        self.assertEqual(fix_json_response(response), expected)

    def test_wrap_multiple_objects(self):
        response = '''{"key": "value"}, {"key2": "value2"}'''
        expected = [{"key": "value"}, {"key2": "value2"}]
        self.assertEqual(fix_json_response(response), expected)

    def test_complex_case(self):
        response = '''```json{"key": "value"```'''
        expected = {"key": "value"}
        self.assertEqual(fix_json_response(response), expected)

    def test_malformed_json(self):
        response = '''{
            "key1": "value1",
            "key2": "value2"
            },
            {
            "key3": "value3",
            "key4": "value4"
            }'''
        expected = [{'key1': 'value1', 'key2': 'value2'},
                     {'key3': 'value3', 'key4': 'value4'}]
        self.assertEqual(fix_json_response(response), expected)

    def test_embedded_json(self):
        response = '''```json{"embedded": {"key": "value"}}```'''
        expected = {'embedded': {'key': 'value'}}
        self.assertEqual(fix_json_response(response), expected)

    def test_on_real_example(self) -> None:
        """Tests fix on real example response.

    
        """

        response = 'Here is the recipe for Apple Pancakes in the required JSON format:\n\n```json\n{\n  "name": "Apple Pancakes",\n  "serving_size": 1,\n  "ingredients": [\n    {\n      "id": 1,\n      "name": "flour",\n      "quantity": 1,\n      "unit": "cup"\n    },\n    {\n      "id": 2,\n      "name": "apple",\n      "quantity": 1,\n      "unit": "large",\n      "notes": "peeled"\n    },\n    {\n      "id": 3,\n      "name": "sugar",\n      "quantity": 1,\n      "unit": "tablespoon"\n    },\n    {\n      "id": 4,\n      "name": "cinnamon",\n      "quantity": 1,\n      "unit": "tablespoon"\n    },\n    {\n      "id": 5,\n      "name": "baking powder",\n      "quantity": 0.5,\n      "unit": "teaspoon"\n    },\n    {\n      "id": 6,\n      "name": "vanilla extract",\n      "quantity": 1,\n      "unit": "teaspoon"\n    },\n    {\n      "id": 7,\n      "name": "milk",\n      "quantity": 2/3,\n      "unit": "cup"\n    },\n    {\n      "id": 8,\n      "name": "egg",\n      "quantity": 1,\n      "unit": "unit"\n    },\n    {\n      "id": 9,\n      "name": "butter",\n      "quantity": 1,\n      "unit": "tablespoon"\n    }\n  ],\n  "steps": [\n    {\n      "number": 1,\n      "description": "In a medium bowl, combine flour, sugar, cinnamon, and baking powder."\n    },\n    {\n      "number": 2,\n      "description": "Separate the egg yolk and egg white.",\n      "preparation_time": 5,\n      "used_ingredients": [8]\n    },\n    {\n      "number": 3,\n      "description": "Whisk the egg white until foamy.",\n      "preparation_time": 5,\n      "used_ingredients": [8]\n    },\n    {\n      "number": 4,\n      "description": "Slice the peeled apple into thin strips or grate the apple.",\n      "preparation_time": 5,\n      "used_ingredients": [2]\n    },\n    {\n      "number": 5,\n      "description": "Combine dry ingredients, apple, vanilla extract, egg white, and milk into a homogenous batter.",\n      "preparation_time": 5,\n      "used_ingredients": [1, 3, 4, 6, 7, 8, 2]\n    },\n    {\n      "number": 6,\n      "description": "To a large pan, add butter. Add the batter (about 3 tbsp per pancake) and cook for 2 min per side on medium-high heat.",\n      "cooking_time": 10,\n      "used_ingredients": [9, 5]\n    }\n  ],\n  "total_preparation_time": {\n    "min": 25,\n    "max": 25\n  },\n  "total_cooking_time": {\n    "min": 10,\n    "max": 10\n  },\n  "total_waiting_time": {\n    "min": 0,\n    "max": 0\n  },\n  "comments": [],\n  "inference_assumptions": [\n    "Assumed that the recipe serves one person",\n    "Assumed that the `large` apple refers to a standard-sized apple"\n  ]\n}\n```\nThe recipe makes one serving of Apple Pancakes and takes approximately 25 minutes to prepare and 10 minutes to cook.'
        assert isinstance(fix_json_response(response), dict)

if __name__ == '__main__':
    unittest.main()
