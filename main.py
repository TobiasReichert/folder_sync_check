import sys
import os


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
    if len(sys.argv) != 3:
        print("Folder sync check \n Usage: python main.py <folder1> <folder2>")
        exit(-1)
    
    print("Scanning " + sys.argv[1] + "...")
    filelist_dir1 = []
    walk_through_dir(sys.argv[1], filelist_dir1)
    print("Finished. Found " + str(len(filelist_dir1)) + " files") 

    print("Scanning " + sys.argv[2] + "...")
    filelist_dir2 = []
    walk_through_dir(sys.argv[2], filelist_dir2)
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
if __name__ == "__main__":
    main()
