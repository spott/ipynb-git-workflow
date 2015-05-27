#!/usr/bin/env python

"""
Usage: python remove_output.py notebook.ipynb [ > without_output.ipynb ]

Modified from remove_output by:
damianavila (https://gist.github.com/damianavila/5305869)
"""
import sys
from IPython.nbformat import read, write


def remove_outputs(nb):
    """remove the outputs from a notebook"""
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
    # for sheet in nb.worksheets:
    #     for cell in sheet.cells:
    #         if "outputs" in cell:
    #             cell.outputs = []
    #         if "prompt_number" in cell:
    #             del cell["prompt_number"]
    #         if "execution_count" in cell:
    #             del cell["execution_count"]
    # if 'signature' in nb.metadata:
    #     nb.metadata['signature'] = ""

if __name__ == '__main__':
    nb = read(sys.stdin, 4)
    remove_outputs(nb)
    write(nb, sys.stdout, 4)

