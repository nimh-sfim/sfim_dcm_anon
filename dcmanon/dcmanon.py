import argparse
from dcmanon import util


def _parse_dcm_anon():
    parser = argparse.ArgumentParser(description="Anonymize a DICOM.")
    parser.add_argument("infile", type=str, help="The input file to anonymize")
    parser.add_argument("-o", "--outfile", default=None, help="The output file name.")
    parser.add_argument(
        "-d", "--outdir", type=str, default=".", help="The output directory."
    )
    args = parser.parse_args()
    return args


def main():
    args = _parse_dcm_anon()
    util.anon_dcmfile(args.infile, out=args.outfile, outdir=args.outdir)


if __name__ == "__main__":
    main()
