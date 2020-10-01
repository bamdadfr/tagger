import os
import style

def Folder(paths):
    results = []

    for path in paths:
        for root, dirs, files in os.walk(path, topdown=False):
            for dir in dirs:
                results.append(os.path.join(root, dir))

    results.sort()

    print(style.yellow('\n---\n'))
    print(style.blue(str(len(results)) + ' folders found.'))
    print(style.yellow('\n---\n'))

    return results
