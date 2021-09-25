import subprocess
import sys


if __name__ == '__main__':

    with open('./bargage/script.py', 'r') as script_file, \
         open('./bargage/input.txt', 'r') as input_file, \
         open("./bargage/output.txt", "w+") as output_file:
        
        script = script_file.read()
        inputs = input_file.read().split('\n\n')

        for index, case in enumerate(inputs):
            result = subprocess.run(
                [sys.executable, '-c', script],
                capture_output=True,
                text=True,
                input=case)
            output_file.write(f"Case {index}\n__Input__:\n{case}\n__Output__:\n{result.stdout}{result.stderr}\n\n\n")
