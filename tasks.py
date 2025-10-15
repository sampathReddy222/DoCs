Task 1 : Getting all the Part Numbers Except Parent Package Part Number.
p_cd = SqlHelper.GetFirst("select * from directory inner join directory_defn on directory.directory_cd = directory_defn.directory_cd where dir_name = 'ALS Packages'")
for i in context.Quote.GetAllItems():
    cd = SqlHelper.GetFirst("select DIRECTORY_CD from directory where PRODUCT_ID = '"+str(i.ProductId)+"'")
    if str(cd.DIRECTORY_CD) == str(p_cd.DIRECTORY_CD):
        pass
    else:
        Trace.Write(i.PartNumber)
________________________________________________________________________________________________
Task 2: Get all the items Details according to their respective categories
a = context.Quote.GetAllItems()
lis = []
trace = {}
refId = 1
quoteNumber = context.Quote.QuoteNumber
currency = context.Quote.GetCustomField("Currency").Value
for i in a:
    cd = SqlHelper.GetFirst("select dir_name from directory inner join directory_defn on directory.directory_cd = directory_defn.directory_cd where product_id = '"+str(i.ProductId )+"'")
    totalSP = i.ExtendedListPrice
    di = {}
    if str(cd.dir_name) not in trace:
        di["attributes"] = {"referenceId":str("ref"+str(refId)),"type":"sObject"}
        di["productName"] = str(cd.dir_name)
        di["totalPrice"] = totalSP
        di["quoteNumber"] = quoteNumber
        di["currency"] = str(currency)
        di["quantity"] = 1
        refId = refId + 1
        trace[str(cd.dir_name)] = str(cd.dir_name)
    else:
        for j in lis:
            if j["productName"] == str(cd.dir_name):
                j["totalPrice"] = int(j["totalPrice"]) + int(totalSP)
                j["quantity"] = int(j["quantity"]) + 1
    if di != {}:
        lis.append(di)
reqJson = {"records":lis}
Trace.Write(str(reqJson))
___________________________________________________________________________________________________
Task 3: Updating all the Quote Status from the quotes from Custom Table
quoteNumber = SqlHelper.GetList("select QUOTE_NUMBER from SRK_UPDATE_QUOTE_STATUS")
for i in quoteNumber:
    QuoteHelper.Get(str(i.QUOTE_NUMBER)).ChangeStatus("Quote in Draft / Preparation")

___________________________________________________________________________________________________
Task 4: Updating Quote details into a Quote Table
quoteNumbers = ["03440001","03440002","03440003","03440004"]
customTable = SqlHelper.GetTable("SRK_QUOTE_DATA_CUSTOM_TABLE")
customTableQN = SqlHelper.GetList("select QUOTE_NUMBER from SRK_QUOTE_DATA_CUSTOM_TABLE")
lis = []
for i in customTableQN:
    lis.append(str(i.QUOTE_NUMBER))
for i in quoteNumbers:
    quote = QuoteHelper.Get(str(i))
    quoteId = quote.Id
    region = quote.GetCustomField("Opportunity_Region").Value
    subRegion = quote.GetCustomField("Sub_Region").Value
    quoteName = quote.GetCustomField("Quote_Name").Value
    status = quote.StatusName
    if str(i) not in lis:
        tableRow = {"QUOTE_NUMBER":str(i),"QUOTE_NAME":str(quoteName),"QUOTE_ID":str(quoteId),"REGION":str(region),"SUB_REGION":str(subRegion),"STATUS":str(status)}
        customTable.AddRow(tableRow)
        SqlHelper.Upsert(customTable)
    else:
        cpqId = SqlHelper.GetFirst("select CpqTableEntryId from SRK_QUOTE_DATA_CUSTOM_TABLE")
        tableRow = {"QUOTE_NUMBER":str(i),"QUOTE_NAME":str(quoteName),"QUOTE_ID":str(quoteId),"REGION":str(region),"SUB_REGION":str(subRegion),"STATUS":str(status),"CpqTableEntryId":int(cpqId.CpqTableEntryId)}
        customTable.AddRow(tableRow)
        SqlHelper.Upsert(customTable)

#quote = QuoteHelper.Get('03440001')
___________________________________________________________________________________________________
GETTING RANGE OF ENTRIES FORM THE SYSTEM TABLES

a = SqlHelper.GetList("select top 1000 * from (select *, ROW_NUMBER() over (order by SYSTEM_ID) as r_n_n from products) xx where r_n_n >=1001")
___________________________________________________________________________________________________
GETTING COUNT OF ITEMS IN EACH CATEGORY

a = SqlHelper.GetList('select * from directory')
d = {}
for i in a:
    di = SqlHelper.GetFirst("select * from products where product_id = '"+str(i.PRODUCT_ID)+"'")
    if str(di.PRODUCT_ID) in d:
        d[str(di.PRODUCT_ID)] = int(d[str(di.PRODUCT_ID)]) + 1
        Trace.Write(di.PRODUCT_ID)
    else:
        d[str(di.PRODUCT_ID)] = 1
Trace.Write(str(d))
Trace.Write(str(count))
______________________________________________________________________________________________________
GETTING PRODUCT TYPE OF PRODUCT

productTypes = SqlHelper.GetFirst('select a.PRODUCTTYPE_NAME  from products as p inner join PRODUCT_TYPES_DEFN as a on p.PRODUCTTYPE_CD = A.PRODUCTTYPE_CD ')
_______________________________________________________________________________________________________
