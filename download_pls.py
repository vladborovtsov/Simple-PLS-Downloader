#!/usr/bin/env python

import os
import sys
import configparser
import urllib

'''
Usage: 

download_pls.py <PLS filename> <folder for downloads>
'''

playlist_file=sys.argv[1]
dst_dir=sys.argv[2]

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

###

pls = configparser.RawConfigParser()
pls.read(playlist_file)

p = pls['playlist']
fcount = p['NumberOfEntries']
print fcount

for x in range(1,int(fcount)+1):
    url = p['File%s'%(x,)]
    title = p['Title%s'%(x,)]
    
    #print x,":",url,title
    #print "Downloading..."
    
    fntitle = "".join(c for c in title if c.isalnum() or c in (' ','.','_','-')).rstrip().replace("  "," ").replace("..",".")[:50]
    fn = os.path.join( dst_dir, "%s.mp3" % (fntitle))
    print "%s of %s ::::  %s -> %s" % (x, fcount, url, fn)
    
    if not os.path.exists(fn):
	urllib.urlretrieve(url, fn)
    else:
	print "Skipping %s - FILE EXISTS" % (fn)