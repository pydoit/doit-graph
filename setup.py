from setuptools import setup

setup(
    name = 'doit-graph',
    description = "doit cmd plugin: create task's dependency-graph image",
    version = '0.1.0',
    license = 'MIT',
    author = 'Eduardo Naufel Schettino',
    url = 'http://github.com/pydoit/doit-graph',
    py_modules=['doit_graph'],
    entry_points = {
        'doit.COMMAND': [
            'graph = doit_graph:GraphCmd'
        ]
    },
)
