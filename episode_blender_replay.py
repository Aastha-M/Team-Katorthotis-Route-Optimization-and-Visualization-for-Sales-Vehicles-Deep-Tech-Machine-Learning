import bpy
import math
ob=bpy.data.objects["j1"]
junc_pos=[]
for i in range(1,7):
    ob=bpy.data.objects['j'+str(i)]
    junc_pos.append(ob.location)
f=open(r'C:\Users\Abi\Documents\academics\projects\sales_vehicle\visualization\blender\episode_test.txt','r')
s=f.read()
lines=s.split('\n')
if(lines[len(lines)-1]==''):
    lines=lines[:len(lines)-1]
l1=lines[0].split(',')
src=int(l1[0])
des=int(l1[1])
pos_log=[]
pos=junc_pos[src]
pos_log.append(pos)
for i in lines[1:]:
    pos=junc_pos[int(i)]
    pos_log.append(pos)
angles=[]
for i in range(0,len(pos_log)-1):
    p1=pos_log[i]
    p2=pos_log[i+1]
    h=p2[1]-p1[1]
    b=p2[0]-p1[0]
    if(b==0):
        b=10**-10
    ang=math.atan(h/b)
    angles.append(ang)
    if(i==0):
        angles.append(ang)
ob=bpy.data.objects["truck"]
ob.select=True
frame_num=0
ob.rotation_mode='XYZ'
angles.append(angles[-1])
for i in range(len(pos_log)):
    bpy.context.scene.frame_set(frame_num)
    ob.location=pos_log[i]
    ob.rotation_euler=(0,0,angles[i])
    ob.keyframe_insert(data_path="location",index=-1)
    ob.keyframe_insert(data_path="rotation_euler",index=-1)
    frame_num+=2
    bpy.context.scene.frame_set(frame_num)
    ob.rotation_euler=(0,0,angles[i+1])
    ob.keyframe_insert(data_path="location",index=-1)
    ob.keyframe_insert(data_path="rotation_euler",index=-1)
    frame_num+=18
print(junc_pos)