import pygraphviz

from doit.cmd_base import DoitCmdBase
from doit.control import TaskControl




class GraphCmd(DoitCmdBase):
    doc_purpose = "create task's dependency-graph image"

    cmd_options = tuple()

    def _execute(self):
        control = TaskControl(self.task_list)

        graph = pygraphviz.AGraph(strict=False, directed=True)
        graph.node_attr['color'] = 'lightblue2'
        graph.node_attr['style'] = 'filled'
        for task in control.tasks.values():
            # add nodes
            node_attrs = {}
            if task.has_subtask:
                node_attrs['peripheries'] = '2'
            graph.add_node(task.name, **node_attrs)

            # add edges
            for sink in task.task_dep:
                graph.add_edge(task.name, sink)
            for sink in task.setup_tasks:
                graph.add_edge(task.name, sink)

        graph.write('tasks.dot')

