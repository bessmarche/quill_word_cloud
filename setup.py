import io
from setuptools import setup
from setuptools.extension import Extension
import versioneer

with io.open('README.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(
    author="Andreas Mueller, adjusted for Quill project by Beatrice Marchegiani",
    author_email="Andreas: t3kcit+wordcloud@gmail.com Beatrice: beatrice.marchegiani@hertford.ox.ac.uk",
    name='wordcloud',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/amueller/word_cloud',
    description='A word cloud generator, based on Andreas Mueller original package (see url), tailored to meet the need to the Quill Project',
    long_description=readme,
    long_description_content_type='text/markdown; charset=UTF-8',
    license='MIT',
    install_requires=['numpy>=1.6.1', 'pillow', 'matplotlib'],
    ext_modules=[Extension("wordcloud.query_integral_image",
                           ["wordcloud/query_integral_image.c"])],
    entry_points={'console_scripts': ['wordcloud_cli=wordcloud.__main__:main']},
    packages=['wordcloud'],
    package_data={'wordcloud': ['stopwords', 'DroidSansMono.ttf']}
)
