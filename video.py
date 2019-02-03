#!/usr/bin/python
import os, heapq, sys, time, shutil, filecmp 
from stat import *


traditional = [
    (1024 ** 5, 'P'),
    (1024 ** 4, 'T'), 
    (1024 ** 3, 'G'), 
    (1024 ** 2, 'M'), 
    (1024 ** 1, 'K'),
    (1024 ** 0, 'B'),
    ]

alternative = [
    (1024 ** 5, ' PB'),
    (1024 ** 4, ' TB'), 
    (1024 ** 3, ' GB'), 
    (1024 ** 2, ' MB'), 
    (1024 ** 1, ' KB'),
    (1024 ** 0, (' byte', ' bytes')),
    ]

verbose = [
    (1024 ** 5, (' petabyte', ' petabytes')),
    (1024 ** 4, (' terabyte', ' terabytes')), 
    (1024 ** 3, (' gigabyte', ' gigabytes')), 
    (1024 ** 2, (' megabyte', ' megabytes')), 
    (1024 ** 1, (' kilobyte', ' kilobytes')),
    (1024 ** 0, (' byte', ' bytes')),
    ]

iec = [
    (1024 ** 5, 'Pi'),
    (1024 ** 4, 'Ti'),
    (1024 ** 3, 'Gi'), 
    (1024 ** 2, 'Mi'), 
    (1024 ** 1, 'Ki'),
    (1024 ** 0, ''),
    ]

si = [
    (1000 ** 5, 'P'),
    (1000 ** 4, 'T'), 
    (1000 ** 3, 'G'), 
    (1000 ** 2, 'M'), 
    (1000 ** 1, 'K'),
    (1000 ** 0, 'B'),
    ]



def size(bytes, system=verbose):
    for factor, suffix in system:
        if bytes >= factor:
            break
    bytes = bytes + .00
    amount = bytes/factor
    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return "%.2f" % amount + suffix 



print 'Get Files From:', str(sys.argv[1])
def move_files(rootfolder, extension=".avi"):
        counter = 0
        totalcount = 0
        totalsize = 0
        dircount = 0 
        for dirname, dirnames, filenames in os.walk(rootfolder):
                dircount = dircount + 1
                print "\nScaning Directory " + str(dircount) + ": " + dirname
        	for filename in filenames:
                        totalcount = totalcount + 1
        		if filename.lower().endswith(extension):
				src = os.path.join(dirname, filename)
                                stop = False
                                st = os.stat(src)
                                counter = counter + 1
                                totalsize = totalsize + st.st_size
				dst = os.path.join(sys.argv[2], time.strftime('%Y-%m-%d',time.localtime(st[ST_MTIME])))                                 
				print "\n\tDestination Folder Name: ", dst
        			try:
                			os.makedirs(dst)
				except:
					pass

                                dstfile = os.path.join(dst, str(st[ST_MTIME]) + "-" + filename) 
				while not stop:
					print "\tVerifing file number " + str(counter) + ": ", src 
					try:
						s1 = st 
						s2 = os.stat(dstfile)
						if s1.st_size == s2.st_size and int(s1.st_mtime) == int(s2.st_mtime):
							stop = True	
						else:
							print "\t\tFailed verification"
                                        except:	
						print "\t\tFile does not exists"

					if not stop:
						print "\tCopying: ", src 
						shutil.copy2(src, dstfile)
	print "\n\n" + str(counter) + " files copied of " + str(totalcount) + " from " + str(dircount) + " directories, with a total size of " + str(size(totalsize))
				
move_files(sys.argv[1], (".mov", ".m4a", ".mp4" , ".jpg"))
