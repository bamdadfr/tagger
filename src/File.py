import os

def File(path):
    results = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if ".flac" in name:
                results.append(os.path.join(root, name))

    results.sort()

    return results
