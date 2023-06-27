import bpy
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=0.0001, use_sharp_edge_from_normals=True)
bpy.ops.object.mode_set(mode='OBJECT')
