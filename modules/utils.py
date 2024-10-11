def load_environment_variables(dotenv_path):
    """
    Load environment variables from a .env file and return the value of 'CODE_CMD_PATH'.

    Args:
        dotenv_path (str): The path to the .env file.

    Returns:
        str: The value of the 'CODE_CMD_PATH' environment variable, or None if it is not set.
    """
    import os
    from dotenv import load_dotenv
    load_dotenv(dotenv_path)
    return os.getenv('CODE_CMD_PATH')

def get_installed_extensions(code_cmd_path):
    """
    Retrieves a list of installed extensions for Visual Studio Code.

    Args:
        code_cmd_path (str): The path to the Visual Studio Code executable. store on .env file

    Returns:
        list: A list of installed extension identifiers as strings.
    """
    import subprocess
    result = subprocess.run([code_cmd_path, '--list-extensions'], capture_output=True, text=True)
    return result.stdout.splitlines()

def extract_xpath(xpath, url):
    """
    Extracts content from a given URL using an XPath expression.
    Args:
        xpath (str): The XPath expression to locate the desired content.
        url (str): The URL of the webpage to extract content from.
    Returns:
        str or None: The extracted content as a string if successful, 
                     or None if an error occurs (e.g., network issues, 
                     invalid XPath, or content not found).
    """
    import requests
    from lxml import html
    

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        tree = html.fromstring(response.content)
        content = tree.xpath(xpath)[0].text
        return content
    except (requests.exceptions.RequestException, IndexError):
        return None

def generate_extension_data(dotenv_path, extensions):
    """
    Generates a DataFrame containing extension names, identifiers, and URLs based on the provided extensions list.
    This function loads environment variables from a .env file specified by `dotenv_path`, retrieves the XPATH 
    environment variable, and uses it to extract extension names from generated URLs.
    Args:
        dotenv_path (str): The path to the .env file containing environment variables.
        extensions (list of str): A list of extension identifiers.
    Returns:
        pandas.DataFrame: A DataFrame with columns 'extension name', 'identifier', and 'url'.
    Raises:
        ValueError: If the XPATH environment variable is not set in the .env file.
    """
    import pandas as pd
    import os
    from dotenv import load_dotenv
    
    load_dotenv(dotenv_path)
    xpath = os.getenv('XPATH')

    if not xpath:
        raise ValueError("XPATH environment variable not set in the .env file")
    generated_url = ['https://marketplace.visualstudio.com/items?itemName=' + ext for ext in extensions]
    extension_names = [extract_xpath(xpath, u) for u in generated_url]
    return pd.DataFrame({
        'extension name': extension_names,
        'identifier': extensions,
        'url': generated_url
    })
