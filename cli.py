import sys,os
for file in os.listdir("/etc"):
    input = open(os.path.join("/etc", file), "r")
    content = input.read()
    arg = sys.argv[0]
    i=1
    while i<len(arg):
        print(arg[i], arg[i+1], content)
        if(sys.argv[0]== '-c'):
            print(os.path.exists('/proc/cpuinfo'))
        if (sys.argv[0] == '-m'):
            print(os.path.exists('/proc/cpuinfo'))
        if (sys.argv[0] == '-f'):
            print(os.path.exists('/proc/cpuinfo'))
        if (sys.argv[0] == '-h'):
            print(os.path.exists('/proc/cpuinfo'))
        if (sys.argv[0] == '--help'):
            print("This is Help Message")
        i += 2
