#!/usr/bin/env fiji
"""Drive the application from this file, using a main() function below.
"""
import argparse


def main(fn, verbose):
    """Run the main Fiji-based functionality.
    """
    from jython_imports import IJ
    impin = IJ.openImage(fn)
    fout = fn + '.out.tif'
    if verbose:
        print(fout)
    IJ.saveAs(impin, 'tif', fout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Do work using Fiji's huge plugin library.")
    parser.add_argument('fin', help='The file to be opened.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print out runtime information.')

    args = parser.parse_args()
    main(args.fin, args.verbose)
