from .wordcloud import (WordCloud, STOPWORDS, random_color_func,
                        get_single_color_func)
from .color_from_image import ImageColorGenerator
from .model_for_quill import  made_for_quill

__all__ = ['WordCloud', 'STOPWORDS', 'random_color_func',
           'get_single_color_func', 'ImageColorGenerator', 'made_for_quill',
           '__version__']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
