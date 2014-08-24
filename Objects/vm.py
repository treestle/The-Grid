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

class VM(base):
    """Class Docs"""
    
    def __init__(self):
        self.mesh=bpy.data.meshes["Server"]
        self.offset=(0,0,1) 
        self.start=(0,0,0) 
        self.scale=(5,5,5)
        self.scn = bpy.context.scene
        self.api=vdc_api_call.create_api_caller()
        self.VM=list()
        self.vdc_offset=dict()
        
    def get(self):
        ###Example
        return(self.api.listVirtualMachines()["virtualmachine"])
    
    def populate(self):
        self.vms=self.get()
        self.build(self.vms)
       
    def build(self, lst):
        for item in lst:
            ob=bpy.data.objects.new("{0} - {1}".format(self.__class__.__name__,item["name"]),self.mesh)
            vdc_obj=self.fetch(item["zoneid"])
            vdc_x,vdc_y,vdc_z=vdc_obj.location
            x=vdc_x
            y=vdc_y
            z=vdc_z
            if item["zoneid"] in self.vdc_offset:
                x+=self.vdc_offset[item["zoneid"]]["x"]
                y+=self.vdc_offset[item["zoneid"]]["y"]
                z+=self.vdc_offset[item["zoneid"]]["z"]
                self.vdc_offset[item["zoneid"]]["x"]+=self.offset[0]
                self.vdc_offset[item["zoneid"]]["y"]+=self.offset[1]
                self.vdc_offset[item["zoneid"]]["z"]+=self.offset[2]
            else:
                self.vdc_offset[item["zoneid"]]=dict()
                self.vdc_offset[item["zoneid"]]["x"]=self.offset[0]
                self.vdc_offset[item["zoneid"]]["y"]=self.offset[1]
                self.vdc_offset[item["zoneid"]]["z"]=self.offset[2]
            ob.location=Vector((x,y,z))
            ob.scale=Vector(self.scale)
            for key,value in item.items():
                ob[key]=value
            self.scn.objects.link(ob)
       
    @classmethod
    def fetch(self,id):
        return(find("id",id)[0])
        