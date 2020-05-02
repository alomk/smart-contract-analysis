import json
from subprocess import Popen, PIPE, STDOUT

FILE_PATH = "./data-000000000000"

counter = 332 # what index to start at

out = open(f"output{FILE_PATH[2:]}.txt","a")

with open(FILE_PATH, "r") as fp:
    lines = fp.readlines()

for i in range(counter, len(lines), 1):
    print(i)
    out.write(f"\nCOUNTER {counter}")
    p = Popen(['pakala', '-', '--exec-time','30', '--analysis-time', '30', '--max-transaction-depth', '5', '-z'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    p_stdout = p.communicate(input=bytes(json.loads(lines[i])['bytecode'][2:], "UTF-8"))
    out.write(str(p_stdout[0]))
    counter+=1

out.close()



