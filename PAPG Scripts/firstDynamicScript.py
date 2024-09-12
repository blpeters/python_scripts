# firstDynamicScript.py
# Description: A short script which demonstrates dynamic user input with ArcPy
# Requires a configuration file to dynamically input info.
# This is the firstDynamicConfig config at run button.

import os
import arcpy
arcpy.env.overwriteOutput = True

# Set the input workspace, get the feature class name to copy. and the output location
arcpy.env.workspace = arcpy.GetParameterAsText(0)
in_featureclass = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

in_fc = os.path.join(arcpy.env.workspace, in_featureclass)
print(f"We are copying the {in_fc} layer to the {out_workspace} directory")

# Copy feature class to output location
arcpy.CopyFeatures_management(in_fc, os.path.join(out_workspace, in_featureclass))

print("...")
print(f"Successfully copied the {in_fc} layer to the {out_workspace} directory")