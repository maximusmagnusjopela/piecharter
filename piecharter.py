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
            default=400
            )

    parser.add_argument(
            '-L',
            '--length',
            help='lenght of the chart (px)',
            type=int,
            default=400
            )

    parser.add_argument(
            '-F',
            '--font-size',
            help='size of the label font',
            default=12
            )

    parser.add_argument(
            '-S',
            '--start-angle',
            help='start angle for the pie chart',
            type=float,
            default=10
            )


    args = parser.parse_args()
    piechart(args.labels,
             args.sizes,
             args.height,
             args.length,
             args.font_size,
             args.start_angle,
             args.filename)

    return

def piechart(labels, sizes, height, length, font_size, start_angle, filename):
    """ creates and saves a piechart to filename"""

    my_dpi = 96.0
    plt.figure(figsize=(height/my_dpi, length/my_dpi), dpi=my_dpi)
    _, texts = plt.pie(sizes,labels=labels, labeldistance=0.55, colors=['b','g','r','y','c'], startangle=start_angle)

    for t in texts:
        t.set_color('white')
        t.set_fontsize(font_size)
        t.set_horizontalalignment('center')
        t.set_weight('bold')

    plt.axis('equal')
    plt.savefig(filename,bbox_inches='tight')

    return


if __name__ == '__main__':
    main()
