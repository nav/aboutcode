#!/usr/bin/env python

import os
import argparse
import fs
import graph


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=str,
                        help="path to the root directory of project")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    directory = os.path.abspath(args.directory)
    tree = fs.recursively_generate_directory_tree(directory)
    graph.generate_graph(tree)
