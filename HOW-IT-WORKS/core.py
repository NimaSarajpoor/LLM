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


class TokenTransform:
    def __init__(self, vocabulary, regex_tokenizer):
        """
        Instanciate an object from this class

        Parameters
        ----------
        vocabulary : dict
            A dictionary where each key is a unique token (e.g. word),
            and its corresponding value is a numerical value known as token id.

        regex_tokenizer : str
            A regex pattern that is used for splitting text during the tokenization process

        Returns
        -------
        None
        """
        self.str2int = vocabulary
        self.int2str = {token_id : token for (token, token_id) in vocabulary.items()}

        self.regex_tokenizer = regex_tokenizer

    
    def encode(self, text):
        tokens = tokenizer(text, self.regex_tokenizer)

        # let's assume `self.str2int` contains all the keys
        token_ids = [self.str2int[t] for t in tokens]
        
        return token_ids


    def decode(self, token_ids):
        # let's assume `self.int2str` contains all the keys
        text = " ".join(self.int2str[i] for i in token_ids)
        return text


class TokenTransformV2:
    def __init__(self, vocabulary, regex_tokenizer):
        """
        Instanciate an object from this class

        Parameters
        ----------
        vocabulary : dict
            A dictionary where each key is a unique token (e.g. word),
            and its corresponding value is a numerical value known as token id.

        regex_tokenizer : str
            A regex pattern that is used for splitting text during the tokenization process

        Returns
        -------
        None
        """
        self.UNKNOWN_KEYWORD = "<|unk|>"
        self.END_OF_TEXT = "<|endoftext|>" 
        self.regex_tokenizer = regex_tokenizer
        
        lst = list(vocabulary.keys())
        if self.UNKNOWN_KEYWORD not in lst:
            lst.append(self.UNKNOWN_KEYWORD)

        if self.END_OF_TEXT not in lst:
            lst.append(self.END_OF_TEXT)
        
        vocabulary = {
            s:i for (i, s) in enumerate(sorted(set(lst)))
        }
        self.str2int = vocabulary
        self.int2str = {token_id : token for (token, token_id) in vocabulary.items()}

    
    def encode(self, text):
        tokens = tokenizer(text, self.regex_tokenizer)

        # let's assume `self.str2int` contains all the keys

        uknown_id = self.str2int[self.UNKNOWN_KEYWORD]
        token_ids = [
            self.str2int.get(t, uknown_id) for t in tokens
        ]
        
        return token_ids


    def decode(self, token_ids):
        # let's assume `self.int2str` contains all the keys
        text = " ".join(self.int2str[i] for i in token_ids)
        return text