envUrl = "https://konicabusinesssolutions-tst.cpq.cloud.sap"
tokenUrl = envUrl + "/basic/api/token"
payload = "grant_type=password&username=apac1-c4-admin@konicaminolta.com&password=Sap@1234567891"
response = RestClient.Post(tokenUrl, payload)
bearerToken = "Bearer " + str(response.access_token)
header = {'Authorization': bearerToken}
getTable = envUrl + "/api/custom-table/v1/customTables/" + "Product_Standard_Pricebook_A201_L1"
tableInfoRes = RestClient.Get(getTable, header)
body = {"value": [{"id": 12965,"columnName": "TEST","dbType": "DECIMAL","columnSize": 6,"isNullable": True,"isProtected": False,"isSensitive": False}]}
columns = ['ProductName', 'PriceGroup', 'FOBCost', 'LandedCost', 'StandardPrice', 'ListPrice', 'MonthlyRecurringCost', 'MonthlyRecurringStandardPrice', 'MonthlyRecurringListPrice', 'ThresholdLevel1', 'ThresholdLevel2', 'ThresholdLevel3', 'ThresholdLevel4', 'ThresholdLevel5', 'ThresholdLevelNumber', 'ValuationType', 'ValidFrom', 'ValidTo', 'Indicator1', 'Indicator2', 'Indicator3', 'LandedCostPlus', 'BottomPrice']
dataType = ['NVARCHAR', 'NVARCHAR', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'DECIMAL', 'INT', 'NVARCHAR', 'DATE', 'DATE', 'NVARCHAR', 'NVARCHAR', 'NVARCHAR', 'DECIMAL', 'DECIMAL',]
columnSize = ['250', '250', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', 'None', '250', 'None', 'None', '250', '250', '250', '6', '6']
#columns = [str(d["columnName"]) for d in tableInfoRes.columns]
#dataType = [str(d["dbType"]) for d in tableInfoRes.columns]
#columnSize = [str(d["columnSize"]) for d in tableInfoRes.columns]
Trace.Write(str(len(columns)))
Trace.Write(str(len(dataType)))
Trace.Write(str(len(columnSize)))
table = "Product_Standard_Pricebook_A201_L1"
#getTable = envUrl + "/api/custom-table/v1/customTables/" + table
#tableInfoRes = RestClient.Get(getTable, header)
updateColumn = envUrl + "/api/custom-table/v1/customTables/"+table+"/columns"
updateColumnRes = RestClient.Patch(updateColumn, body, header)
'''for i in range(len(columns)):
    if columns[i] not in ["ThresholdLevelNumber","ValidFrom","ValidTo"]:
        tBody = {"value": [{"id": 0,"columnName": columns[i],"dbType": dataType[i],"columnSize": columnSize[i],"isNullable": True,"isProtected": False,"isSensitive": False}]}
    else:
        tBody = {"value": [{"id": 0,"columnName": columns[i],"dbType": dataType[i],"isNullable": True,"isProtected": False,"isSensitive": False}]}
    updateColumn = envUrl + "/api/custom-table/v1/customTables/"+table+"/columns"
    updateColumnRes = RestClient.Patch(updateColumn, tBody, header)'''
====================================================================================
envUrl = "https://konicabusinesssolutions.cpq.cloud.sap"
tokenUrl = envUrl + "/basic/api/token"
payload = "grant_type=password&username=apac1-c4-admin@konicaminolta.com&password=Sap@1234567891"
response = RestClient.Post(tokenUrl, payload)
bearerToken = "Bearer " + str(response.access_token)
header = {'Authorization': bearerToken}
body = {"value": [{"id": 0,"columnName": "SalesCost","dbType": "DECIMAL","columnSize": 6,"isNullable": True,"isProtected": False,"isSensitive": False}]}
tables = [str(table.TableName) for table in SqlHelper.GetList("select TableName from DUMMY_TABLE_TABLES")]
Trace.Write(str(tables))
#tables = ["Product_CP_Pricebook_A201_L1", "Product_CP01_Pricebook_A201_L1", "Product_GMA_Pricebook_A201_L1", "Product_SATS_Pricebook_A201_L1", "Product_Standard_Pricebook_A201_L1", "Product_VITAL_A201_L1", "Product_Cons_Charge_A201_L1", "Product_USED_TSG1Y_A201_L1", "Product_USED_TSG3Y_A201_L1", "Product_EDUHUB_Pricebook_A201_L1", "Product_G1_Pricebook_A201_L1", "Product_G1002_Pricebook_A201_L1", "Product_G1076_Pricebook_A201_L1", "Product_G1116_Pricebook_A201_L1", "Product_G166_Pricebook_A201_L1", "Product_G243_Pricebook_A201_L1", "Product_G317_Pricebook_A201_L1", "Product_G322_Pricebook_A201_L1", "Product_G787_Pricebook_A201_L1", "Product_G938_Pricebook_A201_L1", "Product_GA13_Pricebook_A201_L1", "Product_AWWA_Pricebook_A201_L1", "Product_G386_Pricebook_A201_L1", "Product_G901_Pricebook_A201_L1", "Product_G1077_Pricebook_A201_L1", "Product_NUS_A201_L1", "Product_G1920_A201_L1", "Product_CP_A01_A201_L1", "Product_BSG024_A201_L1", "Product_BSG028_A201_L1", "Product_BSG042_A201_L1", "Product_BSG053_A201_L1", "Product_BSG058_A201_L1", "Product_BSG060_A201_L1", "Product_BSG064_A201_L1", "Product_BSG079_A201_L1", "Product_BSG080_A201_L1", "Product_BSG084_A201_L1", "Product_BSG085_A201_L1", "Product_BSG086_A201_L1", "Product_BSG105_A201_L1", "Product_BSG110_A201_L1", "Product_BSG111_A201_L1", "Product_BSG114_A201_L1", "Product_BSG116_A201_L1", "Product_BSG128_A201_L1", "Product_BSG138_A201_L1", "Product_BSG139_A201_L1", "Product_BSG156_A201_L1", "Product_BSG157_A201_L1", "Product_BSG165_A201_L1", "Product_BSG168_A201_L1", "Product_BSG170_A201_L1", "Product_BSG173_A201_L1", "Product_BSG176_A201_L1", "Product_BSG178_A201_L1", "Product_BSG179_A201_L1", "Product_BSG180_A201_L1", "Product_BSG181_A201_L1", "Product_BSG189_A201_L1", "Product_BSG190_A201_L1", "Product_BSG193_A201_L1", "Product_BSG195_A201_L1", "Product_BSG196_A201_L1", "Product_BSG197_A201_L1", "Product_BSG198_A201_L1", "Product_BSG199_A201_L1", "Product_BSG200_A201_L1", "Product_BSG145_A201_L1", "Product_BSG201_A201_L1", "Product_BSG203_A201_L1", "Product_BSG204_A201_L1", "Product_BSG205_A201_L1", "Product_BSG207_A201_L1", "Product_BSG208_A201_L1", "Product_BSG209_A201_L1", "Product_BSG210_A201_L1", "Product_BSG211_A201_L1", "Product_BSG212_A201_L1", "Product_BSG213_A201_L1", "Product_BSG214_A201_L1", "Product_BSG215_A201_L1", "Product_BSG216_A201_L1", "Product_BSG218_A201_L1", "Product_BSG219_A201_L1", "Product_BSG220_A201_L1", "Product_BSG221_A201_L1", "Product_BSG223_A201_L1", "Product_BSG224_A201_L1", "Product_BSG225_A201_L1", "Product_BSG226_A201_L1", "Product_BSG227_A201_L1", "Product_BSG228_A201_L1", "Product_BSG229_A201_L1", "Product_BSG230_A201_L1", "Product_BSG231_A201_L1", "Product_BSG232_A201_L1", "Product_BSG233_A201_L1", "Product_BSG234_A201_L1", "Product_BSG235_A201_L1", "Product_BSG236_A201_L1", "Product_BSG237_A201_L1", "Product_BSG238_A201_L1", "Product_BSG239_A201_L1", "Product_BSG240_A201_L1", "Product_BSG241_A201_L1", "Product_BSG244_A201_L1", "Product_BSG245_A201_L1", "Product_BSG246_A201_L1", "Product_BSG247_A201_L1", "Product_BSG248_A201_L1", "Product_BSG249_A201_L1", "Product_BSG250_A201_L1", "Product_BSG251_A201_L1", "Product_BSG252_A201_L1", "Product_BSG253_A201_L1", "Product_BSG254_A201_L1", "Product_BSG255_A201_L1", "Product_BSG256_A201_L1", "Product_BSG257_A201_L1", "Product_BSG258_A201_L1", "Product_BSG260_A201_L1", "Product_BSG259_A201_L1", "Product_BSG261_A201_L1", "Product_BSG262_A201_L1", "Product_BSG263_A201_L1", "Product_BSG264_A201_L1", "Product_BSG265_A201_L1", "Product_BSG266_A201_L1", "Product_BSG267_A201_L1", "Product_BSG268_A201_L1", "Product_BSG269_A201_L1", "Product_BSG270_A201_L1", "Product_BSG271_A201_L1", "Product_BSG272_A201_L1", "Product_BSG273_A201_L1", "Product_BSG274_A201_L1", "Product_BSG275_A201_L1", "Product_BSG276_A201_L1", "Product_BSG277_A201_L1", "Product_BSG278_A201_L1", "Product_BSG279_A201_L1", "Product_BSG280_A201_L1"]
for table in tables:
    getTable = envUrl + "/api/custom-table/v1/customTables/" + table
    tableInfoRes = RestClient.Get(getTable, header)
    if "columns" in tableInfoRes:
        if "SAlESCOST" not in [str(d["columnName"]) for d in tableInfoRes.columns]:
            updateColumn = envUrl + "/api/custom-table/v1/customTables/"+table+"/columns"
            updateColumnRes = RestClient.Patch(updateColumn, body, header)
            break
