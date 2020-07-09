#!/usr/bin/env python3

import os
import sys
import zipfile
import re
import argparse

from zipfile import ZipFile

BEATMAP_PATTERN = "(\w.+osz)" 

def is_name_valid(name):
    return re.match(BEATMAP_PATTERN, name, re.M | re.I | re.U)

def run():
    parser = argparse.ArgumentParser(prog="osube", description="Extract osu! beatmap. (.osz)")
    parser.add_argument("File", nargs="*", help="Beatmap files")
    parser.add_argument("Path", type=str, help="Extract path")
    parser.add_argument("-k", "--keep", action="store_true", help="Keep beatmap after extract")
    parser.add_argument("-s", "--silent", action="store_true", help="Suppress result")

    args = parser.parse_args();
    extract_dir = args.Path

    if not os.path.isdir(extract_dir):
        print("Extract path does not exist")
        return

    #Retreive .osz file
    beatmaps = args.File

    if len(beatmaps) <= 0:
        for item in os.listdir():
            if is_name_valid(item):
                beatmaps.append(item)

    #Extract all .osz file to specify directory
    success_files = []
    fail_files = []

    for item in beatmaps:
        if zipfile.is_zipfile(item):
            with ZipFile(item) as file:
                folder_name = re.sub(r".osz", "", item)
                file.extractall(extract_dir + "/" + folder_name)
                success_files.append(item)
        else:
            fail_files.append(item)

    #Try to remove beatmaps
    if not args.keep:
        for item in beatmaps:
            os.remove(item)

    #Show result
    if args.silent:
        return

    if (len(success_files) > 0):
        print("Successful extract beatmaps : ")
        print("------------------------------")
        for item in success_files:
            print(item)
        print()

    if (len(fail_files) > 0):
        print("Fail to extract beatmaps : ")
        print("------------------------------")
        for item in fail_files:
            print(item)
        print()


if __name__ == "__main__":
    run()

