import argparse
from dcmanon import util


def _parse_dcm_hdr():
    parser = argparse.ArgumentParser(description="Print DICOM header.")
    parser.add_argument(
        "file", type=str, help="The input file to print header info for."
    )
    args = parser.parse_args()
    return args


def main():
    args = _parse_dcm_hdr()
    util.print_header(args.file)


if __name__ == "__main__":
    main()
