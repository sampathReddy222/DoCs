Print all container data
colms = []
cont = Product.GetContainerByName("SC_Models_Scope").Rows
for row in cont:
    for col in row.Columns:
        Trace.Write(col.Name)
        colms.append(str(col.Name))
    break
for row in cont:
    rowString = ""
    for col in colms:
        rowString += (str(col) + "	==	" + (row[col] if row[col] not in [None,""] else "") + "		")
    Trace.Write(str(rowString))
=================================================================================================================
Get attribute Name from Console

ko.contextFor($0).$data.name()
===================================================================================================================
