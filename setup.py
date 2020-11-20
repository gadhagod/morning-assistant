import setuptools

setuptools.setup(
    name='morning-assistant',
    version='0.1',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='Have a virtual assistant deliver you local weather and world news on demand!',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://gadhagod.github.io/morning-assistant',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'click',
        'bbc-feeds',
        'gTTS'
    ],
    scripts=[
        './assistant',
        './assistant.py'
    ],
    python_requires='>=3.6'
)