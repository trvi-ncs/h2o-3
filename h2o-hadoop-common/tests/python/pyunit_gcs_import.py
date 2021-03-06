#! /usr/env/python

import sys
import os
sys.path.insert(1, os.path.join("../../../h2o-py"))
from tests import pyunit_utils
import h2o

def gcs_import():
    # Just test the import works - no class clashes, no exception
    keys = h2o.import_file("gs://gcp-public-data-nexrad-l2/2018/01/01/KABR/NWS_NEXRAD_NXL2DPBL_KABR_20180101050000_20180101055959.tar", parse=False)
    assert len(keys) == 1


if __name__ == "__main__":
    pyunit_utils.standalone_test(gcs_import)
else:
    gcs_import()
