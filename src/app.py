import subprocess
import argparse


def commands():
    parser = argparse.ArgumentParser(description = '...')


with open("output.txt", "w+") as output:
    subprocess.call(["python", "./script.py"], stdout=output);

if __name__ == '__main__':
    pass