
# doit-graph

Generates a graph (using graphviz's dot) of [doit](http://pydoit.org) tasks.

Sample for [doit tutorial](http://pydoit.org/tutorial_1.html) tasks:

![Sample output](/tasks.png)


## install

pip install doit-graph


## usage

```
$ doit graph
$ dot -Tpng tasks.dot -o tasks.png
```

- By default sub-tasks are hidden. Use option `--show-subtasks` to display them.

- By default all tasks are included in graph.
  It is possible to specify which tasks should be included in the graph (note dependencies will be automatically included).

- To draw tasks in execution order (i.e. reverse of dependency direction), use option `--reverse`

```
$ doit graph --reverse
```

- To draw tasks from left-to-right instead of the default top-to-bottom, use option `--horizontal` or `-h`

```
$ doit graph --horizontal
```

### legend

![Legend](/legend.png)

- group-tasks have double bondary border in the node
- `task-dep` arrow have a solid head
- `setup-task` arrow have an empty head



### limitations

`calc_dep` and `delayed-tasks` are not supported.



## DEV notes

http://graphviz.org/doc/info/attrs.html
