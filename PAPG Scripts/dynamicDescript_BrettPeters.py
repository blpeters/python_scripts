# dynamicDescript_BrettPeters.py
# Uses arcpy to create a 300-ft buffer around a user-inputted feature class (0) for the
# portion of (0) that falls within the second user-inputted feature class (1)

import arcpy

arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"
arcpy.env.overwriteOutput = True

fc_in = arcpy.GetParameterAsText(0)  # fc to be processed (Campsites)
fc_clip = arcpy.GetParameterAsText(1)  # clipping fc (Backcountry_Camping_Areas)
fc_out = arcpy.GetParameterAsText(2)  # Desired name of resulting output feature class

arcpy.Clip_analysis(fc_in, fc_clip, "fc_in_clipped")
arcpy.Buffer_analysis("fc_in_clipped", fc_out, "300 feet")

# Print out the name and file path of each layer you use in the script
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    if (fc == fc_in) or (fc == fc_clip) or (fc == fc_out):
        desc = arcpy.Describe(fc)
        print(f"Feature Class Name: {desc.name}, Path: {desc.path}")
