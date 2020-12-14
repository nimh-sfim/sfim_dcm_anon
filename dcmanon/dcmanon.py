#!/bin/env python

import os
from glob import glob
import argparse
from dcmanon import util

def run_anon(source, dest, name="", ident=None):
    """
    Runs anonymization

    Parameters
    ----------
    source : str
        The source file or directory to anonymize.
    dest : str
        The destination for anonymized files.
    name : str
        The replacement name for Patient Name. Default is blank.
    ident : str
        The replacement Patient ID. Default is original ID.
    """
    if os.path.isfile(source):
        util.anon_dcmfile(source, out=dest, name=name, ident=ident)
    elif os.path.isdir(source):
        # Verify dest will exist as a directory
        if not os.path.isdir(dest):
            if os.path.isfile(dest):
                raise ValueError(
                    "%s exists as a file; must be directory" % dest
                )
            os.mkdir(dest)
        # Glob for dcm files
        dcmfiles = glob(os.path.join(source, '*.dcm'))
        if len(dcmfiles) == 0:
            raise ValueError(
                "Target directory %s has no DICOM files." % source
            )
        for f in dcmfiles:
            # Get basename
            path, fname = os.path.split(f)
            name, ext = os.path.splitext(fname)
            out_full = os.path.join(dest, name)
            print("Writing to %s" % out_full)
            util.anon_dcmfile(f, out=out_full, name=name, ident=ident)
    else:
        raise ValueError("DICOM source %s does not exist" % source)


def _parse_dcm_anon():
    parser = argparse.ArgumentParser(description="Anonymize a DICOM.")
    output = parser.add_mutually_exclusive_group(required=True)
    output.add_argument(
        "-o", "--out", type=str,
        help="Output destination."
    )
    output.add_argument(
        "-f", "--overwrite", action="store_true",
        help="Overwrite the original files."
    )
    parser.add_argument(
        "input", type=str,
        help="The input file or directory to anonymize."
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
    run_anon(args.input, args.out, name=args.name, ident=args.ident)


if __name__ == "__main__":
    main()
