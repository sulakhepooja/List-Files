import sys,os
with open('/proc/cpuinfo') as f:
    for line in f:
        if line.strip():

            if line.rstrip('\n').startswith('model name'):
                model_name = line.rstrip('\n').split(':')[1]
                print(model_name)
        if line.strip():

            if line.rstrip('\n').startswith('cpu cores'):
                cpu_cores = line.rstrip('\n').split(':')[1]
                print(cpu_cores)
        if line.strip():

            if line.rstrip('\n').startswith('vendor_id'):
                vendor_id = line.rstrip('\n').split(':')[1]
                print(vendor_id)
        if line.strip():

            if line.rstrip('\n').startswith('cpu family'):
                cpu_family = line.rstrip('\n').split(':')[1]
                print(cpu_family)
        if line.strip():

            if line.rstrip('\n').startswith('cpu MHz'):
                cpu_MHz = line.rstrip('\n').split(':')[1]
                print(cpu_MHz)

