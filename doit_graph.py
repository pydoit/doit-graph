import pygraphviz
from doit.cmd_base import DoitCmdBase

class GraphCmd(DoitCmdBase):
    doc_purpose = "create task's dependency-graph image"

    cmd_options = tuple()

    def _execute(self):
        tasks = dict([(t.name, t) for t in self.task_list])

        graph = pygraphviz.AGraph(strict=False, directed=True)
        graph.node_attr['color'] = 'lightblue2'
        graph.node_attr['style'] = 'filled'
        for task in tasks.values():
            graph.add_node(task.name)
            for sink in task.task_dep:
                graph.add_edge(task.name, sink)
            for sink in task.setup_tasks:
                graph.add_edge(task.name, sink)
        graph.write('tasks.dot')

