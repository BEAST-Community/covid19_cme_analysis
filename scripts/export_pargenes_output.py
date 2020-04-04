import os
import sys
import shutil

import util
import common
import reattach_duplicates
import rf_distance
import iqtree_tests

def export(pargenes_run_dir, paths):
  print("Pargenes run dir: " + pargenes_run_dir)
  pargenes_output = os.path.join(pargenes_run_dir, "pargenes_output")
  ml_run_dir = os.path.join(pargenes_output, "mlsearch_run", "results", "ali_fasta")

# export best ml tree (with support values if existing)
  src = ""
  if (common.pargenes_bs_trees > 0):
    src = os.path.join(pargenes_output, "supports_run", "results", "ali_fasta.support.raxml.support")
  else:
    src = os.path.join(ml_run_dir, "ali_fasta.raxml.bestTree")
  shutil.copy(src, paths.raxml_best_tree)

# export best tree with duplicates reattached
  reattach_duplicates.reattach_duplicates(src, paths.raxml_best_tree_with_duplicate, paths.duplicates_json)
  
# export best tree with TBE values
  if (common.pargenes_bs_trees > 0):
    src = os.path.join(pargenes_output, "supports_run", "results", "ali_fasta.support.tbe.raxml.support")
    shutil.copy(src, paths.raxml_best_tree_tbe)

# export best ml model
  src = os.path.join(ml_run_dir, "ali_fasta.raxml.bestModel")
  shutil.copy(src, paths.raxml_best_model)

# export all ml trees
  src = os.path.join(ml_run_dir, "sorted_ml_trees.newick")
  shutil.copy(src, paths.raxml_all_ml_trees)
  src = os.path.join(ml_run_dir, "sorted_ml_trees_ll.newick")
  shutil.copy(src, paths.raxml_all_ml_trees_ll)

# export bootstrap trees
  if (common.pargenes_bs_trees > 0):
    src = os.path.join(pargenes_output, "concatenated_bootstraps", "ali_fasta.bs")
    shutil.copy(src, paths.raxml_bootstrap_trees)

  rf_distance.export_pairwise_rf_distance(paths.raxml_all_ml_trees, paths.raxml_all_ml_trees_rf_distances, paths.raxml_all_ml_trees_rf_logs)
  

# compute RF distance between starting and ML trees for the best run
  rf_dir = os.path.join(paths.runs_dir, "rfdistances")
  util.clean_dir(rf_dir)
  util.mkdirp(rf_dir)
  tree1 = os.path.join(ml_run_dir, "ali_fasta.raxml.bestTree")
  tree2 = os.path.join(ml_run_dir, "ali_fasta.raxml.startTree")
  rf = rf_distance.get_rf_distance(tree1, tree2, rf_dir)
  print("RF between start and ML trees: " + str(rf))


