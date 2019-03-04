#!/usr/bin/env python

import os


def get_file_contents(filename: str) -> bytes:
    """Return contents of a file
    """
    with open(filename) as fd:
        return fd.read()


def is_python_file(filename: str) -> bool:
    """Return whether a file is a Python file or not
    """
    return filename.endswith('.py')


def recursively_generate_directory_tree(directory: str) -> dict:
    """Return a dict of recursively generated directory tree
    """
    tree = {}
    common_path = os.path.dirname(directory)
    exclude = [
        '.git',
        '.pycache',
        '.pytest_cache',
        'migrations',
        '__pycache__',
        'node_modules',
    ]
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude]

        _absdir = os.path.dirname(root)
        _root = os.path.basename(root)
        _diff = _absdir.replace(common_path, '').lstrip('/')

        branch = tree
        for nested_path in _diff.split('/'):
            if nested_path:
                branch = branch.setdefault(nested_path, {})
        branch.setdefault(_root, {})
        branch[_root]['_'] = [f for f in files if is_python_file(f)]

    return tree
