#!/usr/bin/env python

import os
import util

scripts_dir = os.path.dirname( os.path.realpath(__file__) )
base_dir = os.path.abspath( os.path.realpath( os.path.join(
            os.path.dirname( os.path.abspath( os.path.realpath( __file__ ))),
            "..")))
work_dir = os.path.join(base_dir, "work_dir")

# tools
software_path = os.path.join(base_dir, "software")
raxml = os.path.join(software_path, "raxml-ng", "bin", "raxml-ng-mpi")
modeltest = os.path.join(software_path, "modeltest", "bin", "modeltest-ng-mpi")
pargenes = os.path.join(software_path, "ParGenes", "pargenes", "pargenes-hpc.py")
mptp = os.path.join(software_path, "mptp", "bin", "mptp")
epa = os.path.join(software_path, "epa-ng", "bin", "epa-ng")
root_digger = os.path.join(software_path, "root_digger", "bin", "rd")
genesis = os.path.join(software_path, "genesis", "bin", "apps")
genesis_reduce_duplicates = os.path.join(genesis, "reduce_duplicates")
genesis_reattach_duplicates = os.path.join(genesis, "reattach_duplicates")

# config
config_dir = os.path.join(base_dir, "config")
outgroup_spec = os.path.join(config_dir, "outgroups.txt")

# paths that depend on the specified version
class Paths():
  """docstring for Paths"""
  def __init__( self, argv, i=1 ):
    version = util.get_version( argv, i )

    self.version = version
    self.root_data_dir = util.versioned_path(version, self.root_data_dir)
    self.data_path = util.versioned_path(version, self.data_path)
    self.raw_alignment = util.versioned_path(version, self.raw_alignment)
    self.alignment = util.versioned_path(version, self.alignment)
    self.outgroup_alignment = util.versioned_path(version, self.outgroup_alignment)
    self.duplicates_json = util.versioned_path(version, self.duplicates_json)

    self.root_runs_dir = util.versioned_path(version, self.root_runs_dir)
    self.runs_dir = util.versioned_path(version, self.runs_dir)
    self.raxml_ml_runs_dir = util.versioned_path(version, self.raxml_ml_runs_dir)
    self.pargenes_runs_dir = util.versioned_path(version, self.pargenes_runs_dir)
    self.modeltest_runs_dir = util.versioned_path(version, self.modeltest_runs_dir)

    self.root_results_dir = util.versioned_path(version, self.root_results_dir)
    self.results_dir = util.versioned_path(version, self.results_dir)
    self.raxml_best_tree = util.versioned_path(version, self.raxml_best_tree)
    self.raxml_best_tree_tbe = util.versioned_path(version, self.raxml_best_tree_tbe)
    self.raxml_best_tree_with_duplicate = util.versioned_path(version, self.raxml_best_tree_with_duplicate)
    self.raxml_best_model = util.versioned_path(version, self.raxml_best_model)
    self.raxml_all_ml_trees = util.versioned_path(version, self.raxml_all_ml_trees)
    self.raxml_all_ml_trees_rf_distances = util.versioned_path(version, self.raxml_all_ml_trees_rf_distances)
    self.raxml_all_ml_trees_rf_logs = util.versioned_path(version, self.raxml_all_ml_trees_rf_logs)
    self.raxml_all_ml_trees_ll = util.versioned_path(version, self.raxml_all_ml_trees_ll)
    self.raxml_bootstrap_trees = util.versioned_path(version, self.raxml_bootstrap_trees)

    self.mptp_output = util.versioned_path(version, self.mptp_output)
    self.epa_rooting_dir = util.versioned_path(version, self.epa_rooting_dir)

  version = "UNDEFINED"
  # data
  root_data_dir = "data"
  data_path = os.path.join(root_data_dir)
  raw_alignment = os.path.join(data_path, "covid_raw.fasta")
  alignment = os.path.join(data_path, "covid_edited.fasta")
  outgroup_alignment = os.path.join(data_path, "covid_outgroups.fasta")
  duplicates_json = os.path.join(data_path, "covid_duplicates.json")

  # runs
  root_runs_dir = "runs"
  runs_dir = os.path.join(root_runs_dir)
  raxml_ml_runs_dir = os.path.join(runs_dir, "raxml_runs")
  pargenes_runs_dir = os.path.join(runs_dir, "pargenes_runs")
  modeltest_runs_dir = os.path.join(runs_dir, "modeltest_runs")

  # results
  root_results_dir = "results"
  results_dir = os.path.join(root_results_dir)
  raxml_best_tree = os.path.join(results_dir, "raxml_best_tree.newick")
  raxml_best_tree_tbe = os.path.join(results_dir, "raxml_best_tree_tbe.newick")
  raxml_best_tree_with_duplicate = os.path.join(results_dir, "raxml_best_tree_with_duplicate.newick")
  raxml_best_model = os.path.join(results_dir, "raxml_best_model.txt")
  raxml_all_ml_trees = os.path.join(results_dir, "raxml_all_ml_trees.newick")
  raxml_all_ml_trees_ll = os.path.join(results_dir, "raxml_all_ml_trees_with_ll.txt")
  raxml_bootstrap_trees = os.path.join(results_dir, "raxml_bs_trees.newick")

  raxml_all_ml_trees_rf_distances = os.path.join(results_dir, "raxml_all_ml_trees.rf.distances")
  raxml_all_ml_trees_rf_logs = os.path.join(results_dir, "raxml_all_ml_trees.rf.logs")
  mptp_output = os.path.join(results_dir, "mptp_output.txt")
  epa_rooting_dir = os.path.join(results_dir, "epa_rooting")
  root_digger_output = os.path.join(results_dir, "root_digger_lwr.newick")
  root_digger_logfile = os.path.join(root_digger_runs_dir,


# misc
subst_model = "GTR+R4"
raxml_precision = "9"
raxml_min_bl = "0.000000001"
 
pargenes_seed = 3000
pargenes_rand_trees = 0
pargenes_pars_trees = 100
pargenes_bs_trees = 100

if (util.is_slurm()):
  available_cores = 256
else:
  available_cores = 40

cores_for_one_raxml_run = 4


