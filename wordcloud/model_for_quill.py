import os
from .wordcloud import WordCloud

# general variables to fulfill the requirement for the final product on the quill website.
# Put here for convinient future editing. More parameter can be customized: see parameters for WordCloud

canvas_color = "white"
canvas_height = 749
canvas_width = 1123
font = 'Impact.ttf'
min_font_size = 30
max_words = 100
priority_factor_NE = 2


def made_for_quill(text):
    """
    to produce the wordcloud as a matplotlib graph use the following code snippet:

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


    :param text:[str] = list of strings to take into consideration when building the wordcloud.
           NOTE: the  text is assumed not to contain any ALL CAPS passages.
    :return: the HTML string for the wordcloud

    """
    # set the font for the wordcloud.
    # !NOTE! Check that the font is compatible with the svg converter. Example of supported fonts are arial and impact
    FILE = os.path.dirname(__file__)
    FONT_PATH = os.environ.get('FONT_PATH', os.path.join(FILE, font))

    comment_words = ' '

    # iterate through the list of texts to get a string of all the words
    for val in text:

       # typecaste each val to string
       val = str(val)

       # split the value
       # TODO find a way to take into account more compound words when doing tokenization
       tokens = val.split()

       # Converts tokens at the beginning of a phrase into lowercase, Named Entities retain the uppercase.
       # FIXME: ATM a string like "Hello. George" is made into "hello. george" rather than "hello. George"
       for i in range(len(tokens)):
           if i == 0:
               tokens[i] = tokens[i].lower()
           elif tokens[i - 1][-1] in ['.', '!', '...', '?', ';', '"']:
               tokens[i] = tokens[i].lower()


       # add the new words to comment_words
       for words in tokens:
           comment_words = comment_words + words + ' '

    # create the wordcloud object
    wordcloud = WordCloud(font_path=FONT_PATH,
                          width=canvas_width, height=canvas_height,
                          prefer_horizontal=1,
                          background_color= canvas_color,
                          max_words=max_words,
                          min_font_size= min_font_size,
                          priority_NE = priority_factor_NE).generate(comment_words)

    # convert the wordcloud in a html string
    return (wordcloud.to_html())

