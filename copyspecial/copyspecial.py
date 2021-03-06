#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# Write functions and modify main() to call them


def get_paths(dir):
    paths = []
    re_special = '__\w+__'
    filenames = os.listdir(dir)
    for filename in filenames:
        match = re.search(re_special, filename)
        if match:
            paths.append(os.path.abspath(os.path.join(dir, filename)))
    return paths


def copy_to_dir(paths, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        filename = os.path.basename(path)
        shutil.copy(path, dir)


def zip(paths, zipfile):
    cmd = 'tar -czf ' + zipfile + ' ' + ' '.join(paths)
    (status, output) = subprocess.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # Call your functions
    paths = []
    for dir in args:
        paths += get_paths(dir)  # only works if both elements are lists

    if todir:
        copy_to_dir(paths, todir)

    elif tozip:
        zip(paths, tozip)

    else:
        print('\n'.join(paths))


if __name__ == "__main__":
    main()
