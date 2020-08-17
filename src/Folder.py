import os

def Folder(paths):
    results = []

    for path in paths:
        for root, dirs, files in os.walk(path, topdown=False):
            for dir in dirs:
                results.append(os.path.join(root, dir))

    results.sort()

    print('\n---\n')
    print(len(results) + ' folders found.')
    print('\n---\n')

    return results
