import sys,os
for file in os.listdir("/etc"):
    input = open(os.path.join("/etc", file), "r")
    content = input.read()
    arg = sys.argv[0]
    i=1
    while i<len(arg):
        print(arg[i], arg[i+1], content)
        i+=2
