import arcpy
arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"
arcpy.env.overwriteOutput = True
fcList = arcpy.ListFeatureClasses("")
# Make a for loop
for fc in fcList:
    # set up an if / else statement
    if fc == "Park_Trails" or fc == "Trail_Points":
        print("Some of our data are Park Trails and Trail Points.")
    # use an elif statement
    elif fc == "Campsites" or fc == "Backcountry_Camping_Areas":
        print("Some of our data are Campsites and Backcountry Camping Areas.")
    # finish the conditionals by using an else: statement
    else:
        print("Some data are neither Park Trails, Trail Points, Campsites, or Backcountry Camping Areas")