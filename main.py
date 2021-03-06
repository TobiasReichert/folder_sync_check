import sys
import os
import argparse
import time
import shutil


class File(object):

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


def walk_through_dir(root_dir, filelist):
    """
    collect all files in the given directory 
    """
    for root, subdirs, files in os.walk(root_dir):
        for file in files:
            path = os.path.join(root, file)
            path = os.path.abspath(path)
            filelist.append(File(file, path))
        for subdir in subdirs:
            walk_through_dir(subdir, filelist)

def main():

    
    arg_p = argparse.ArgumentParser(
        description="####  Folder sync checker  #####")
    arg_p.add_argument("-c", "--copy",
        help="Copys the missing files in a unsorted<date> folder in dest", action="store_true")
    arg_p.add_argument("src", help="Path to the Sorce") 
    arg_p.add_argument("dest", help="Path to the Destination") 
    args = arg_p.parse_args()

    print("Scanning " + args.src + "...")
    filelist_dir1 = []
    walk_through_dir(args.src, filelist_dir1)
    print("Finished. Found " + str(len(filelist_dir1)) + " files") 

    print("Scanning " + args.dest + "...")
    filelist_dir2 = []
    walk_through_dir(args.dest, filelist_dir2)
    print("Finished. Found " + str(len(filelist_dir2)) + " files") 

    files_missing = []
    for file1 in filelist_dir1:
        file_found = None
        for file2 in filelist_dir2:
            if file1.name == file2.name:
                file_found = file1

        if file_found == None:
            files_missing.append(file1)
    print("\n")
    print(str(len(files_missing)) + " missing files")
    print("\n")
    print(files_missing)

    if args.copy:
        dest_folder = os.path.join(args.dest, "unsorted" + str(time.strftime("%Y%m%d")))
        print("Copying to " + dest_folder + "...")
        if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
        for file in files_missing:
            shutil.copy2(file.path, dest_folder)

if __name__ == "__main__":
    main()
