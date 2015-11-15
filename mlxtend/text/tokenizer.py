"""
Functions to tokenize text.

"""

# mlxtend
# Author:
#        Sebastian Raschka

import re

def tokenizer_words_and_emoticons(text):
    """Funtion that returns lowercase words and emoticons from text

    Example:
    >>> tokenizer_words_and_emoticons('</a>This :) is :( a test :-)!')
    ['this', 'is', 'a', 'test', ':)', ':(', ':-)']
    """
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons)
    return text.split()


def tokenizer_emoticons(text):
    """Funtion that returns emoticons from text

    Example:
    >>> tokenizer_emoticons('</a>This :) is :( a test :-)!')
    [':)', ':(', ':-)']
    """
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    return emoticons