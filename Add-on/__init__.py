import bpy


class xtPanel(bpy.types.Panel):
    ## yeah im calling it xiv tools so what wanna fight about it
    bl_label = "XIV Tools"
    bl_idname = "OBJECT_PT_xt"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

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
