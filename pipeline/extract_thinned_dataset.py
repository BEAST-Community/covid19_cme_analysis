#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, 'scripts')
import common
import thinned_dataset_extraction

paths = common.Paths( sys.argv )

# Support Selection thinning 
thinned_dataset_extraction.extract_ss(paths, "-ss_thinned", paths.ss_mre_thinned_tree)

# Clade compression thinning
thinned_dataset_extraction.extract_cc(paths, "-cc_thinned", paths.cc_thinned_alignment)
