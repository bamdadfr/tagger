import os

def Folder(p):
    path = p
    results = []

    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            results.append(os.path.join(root, dir))

    results.sort()

    return results
