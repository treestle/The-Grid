import os,sys
sys.path.append(os.getcwd())
from Objects import Zone, VM

zone=Zone()
zone.populate()

vm=VM()
vm.populate()