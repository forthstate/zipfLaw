"""Plot the word count distribution"""

import argparse
import pandas as pd

def main(args):
    """plots the word frequency against the inverse rank using 
       the pandas library
    """
    input_csv = args.infile
    df = pd.read_csv(input_csv, header=None,
                     names=('word','word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                            method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
                               y='inverse_rank', xlim=args.xlim,
                               figsize=[12, 6],
                               grid=True)
    fig = scatplot.get_figure()
    fig.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'), 
                        nargs='?', default='-',
                        help='Input csv file name')
    parser.add_argument('--outfile', type=str,
                        default='results/plotcounts.png',
                        help='Output file name')
    parser.add_argument('--xlim', type=float, nargs=2,
                        default=None, metavar=('XMIN','XMAX'),
                        help='X-axis limits')
    args = parser.parse_args()
    main(args)
