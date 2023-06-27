import bpy


bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', vert_mapping='EDGEINTERP_NEAREST', layers_select_src='NAME', layers_select_dst='ALL', mix_mode='REPLACE')
bpy.ops.object.mode_set(mode='OBJECT')
