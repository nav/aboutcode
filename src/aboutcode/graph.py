#!/usr/bin/env python

import uuid
from graphviz import Graph


def walk_directory_tree(dot, directory, parent=None):
    for subdir, children in directory.items():
        if subdir == '_':
            if children:
                dot.attr('node', shape='rectangle')
                node_text = ''
                for child in children:
                    node_text += f'<font color="blue">{child}</font><br/>\n'
                node_text = f'<{node_text}>'
                child_node_id = uuid.uuid4().hex
                dot.node(child_node_id, node_text)
                dot.edge(parent, child_node_id)
            continue

        node_id = uuid.uuid4().hex
        dot.attr('node', shape='ellipse')
        dot.node(node_id, subdir)
        if parent is not None:
            dot.edge(parent, node_id)
        if isinstance(children, dict):
            walk_directory_tree(dot, children, parent=node_id)


def generate_graph(directory_tree: dict) -> None:
    dot = Graph(
        'Directory Tree',
        filename='directory_tree',
        engine='dot',
        format='svg',
        #edge_attr={'dir': None}
    )

    walk_directory_tree(dot, directory_tree)
    dot.render()
