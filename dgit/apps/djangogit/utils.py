import os

def get_repository_dirs(root_path):
    """
    get repository dirs from given root_path
    """
    dirs = []
    for fname in os.listdir(root_path):
        fname = os.path.join(root_path,fname)
        if os.path.isdir(fname):
            #checking if current path has .git subdirectory
            if os.path.exists(os.path.join(fname,".git")):
                dirs.append(fname)
    return dirs
