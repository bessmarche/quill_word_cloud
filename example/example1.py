#!/usr/bin/env python3
# Tests for Bess' quill project

# Import the custom quill module
from wordcloud import made_for_quill

# Open the output html file
import subprocess

# On first run need to download resources from nltk
# You may need to import nltk
import nltk
# For example select popular; click download; then once complete exit
#nltk.download('punkt')
# remember if using a custom download dir to add the download path:
#nltk.data.path.append('.../.../nltk_data')
nltk.data.path.append('/home/jamesfallon/Packages/nltk_data')

# Enter test text eg. Lorem Ipsum
test_list = ['test Lorem ipsum dolor sit amet', 
             'consectetur adipiscing elit',
             'test Nulla lectus ligula', 
             'imperdiet at porttitor quis',
             'smth commodo eget tortor',  
             'Orci varius natoque penatibus et magnis dis parturient montes'] 

# Create the word cloud
cloud = made_for_quill(test_list)

# Save output to an html file
fname = 'lorem_ipsum.html'
with open(fname, 'w') as f:
    f.write(cloud)

# Open html file in browser
# try linux/mac open commands. 
# sorry don't know how to do this on windows, maybe you can't ;(
open_commands = {'linux': 'xdg-open',
                 'mac':   'open'}
for command in open_commands.values():
    try:
        subprocess.run([command, fname], check=True)
        break
    except FileNotFoundError:
        pass
else:
    print("Couldn't automatically open html. Please open {}".format(fname)
         + "in your web browser to view the results :)")
