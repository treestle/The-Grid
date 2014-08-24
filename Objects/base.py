import sys
sys.path.append("/usr/lib/python3.4/site-packages")
import vdc_api_call
import bpy 
from mathutils import Vector

class base(object):
    
    def __init__(self):
        self.mesh=mesh
        self.offset=(2,2,2) 
        self.start=(0,0,0)
        self.scale=(0.9,0.9,0.9)
        self.scn = bpy.context.scene
        self.api=vdc_api_call.create_api_caller()
        
    def get(self):
        ###Example
        return(self.api.listZones()["zone"])
    
    def build(self, lst):
        x=self.start[0]
        y=self.start[1]
        z=self.start[2]
        for item in lst:
            ob=bpy.data.objects.new("{0} - {1}".format(self.__class__.__name__,item["name"]),self.mesh)
            ob.location=Vector((x,y,z))
            ob.scale=Vector(self.scale)
            for key,value in item.items():
                ob[key]=value
            self.scn.objects.link(ob)
            x+=self.offset[0]
            y+=self.offset[1]
            z+=self.offset[2]
            
    

    