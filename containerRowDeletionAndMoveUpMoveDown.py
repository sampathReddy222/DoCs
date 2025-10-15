container=Product.GetContainerByName('Well Selected Materials')
Personal_Row_Indexes = []
for row in container.Rows:
    if row['DocSectionName'] == 'Personnel' and row['IncludeOrItemize'] == 'Included':
        Personal_Row_Indexes.append(row.RowIndex)
    Trace.Write('-------------'+str(row.RowIndex)+'--------------------')
Trace.Write(str(Personal_Row_Indexes))
container.DeleteRow(Personal_Row_Indexes[0])
x = 1
for j in Personal_Row_Indexes[1:]:
    Trace.Write('Deleting Index' + '----------------' + str(j-x))
    container.DeleteRow(j-x)
    x = x + 1
----------------------------------------------------------------------------------------------------------------------------------------------------
container = Product.GetContainerByName("Well Selected Materials")
aligned_Rows_Count = 1
while container.Rows.Count+1 != aligned_Rows_Count:
    latest_row = container.Rows.Count - aligned_Rows_Count
    while container.Rows[latest_row]['IncludeOrItemize'] == 'Included' and container.Rows[latest_row]['DocSectionName'] != container.Rows[latest_row-1]['DocSectionName']:
        container.MoveRowUp(int(container.Rows[latest_row].RowIndex))
        Trace.Write(latest_row)
        latest_row = latest_row - 1
    aligned_Rows_Count = aligned_Rows_Count + 1
    Trace.Write(aligned_Rows_Count)
