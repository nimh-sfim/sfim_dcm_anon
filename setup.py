from setuptools import setup, find_packages
setup(name='dcmanon',
      version='0.1',
      description='Anonymizes Dicoms',
      author='Joshua B. Teves',
      author_email='joshua.teves@nih.gov',
      python_requires='>=3.6',
      install_requires='pydicom',
      entry_points={'console_scripts':
          ['dcmanon=dcmanon.dcmanon:main',
           'dcmhdr=dcmanon.dcmhdr:main']}
      )
