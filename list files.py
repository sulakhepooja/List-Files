import os
for file in os.listdir("/etc"):
    if file.endswith(".d"):
        print(os.path.join("/etc", file))
    if file.endswith(".conf") or file.endswith(".cnf"):
        print(os.path.join("/etc", file))
