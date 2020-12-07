#!/bin/env python

import argparse
from dcmanon import util


def _parse_dcm_anon():
    parser = argparse.ArgumentParser(description="Anonymize a DICOM.")
    parser.add_argument(
        "infile", type=str,
        help="The input file to anonymize"
    )
    parser.add_argument(
        "-o", "--outfile", type=str, default="",
        help="The output file name."
    )
    parser.add_argument(
        "-d", "--outdir", type=str, default=".",
        help="The output directory."
    )
    parser.add_argument(
        "-n", "--name", type=str, default="",
        help="The replacement name. Default is blank.",
    )
    parser.add_argument(
        "-i", "--ident", type=str, default=None,
        help="The replacement Patient ID. Default is original ID."
    )
    args = parser.parse_args()
    return args


def main():
    args = _parse_dcm_anon()
    if args.ident == "":
        args.ident = None
    util.anon_dcmfile(
        args.infile,
        out=args.outfile,
        outdir=args.outdir,
        name=args.name,
        ident=args.ident
    )


if __name__ == "__main__":
    main()
