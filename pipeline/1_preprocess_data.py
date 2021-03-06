#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, 'scripts')
import common
import preprocessing
import util

paths = common.Paths( sys.argv )

util.make_path_clean( paths.preanalysis_runs_dir )

preprocessing.trim_separate_align(paths.raw_sequences,
                                  paths.dataset,
                                  paths.preanalysis_runs_dir,
                                  util.make_path_in_workdir(paths.version) )

result_file=os.path.join( paths.preanalysis_runs_dir, "preprocessed.fasta" )
util.expect_file_exists( result_file )
util.copy( result_file, paths.raw_alignment )

outgroup_file=os.path.join( paths.preanalysis_runs_dir, "covid_outgroups.fasta" )
util.expect_file_exists( outgroup_file )
util.copy( outgroup_file, paths.outgroups_file )

preprocessing.remove_duplicates(paths.raw_alignment,
              									paths.alignment,
              									paths.duplicates_json )


