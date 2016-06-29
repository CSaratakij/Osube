#!/usr/bin/env python3

import os
import sys
import zipfile
import re

from zipfile import ZipFile


def help():
    print("\t _______  _______  __   __  _______  _______")
    print("\t|       ||       ||  | |  ||  _    ||       |")
    print("\t|   _   ||  _____||  | |  || |_|   ||    ___|")
    print("\t|  | |  || |_____ |  |_|  ||       ||   |___")
    print("\t|  |_|  ||_____  ||       ||  _   | |    ___|")
    print("\t|       | _____| ||       || |_|   ||   |___")
    print("\t|_______||_______||_______||_______||_______|")
    print()
    print()
    print("\t [ Extract multiple osu!'s beatmap (.osz) ]")
    print()
    print("\t __________________________________________")
    print("\t|                                          |")
    print("\t|            Extract Osu! Beatmap          |")
    print("\t|__________________________________________|")
    print("\t|                                          |")
    print("\t|         osube [extract directory]        |")
    print("\t|       osube /home/username/osu/Songs     |")
    print("\t|__________________________________________|")
    print("\t|                                          |")
    print("\t| Run this command in the folder that have |")
    print("\t|         .osz file to extract.            |")
    print("\t|__________________________________________|")
    print()
    print()


def run():

    if len(sys.argv) > 1:

        if ("-h" in sys.argv) or ("--help" in sys.argv):
            help()

        else:
            extract_dir = sys.argv[1]
            current_dir = os.getcwd()
            current_dir_items = os.listdir(current_dir)
            beatmap_pattern = "(\w.+osz)"
            beatmaps = []
            success_list = []
            fail_list = []

            #Retreive .osz file in current directory
            for item in current_dir_items:
                if re.match(beatmap_pattern, item, re.M | re.I | re.U):
                    beatmaps.append(item)

            #Extract all .osz file to specify directory
            for item in beatmaps:
                if zipfile.is_zipfile(item):
                    with ZipFile(item) as beatmap:
                        beatmap_extract_folder_name = re.sub(r".osz", "", item)
                        beatmap.extractall(extract_dir + "/" + beatmap_extract_folder_name)
                        success_list.append(item)
                else:
                    fail_list.append(item)


            #Show extract result
            print()
            print()
            print("\t ----------------------------------------")
            print("\t|             Extract Result             |")
            print("\t ----------------------------------------")
            print()
            print("\tFail : ", len(fail_list))
            print("\tSuccess : ", len(success_list))
            print()
            print("\tFrom : ", current_dir)
            print("\tTo : ", extract_dir)
            print()

            #List the beatmap that successful extracted
            if (len(success_list) > 0):
                print("\tSuccessful extract beatmaps : ")
                print()
                for item in success_list:
                    print("\t\t- ", item)
                print()

            #List the beatmap that unsuccessful extracted
            if (len(fail_list) > 0):
                print("\tFail to extract beatmaps : ")
                print()
                for item in fail_list:
                    print("\t\t- ", item)
                print()
                print()

    else:
        print()
        print("Please specify extract directory.\t\t:(")
        print()
        help()


if __name__ == "__main__":
    run()
