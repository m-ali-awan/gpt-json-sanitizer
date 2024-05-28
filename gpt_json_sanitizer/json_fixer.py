import json
import re

def fix_json_response(response: str) -> dict:
    """
    Fixes common JSON formatting issues in a string response.
    
    Args:
        response (str): The response string from ChatGPT.
        
    Returns:
        dict: The JSON-compatible dictionary.
    """
    # Attempt to parse the JSON without any modifications
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass  # If it fails, continue with the processing steps
    # Remove markdown JSON code fences and the `json` keyword
    response = re.sub(r'```json\n|```|json', '', response)
    
    # Replace non-standard quotes with standard double quotes
    response = response.replace('“', '"').replace('”', '"')
    
    # Strip leading and trailing whitespace
    response = response.strip()
    
    # Attempt to find JSON object or array within the string
    match = re.search(r'\{[\s\S]*\}|\[[\s\S]*\]', response)
    
    if match:
        cleaned_string = match.group(0)
    else:
        # If no JSON object or array is found, assume the whole response needs fixing
        cleaned_string = response
    
    # Count the number of opening and closing braces
    open_curly = cleaned_string.count('{')
    close_curly = cleaned_string.count('}')
    open_square = cleaned_string.count('[')
    close_square = cleaned_string.count(']')
    
    # Attempt to add enclosing brackets if missing
    if open_curly == 1 and close_curly == 0:
        cleaned_string += '}'
    elif close_curly == 1 and open_curly == 0:
        cleaned_string = '{' + cleaned_string
    elif open_square == 1 and close_square == 0:
        cleaned_string += ']'
    elif close_square == 1 and open_square == 0:
        cleaned_string = '[' + cleaned_string


    # Handle case where both opening and closing brackets are missing
    if open_curly == 0 and close_curly == 0 and open_square == 0 and close_square == 0:
        cleaned_string = '{' + cleaned_string + '}'
    
    # Attempt to fix common issues and parse the JSON
    try:
        #print(f"line 50: {cleaned_string}")
        try:
            return json.loads(cleaned_string)
        except json.JSONDecodeError:
            wrapped_string = f"[{cleaned_string}]"
            #print(f"Attempting to parse wrapped string: {wrapped_string}")
            return json.loads(wrapped_string)
    except json.JSONDecodeError:
        # Handle common issues
        cleaned_string = cleaned_string.replace("'", '"')  # Replace single quotes with double quotes
        cleaned_string = cleaned_string.replace("\n", " ")  # Remove newlines
        cleaned_string = cleaned_string.replace("\t", " ")  # Remove tabs

        # Print the cleaned string for debugging
        print(f"line 59: {cleaned_string}")

        try:
            try:
                return json.loads(cleaned_string)
            except json.JSONDecodeError:
                
                mod_inp = f"[{cleaned_string}]"
                #print(mod_inp)
                return json.loads(mod_inp)
        except json.JSONDecodeError:
            raise ValueError("Unable to fix JSON response")


