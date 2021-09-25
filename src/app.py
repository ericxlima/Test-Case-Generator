import subprocess
import sys


if __name__ == '__main__':

    script = open('./bargage/script.py', 'r').read()
    inputs = open('./bargage/input.txt', 'r').read().split('\n\n')

    with open("./bargage/output.txt", "w+") as output_file:
        for case in inputs:
            result = subprocess.run([sys.executable, '-c', script],
                                    capture_output=True,
                                    text=True,
                                    input=case)
            print(result.stdout, '\n\n\n', result.stderr)
            #  result.stdout e result.stderr
        