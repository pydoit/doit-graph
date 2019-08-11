from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'doit-graph',
    description = "doit cmd plugin: create task's dependency-graph image",
    version = '0.3.0',
    license = 'MIT',
    author = 'Eduardo Naufel Schettino',
    url = 'http://github.com/pydoit/doit-graph',
    long_description=long_description,
    long_description_content_type="text/markdown",

    py_modules=['doit_graph'],
    install_requires = ['doit', 'pygraphviz'],
    entry_points = {
        'doit.COMMAND': [
            'graph = doit_graph:GraphCmd'
        ]
    },

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
    ),
    keywords = "doit graph graphviz",
)
