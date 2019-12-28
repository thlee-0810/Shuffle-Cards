'''
Your solution will be evaluated according to:
	• How you verify the correcness of the algorithm.
	• How well your test suite catches regressions.
	• How you construct your tests and test framework.
	• The maintenance burden of your suite.
	• Code clarity and documentation.
'''

import subprocess

# assgin your input and output test file name
input_file = 'test_data.txt'
output_file = input_file[:-4] + '_result.txt'

with open(output_file, 'w') as wf:
    with open(input_file) as f:
        i = 0
        # read the rows in the text file
        for line in f:
            process = subprocess.Popen(["python", "shuffle.py", line], stdout = subprocess.PIPE)
            stdout = process.communicate()[0]
            wf.write('Input: ' + line + 'Output: ' + str(stdout, 'utf-8'))
            i += 1
            # Tracking how many test cases finished
            if(i % 100 == 0):
                print('Test Cases: ', i)
        print('Total number of test cases: ', i)

    