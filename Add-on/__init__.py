import bpy


class xtPanel(bpy.types.Panel):
    ## i am no longer calling it xiv tools for obvious reasons thanks
    bl_label = "Luna Tools"
    bl_idname = "OBJECT_PT_lt"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_order = 0

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Active object is: " + obj.name, icon='CURSOR')

        row = layout.row()
        row.label(text="Merge verts & clean normals")

def register():
    bpy.utils.register_class(xtPanel)


def unregister():
    bpy.utils.unregister_class(xtPanel)


if __name__ == "__main__":
     register()
