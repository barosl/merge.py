#!/usr/bin/env python

import os
import sys

if not os.path.exists('.mergerc'):
	print >> sys.stderr, '* invalid target directory'
	raise SystemExit, 1

execfile('.mergerc')

os.system('rm -rf *')

def proc_dir(dpath, rel_dpath):
	try: os.mkdir(rel_dpath)
	except OSError: pass

	for fname in os.listdir(dpath):
		fpath = dpath+'/'+fname
		rel_fpath = rel_dpath+'/'+fname

		if os.path.isdir(fpath): proc_dir(fpath, rel_fpath)
		else:
			try: os.symlink(fpath, rel_fpath)
			except OSError:
				print >> sys.stderr, '* err:', fpath

for dpath in dirs:
	proc_dir(dpath, '.')
