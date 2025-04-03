import re
import urllib


def download_textfile_from_url(url, file_path):  
    """
    Download file from url, and save it in the `file_path`

    Parameters
    ----------
    url : str
        The url pointing to the text file of interest

    file_path : str
        The path in which the file is going to be saved.

    Returns
    -------
    None
    """
    if not file_path.endswith('.txt'):
        msg = (
            "This function is for downloading text data only. "
            + f"Please make sure the `file_path = {file_path}` "
            + "ends with the correct format `.txt`"
        )
        raise ValueError(msg)
    urllib.request.urlretrieve(url, file_path)

    return


def read_file(file_path):
    """
    Read file in file_path, and returns its content

    Parameters
    ----------
    file_path : str
        The path pointing to the location of the file of interest

    Returns
    -------
    out : str
        The content of the file 
    """
    with open(file_path, "r", encoding="utf-8") as f:
        out = f.read()

    return out


def tokenizer(raw_text, regex_pattern, remove_white_spaces=True):
    """
    Tokenize a `raw_text` by splitting it according to 
    the provided regex_pattern

    Parameters
    ----------
    raw_text : str
        A string (of words)

    regex_pattern : str
        The regex pattern based on which the `raw_text`
        will be splitted

    remove_white_spaces : bool, default True
        A boolean value indicating whether the white spaces
        should be removed from the list of tokens

    Returns
    -------
    tokens : list
        A list of token
    """
    tokens = re.split(regex_pattern, raw_text)
    if remove_white_spaces:
        tokens = [x for x in tokens if x.strip() != ""]

    return tokens
    