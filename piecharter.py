#!/usr/bin/env python

import matplotlib.pyplot as plt
import argparse

def main():
    """Creates a simple pie chart and saves it to .png file image"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-l',
            '--labels',
            help='labels for the slices of the chart',
            nargs='+',
            required=True
            )

    parser.add_argument(
            '-s',
            '--sizes',
            help='relative sizes of the slices',
            nargs='+',
            required=True
            )

    parser.add_argument(
            '-f',
            '--filename',
            help='path to the filename where the chart will be saved',
            default='chart.png'
            )

    parser.add_argument(
            '-H',
            '--height',
            help='height of the chart (px)',
            type=int,
            default=181
            )

    parser.add_argument(
            '-L',
            '--length',
            help='lenght of the chart (px)',
            type=int,
            default=181
            )

    args = parser.parse_args()
    print(args)

    return

def piechart():
    """docstring for piechart"""


if __name__ == '__main__':
    main()
