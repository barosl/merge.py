#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

dirs = [
	'/media/SENJOUGAHARA/box/작품',
	'/media/SAKAGAMI/box/작품',
	'/home/barosl/box/작품',
]

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