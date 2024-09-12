import arcpy

arcpy.env.workspace =  r"D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"
arcpy.env.overwriteOutput = True

# Create a new table named Trees
arcpy.CreateTable_management(arcpy.env.workspace, "Trees")

# Add new attribute fields to the new table
arcpy.AddField_management("Trees","TREE_NAME", "TEXT")
arcpy.AddField_management("Trees","COUNT", "SHORT")

# Set a variable named 'fields' equal to the fields that will be modified within the 'Trees' table.
# Set a variable named 'row_values' that will be used when a new row is added to the table.
fields = ["TREE_NAME", "COUNT"]
row_values = ["Douglas Fir", 1800]

# Use Insert Cursor to establish a write cursor that will insert a new row into the table.
# Provide the cursor with the name of the table (Trees) as well as the field names that will be updated.
with arcpy.da.InsertCursor("Trees", fields) as cursor:
    cursor.insertRow(row_values)