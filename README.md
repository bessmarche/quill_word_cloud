# quill_word_cloud
Based on the python wordcloud module (to be found at: https://github.com/amueller/word_cloud) customized for use by the Quill Project.

Quill specific feautures include:

- .to_html() method for instances of the class WordCloud that convert a WordCloud object in a html string ready for use in the website

- prioritize_NE() method and .priority_NE parameter for WordCloud objects, allowing to prioritize Named Entities (as identified by nltk) in the greation of the wordcloud, by increasing their detected frequency by a user-choosen factor. 

- improved .to_svg() method that can handle a larger variery of fonts

- make_for_quill() a method that given a list of strings outputs a wordcloud in the form of an html string to suit the requirements fothe Quill Project topic overview (canvas dimension, font, number of words, coulor_scheme, min and max font size, the amount of priority given to Named Entities). All of these requrements can be altered in the model_for_quill.py file 


