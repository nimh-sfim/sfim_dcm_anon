# sfim_dcm_anon
Anonymizes dicom files coming from oxygen tarballs

# Specification
This program will take a tarball from oxygen, and assume the following
directory structure:

```
tarball_name/
    YYYYMMDD-NNNNN
        README-Study.txt
        realtime/
        sc_0000/
        mr_0001/
            dcm1
            dcm2
            ...
        mr_0002/
            dcm1
            dcm2
            ...
        ...
```

That is, the tarball will expand to make a directory of the same name,
which contains a subdirectory with a datetime and 5-digit code.
This directory will itself contain the relevant subject information,
including a realtime directory and directories with the format mr_*.
All copied dicoms will have any PII replaced with a blank string.
The copied directory structure will have the structure:

```
YYYYMMDD/
    realtime/
    series-01/
        series-01_0001.dcm
        series-01_0002.dcm
        ...
    series-02/
        series-02_0001.dcm
        series-02_0002.dcm
        ...
```

unless a different top-level directory name is specified.
The top-level directory will have a complete copy of realtime, and each
series will have its own subdirectory with dicoms named in their
acquisition order (by use of AcquisitionTime dicom information).
