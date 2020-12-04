import os
import pydicom


def load_header(fname):
    """
    Loads a dicom header, without the image data.

    Parameters
    ----------
    fname : str
        The filename for the header to load

    Returns
    -------
    The pydicom.dataset without the image pixels
    """

    return pydicom.dcmread(fname, stop_before_pixels=True)


def print_header(fname, tags=[]):
    hdr = load_header(fname)
    if len(tags) == 0:
        print(hdr)
    else:
        # Ensure we don't put the same tag several times
        tags = list(set(tags))
        for t in tags:
            print(f"{t}:\t" + str(hdr[t].value))


def anon_dcmdata(dcmdata):
    """
    Anonymizes a dicom dataset metadata. DOES NOT DEFACE.

    Parameters
    ----------
    dcmdata : pydicom.dataset
        A dicom dataset to be anonymized

    Returns
    -------
    The anonymized dataset
    """

    anon = dcmdata
    anon.PatientName = ""
    anon.PatientBirthDate = "19700101"
    anon.PatientAge = "99Y"
    anon.PatientWeight = "00.1"

    return anon


def anon_dcmfile(infile, out=None, outdir="."):
    """
    Anonymizes a dicom file

    Parameters
    ----------
    infile : str
        The name or path of a file to be anonymized
    out : str
        The new name of the file. Default: None (appends _anon to original
        filename).
    outdir : str
        The directory the anonymized file should go to.
    """

    # Anonymize data
    dcmdata = pydicom.dcmread(infile)
    anon_data = anon_dcmdata(dcmdata)

    # Devise outfile name
    base_name = os.path.basename(infile)
    if out is None:
        out = base_name + "_anon"
    name, ext = os.path.splitext(out)  # In case user put full .dcm
    full_out = os.path.join(outdir, name + ".dcm")

    # Write file
    anon_data.save_as(full_out)
