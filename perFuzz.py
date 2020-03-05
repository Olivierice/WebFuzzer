#!/bin/python3
import queue
import threading
import urllib3
import urllib.parse as U 
import urllib.error as E
import sys, getopt

def usage():
    print("     - Python Fuzzing Tool -")
    print()
    print("     Usage: perFuzz.py -u target_ip -f word_list")
    print()
    print("     -u --target      -   ip or hostname of the target")
    print("     -f --wordlist    -   wordlist to use to fuzz ")
    print("     -t --threads     -   threads number dedicated to fuzz, have to be an integer")
    print("     -e --extensions  -   extensions you want to add after the words in the word_list")
    print()




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
                    try:
                        nb_threads = int(arg)
                    except:
                        usage()
                        print("/!\\ Warning /!\\    -t --threads - have to be an integer")
                        sys.exit(2)
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
