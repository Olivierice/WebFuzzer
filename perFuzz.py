#!/bin/python3
import queue
import threading
import urllib3
import urllib.parse as U 
import urllib.error as E
import sys, getopt

def usage():
    print("""
---------------------------------------------------------------------------------------
| Usage: python3 perFuzz.py -u target_ip -t nb_threads -f word_list.txt -e extensions |
--------------------------------------------------------------------------------------- 
    """)


def get_args(argv):
    # Number of args = len(sys.argv) | argv[0] = script name
    try:
        if len(sys.argv) > 1:
            opts, args = getopt.getopt(argv,"h:u:t:f:e:",["--url","--threads","--wordlist","--extension"])
            
            for opt, arg in opts:
                if opt == '-h':
                    usage()
                    sys.exit(2)
                elif opt in ("-u","--url"):
                    target_url = arg
                    print("L'argument en face de -u est: {}".format(target_url))

                elif opt in ("-t","--threads"):
                    nb_threads = arg
                    print("L'argument en face de -t est: {}".format(nb_threads))
                elif opt in ("-f","--wordlist"):
                    list_file = arg
                    print("L'argument en face de -f est: {}".format(list_file))
                elif opt in ("-e","--extension"):
                    exts = arg
                    print("L'argument en face de -e est: {}".format(exts))
        else:
            usage()
            sys.exit(2)

    except getopt.GetoptError:
        usage()
        sys.exit(2)

def main(argv):
    get_args(argv)



if __name__ == '__main__':
    main(sys.argv[1:])
