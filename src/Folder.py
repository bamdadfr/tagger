import os
from simple_chalk import chalk

def Folder(paths):
    results = []

    for path in paths:
        for root, dirs, files in os.walk(path, topdown=False):
            for dir in dirs:
                results.append(os.path.join(root, dir))

    results.sort()

    print(chalk.yellow('\n---\n'))
    print(chalk.blue(len(results) + ' folders found.'))
    print(chalk.yellow('\n---\n'))

    return results
