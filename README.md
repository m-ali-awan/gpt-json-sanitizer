# GPT JSON Sanitizer

A package to fix JSON responses from ChatGPT. 
Sometimes getting valid json responses from OpenAI becomes very hard, and we get broken responses eg: missing brackets. Adding extra words like ```json etc.
Here, I am trying to handle such cases by post-processing.  All the cases which we are handling now can be found in `tests`, but I know there can be more. So let me know in issues, and we can extend it further. If you find this helpful, leave a star on GitHub so I know it is useful :)

## Installation

Since the package is minimal, you can directly use the provided `json_fixer.py` module in your project.

## Usage

### Note

> To use this, it is required to instruct OpenAI models to respond in JSON format. You can do this by explicitly asking the model to format its responses as JSON dictionaries. While it is not necessary to use the `response_type:"json"` parameter, doing so will help ensure more consistent and predictable JSON responses.

> And we have to pass final response string from Openai to this: 
`response['choices'][0]['message']['content']`


### Import the Function
First, ensure you have the `json_fixer.py` file in your project. Then import the `fix_json_response` function:







```python
from json_fixer import fix_json_response

response = '''{"key": "value"}'''
print(fix_json_response(response))
# Output: {'key': 'value'}

# missing brackets
response = ''''key': 'value' '''
print(fix_json_response(response))
# Output: {'key': 'value'}

# Wrap Single Object
response = '''{"key": "value"'''
print(fix_json_response(response))
# Output: {'key': 'value'}


# malformed json,
response = '''{
    "key1": "value1",
    "key2": "value2"
    },
    {
    "key3": "value3",
    "key4": "value4"
    }'''
print(fix_json_response(response))
# Output: [{'key1': 'value1', 'key2': 'value2'}, {'key3': 'value3', 'key4': 'value4'}]
