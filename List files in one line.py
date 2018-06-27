import os , stat
permissionDict = {
    'access': {
        '0': ('---'),
        '1': ('--x'),
        '2': ('-w-'),
        '3': ('-wx'),
        '4': ('r--'),
        '5': ('r-x'),
        '6': ('rw-'),
        '7': ('rwx')},}
for file in os.listdir("/etc"):
    if file.endswith(".d") or file.endswith(".conf") or file.endswith(".cnf"):
        print(os.path.join("/etc", file),end = " ",flush = True)
        permissionOctal = oct(os.lstat("/etc").st_mode)[-3:]
        for role, octal in enumerate(permissionOctal):
            print(permissionDict['access'][octal],end = " ",flush = True)

