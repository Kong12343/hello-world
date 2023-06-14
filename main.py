import argparse
from pathlib import Path
import os
import shutil


def getparam():
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto1", "-1", help="",action="store_true" )
    parser.add_argument("--auto2", "-2", help="",action="store_true" )
    parser.add_argument("--auto3", "-3", help="",action="store_true" )
    args = parser.parse_args()
    return args


def amkdir(adir):
    if not os.path.exists(adir):
        os.makedirs(adir)


def main():
    args = getparam()
    print(args.auto1)

if __name__ == "__main__":
    main()
