import subprocess
import sys


if __name__ == '__main__':

    with open('./bargage/script.py', 'r') as script_file, \
         open('./bargage/input.txt', 'r') as input_file, \
         open("./bargage/output.txt", "w+") as output_file, \
         open("./bargage/raw_output.txt", "w+") as raw_output_file:
        
        script = script_file.read()
        inputs = input_file.read().split('\n\n')

        for index, case in enumerate(inputs):
            result = subprocess.run(
                [sys.executable, '-c', script],
                capture_output=True,
                text=True,
                input=case)
            output_file.write(f"> - Case {index}\n- **Input**:\n{case}\n- **Output**:\n" \
                              f"{result.stdout}{result.stderr}\n{'-' * 40}\n")
            raw_output_file.write(f">>>\n{case}\n\n{result.stdout}{result.stderr}\n\n\n")
