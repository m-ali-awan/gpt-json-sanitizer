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

if __name__ == '__main__':
    unittest.main()
