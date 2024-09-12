# Using your knowledge of loops and the Describe function, complete the following
# code blocks to describe the Park_Roads feature class located in the GrandTeton geodatabase.

import arcpy
import os

# Set the workspace environment
arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"

# Using the describe object, Print the spatial reference name
spatialRef = arcpy.Describe('Park_Roads').spatialReference
print(spatialRef.name)

# Make a list of fields from the Roads feature class
featureClass = 'Park_Roads'
fieldList = arcpy.ListFields(featureClass)

# Loop through each field in the list and print the name
for field in fieldList:
    print(field.name)


