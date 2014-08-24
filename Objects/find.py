'''
Created on 24 Apr 2014

@author: corrupted
'''
import bpy 

def find(key,value):
    out=list()
    for obj in bpy.data.objects:
        if key in obj and obj[key] == value:
            out.append(obj)
    return(out)