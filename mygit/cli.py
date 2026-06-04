# mygit/cli.py

from mygit.core.repo import Repo
import sys

def main():

    print("cli lancé")
    args = sys.argv[1:]

    if not args:
        print("Usage: mygit <command>")
        return

    if args[0] == "init":
        Repo().init()
    else:
        print("Commande inconnue")