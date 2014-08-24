'''
Created on 24 Apr 2014

@author: corrupted
'''
from Objects import *
import sys
sys.path.append("/usr/lib/python3.4/site-packages")
import vdc_api_call
import bpy 
from mathutils import Vector

class Zone(base):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.mesh=bpy.data.meshes["Rack"]
        self.offset=(10,0,0)
        self.start=(0,0,0)
        self.scale=(5,5,5)
        self.scn = bpy.context.scene
        self.api=vdc_api_call.create_api_caller()
        self.zones=list()
        
    def get(self):
        ###Example
        return(self.api.listZones()["zone"])
    
    def populate(self):
        self.zones=self.get()
        self.build(self.zones)
       
    @classmethod
    def fetch(self,id):
        return(find("id",id)[0])
        