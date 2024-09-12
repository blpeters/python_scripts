# ListingFields.py
# Arguments:
# D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb\Park_Boundary

import arcpy

# For each field in a feature class, print
# the field name, type, and length
fc = arcpy.GetParameterAsText(0)  # Get user input for a feature class
fields = arcpy.ListFields(fc)
desc = arcpy.Describe(fc)

print(f"The name of the feature class is {desc.name} \n It has fields: ")

for field in fields:
    print(f"{field.name}, which is a type of {field.type} with a length of {field.length}")
