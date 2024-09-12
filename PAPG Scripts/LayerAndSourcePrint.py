## LayerAndSourcePrint.py ##
# This script loops through a geodatabase and
# prints the Name and Data Source of each Layer
import arcpy
arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    desc = arcpy.Describe(fc)
    print(f"Layer name: {desc.name}")
    print(f"Layer data source: {desc.catalogPath}")
