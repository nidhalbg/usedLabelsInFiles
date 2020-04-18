import sys
import os
import fnmatch
import glob
from os import walk
import mmap


def main():
   filelabes = sys.argv[1]

   if not os.path.isfile(filelabes):
       print("File path {} does not exist. Exiting...".format(filelabes))
       sys.exit()
  
   with open(filelabes) as fl:
       for label in fl:
            # check = False
            for root, directories, filenames in os.walk('.'):
                for filename in fnmatch.filter(filenames, '*.js') + fnmatch.filter(filenames, '*.html.twig'):
                    datafile = os.path.join(root,filename)
                    with open(datafile) as df:
                        if os.stat(datafile).st_size == 0:
                            s = mmap.mmap(df.fileno(), 0, access=mmap.ACCESS_READ)
                            if s.find(label) != -1:
                                usedfile = open("usedlabes.txt","w")
                                usedfile.write(label + "used")
                                usedfile.close()

if __name__ == '__main__':
    main()