"""doit-graph

The MIT License

Copyright (c) 2018-present Eduardo Naufel Schettino & contributors
"""

__version__ = (0, 3, 0)

from collections import deque

import pygraphviz

from doit.cmd_base import DoitCmdBase
from doit.control import TaskControl


opt_subtasks = {
    'name': 'subtasks',
    'short': '',
    'long': 'show-subtasks',
    'type': bool,
    'default': False,
    'help': 'include subtasks in graph',
}

opt_reverse = {
    'name': 'reverse',
    'short': '',
    'long': 'reverse',
    'type': bool,
    'default': False,
    'help': 'draw edge in execution order, i.e. the reverse of dependency direction'
}

opt_horizontal = {
    'name': 'horizontal',
    'short': 'h',
    'long': 'horizontal',
    'type': bool,
    'default': False,
    'help': 'draw graph in left-right mode, i.e. add rankdir=LR to digraph output'
}

opt_outfile = {
    'name': 'outfile',
    'short': 'o',
    'long': 'output',
    'type': str,
    'default': None, # actually default dependends parameters
    'help': 'name of generated dot-file',
}



class GraphCmd(DoitCmdBase):
    name = 'graph'
    doc_purpose = "create task's dependency-graph (in dot file format)"
    doc_description = """Creates a DAG (directly acyclic graph) representation of tasks in graphviz's **dot** format (http://graphviz.org).

**dot** files can be convert to images with i.e.

$ dot -Tpng tasks.dot -o tasks.png

Legend:
  - group-tasks have double boundary border in the node
  - `task-dep` arrow have a solid head
  - `setup-task` arrow have an empty head

Website/docs: https://github.com/pydoit/doit-graph
    """
    doc_usage = "[TASK ...]"

    cmd_options = (opt_subtasks, opt_outfile, opt_reverse, opt_horizontal)


    def node(self, task_name):
        """get graph node that should represent for task_name

        :param task_name:
        """
        if self.subtasks:
            return task_name
        task = self.tasks[task_name]
        return task.subtask_of or task_name


    def add_edge(self, src_name, sink_name, arrowhead):
        source = self.node(src_name)
        sink = self.node(sink_name)
        if source != sink and (source, sink) not in self._edges:
            self._edges.add((source, sink))
            self.graph.add_edge(source, sink, arrowhead=arrowhead)


    def _execute(self, subtasks, reverse, horizontal, outfile, pos_args=None):
        # init
        control = TaskControl(self.task_list)
        self.tasks = control.tasks
        self.subtasks = subtasks
        self._edges = set() # used to avoid adding same edge twice

        # create graph
        self.graph = pygraphviz.AGraph(strict=False, directed=True)
        self.graph.node_attr['color'] = 'lightblue2'
        self.graph.node_attr['style'] = 'filled'

        if (horizontal):
            self.graph.graph_attr.update(rankdir='LR')

        # populate graph
        processed = set() # str - task name
        if pos_args:
            to_process = deque(pos_args)
        else:
            to_process = deque(control.tasks.keys())

        while to_process:
            task = control.tasks[to_process.popleft()]
            if task.name in processed:
                continue
            processed.add(task.name)

            # add nodes
            node_attrs = {}
            if task.has_subtask:
                node_attrs['peripheries'] = '2'
            if (not task.subtask_of) or subtasks:
                self.graph.add_node(task.name, **node_attrs)

            # add edges
            for sink_name in task.setup_tasks:
                self.add_edge(task.name, sink_name, arrowhead='empty')
                if sink_name not in processed:
                    to_process.append(sink_name)
            for sink_name in task.task_dep:
                self.add_edge(task.name, sink_name, arrowhead='')
                if sink_name not in processed:
                    to_process.append(sink_name)

        if not outfile:
            name = pos_args[0] if len(pos_args)==1 else 'tasks'
            outfile = '{}.dot'.format(name)
        print('Generated file: {}'.format(outfile))
        if (reverse):
            self.graph.reverse().write(outfile)
        else:
            self.graph.write(outfile)

