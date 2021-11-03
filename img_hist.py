#!/usr/bin/env python3

# Shows a histogram of the number of files per subdirectory of <img-dir>

import os
import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " <img-dir>")
	exit()

res={}

for person in os.listdir(sys.argv[1]):
	nfiles = len(os.listdir(sys.argv[1] + '/' + person))
	res[nfiles] = res.get(nfiles, 0) + 1

plt.bar(res.keys(), res.values())
#plt.xticks(range(1 + max(res.keys())), rotation=90)
plt.xticks(sorted(res.keys()), rotation=90)
plt.show()