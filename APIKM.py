envUrl = "https://konicabusinesssolutions-tst.cpq.cloud.sap"
tokenUrl = envUrl + "/basic/api/token"
payload = "grant_type=password&username=apac1-c4-admin@konicaminolta.com&password=Sap@1234567891"
response = RestClient.Post(tokenUrl, payload)
bearerToken = "Bearer " + str(response.access_token)
header = {'Authorization': bearerToken}
gsU = envUrl + "/api/script/v1/customactions?$top=200"
res = RestClient.Get(gsU, header)
for ca in res.pagedRecords:
    Trace.Write("")
    Trace.Write("")
    Trace.Write("")
    Trace.Write("")
    Trace.Write("")
    Trace.Write("######=========="+str(ca.actionDefinition.name)+"==========######")
    Trace.Write(str(ca.actionDefinition.script))
