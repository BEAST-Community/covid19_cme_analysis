from shutil import rmtree
import os
import sys
import common

def fail( msg ):
	print( msg )
	sys.exit(1)

def versioned_path(version, path):
	return os.path.join( common.work_dir, version, path)

def version_valid( version ):
	return os.path.isdir( versioned_path( version, "" ) )

def get_version( argv, i=1 ):
	if len(argv) < i+1:
		fail("Insufficient arguments (version string?)")
	version = argv[i]
	if not version_valid( version ):
		fail("Invalid version: {}".format(version))
	return version

def clean_dir( path ):
	if os.path.exists( path ):
		rmtree( path, ignore_errors=True )

def mkdirp( path ):
	if not os.path.exists( path ):
		os.mkdir( path )

def make_path( path ):	
	if not os.path.exists( path ):
		os.makedirs( path )

def expect_dir_exists( dir_path ):
	if not os.path.isdir( dir_path ):
		raise RuntimeError( "Directory doesn't exist: " + dir_path )

def expect_file_exists( file_path ):
	if not os.path.isfile( file_path ):
		raise RuntimeError( "File doesn't exist: " + file_path )

def expect_executable_exists( executable ):
	import distutils.spawn
	if not distutils.spawn.find_executable( executable ):
		raise RuntimeError( "Executable not found: " + executable )
