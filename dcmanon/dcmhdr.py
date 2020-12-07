#!/bin/env python

import argparse
from dcmanon import util


def _parse_dcm_hdr():
    parser = argparse.ArgumentParser(
        description="Print DICOM header. Adding arguments prints only"
        "a subset of the available header info."
    )
    parser.add_argument(
        "file", type=str, help="the input file to print header info for."
    )
    parser.add_argument(
        "-n", "--name", action="store_true",
        help="print Patient Name"
    )
    parser.add_argument(
        "-i", "--ident", action="store_true",
        help="print Patient ID"
    )
    parser.add_argument(
        "-d", "--description", action="store_true",
        help="print Series Description."
    )
    parser.add_argument(
        "-s", "--seriesnum", action="store_true", help="print Series Number"
    )
    args = parser.parse_args()
    return args


def main():
    args = _parse_dcm_hdr()
    tags = []
    # Sad hack
    if args.name:
        tags.append("PatientName")
    if args.ident:
        tags.append("PatientID")
    if args.description:
        tags.append("SeriesDescription")
    if args.seriesnum:
        tags.append("SeriesNumber")
    util.print_header(args.file, tags=tags)


if __name__ == "__main__":
    main()
