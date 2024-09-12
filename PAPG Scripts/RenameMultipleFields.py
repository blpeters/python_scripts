import arcpy

arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"

fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    if fc == "Backcountry_Camping_Areas_new":
        print(f"We are using Feature class: {fc}")
        fieldList = arcpy.ListFields(fc)
        for field in fieldList:
            if field.name == 'CampingAre':
                arcpy.AlterField_management(fc, field.name, 'CampingAreaName', 'CampingAreaName')
                print(f"Altered field name: {field.name} to CampingAreaName")
            elif field.name == 'Descriptio':
                arcpy.AlterField_management(fc, field.name, 'Description', 'Description')
                print(f"Altered field name: {field.name} to Description")
            elif field.name == 'Shape_Leng':
                arcpy.AlterField_management(fc, field.name, 'Perimeter', 'Camping Site Perimeter')
                print(f"Altered field name: {field.name} to Perimeter")
            else:
                print(f"Did not Alter Field Name: {field.name}")
    else:
        print(f"We are not using Feature Class {fc}")
print("Script Complete")