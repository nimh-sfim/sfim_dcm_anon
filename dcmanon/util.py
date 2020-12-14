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


def anon_dcmdata(dcmdata, name="", ident=None):
    """
    Anonymizes a dicom dataset metadata. DOES NOT DEFACE.

    Parameters
    ----------
    dcmdata : pydicom.dataset
        A dicom dataset to be anonymized
    name : str
        The new name of the patient. Default: blank.
    ident : str
        The new ID of the patient. Default: None (keeps original ID)

    Returns
    -------
    The anonymized dataset
    """

    anon = dcmdata
    anon.PatientName = name
    if ident:
        anon.PatientID = ident
    # Anonymize Birthdate
    year = anon.PatientBirthDate[:3]
    anon.PatientBirthDate = year + "0101"
    # See if age should be truncated to 90
    age = anon.PatientAge
    time_unit = age[3]
    if time_unit == 'Y':
        # May be over 90
        age_years = int(age[:3])
        if age_years > 90:
            age_years = 90
        age = '%3.3dY' % age_years
        anon.PatientAge = age
    return anon


def anon_dcmfile(infile, out="", name="", ident=None):
    """
    Anonymizes a dicom file

    Parameters
    ----------
    infile : str
        The name or path of a file to be anonymized.
    out : str
        The output name.
    name : str
        The new name of the Patient. Default: blank.
    ident : str
        The new Patient ID. Default: None (keeps original ID).
    """

    # Anonymize data
    try:
        dcmdata = pydicom.dcmread(infile)
    except pydicom.errors.InvalidDicomError:
        raise ValueError('File %s is not a valid dicom' % infile)
    anon_data = anon_dcmdata(
        dcmdata, name=name, ident=ident
    )

    # Devise outfile name
    base_name = os.path.basename(infile)
    base_name, ext = os.path.splitext(base_name)
    if out == "":
        out = base_name
    fname, ext = os.path.splitext(out)  # In case user put full .dcm
    full_out = os.path.join(fname + ".dcm")

    # Write file
    anon_data.save_as(full_out)
