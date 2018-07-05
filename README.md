
# doit-graph

Generates a graph (using graphviz's dot) of tasks.

WIP: not released yet!


## install

pip install doit-graph


## usage

```
$ doit graph
$ dot -Tpng tasks.dot -o tasks.png
```


## DEV notes

http://graphviz.org/doc/info/attrs.html


## TODO

### 0.1

- pos args: show only specified tasks
- graph legend

### 0.x

- include status
- option include file_dep, targets
- calc_dep
- delayed_creation
