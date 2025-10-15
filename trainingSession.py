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
quote = context.Quote
quoteId = context.Quote.Id
quoteNumber = context.Quote.QuoteNumber
quoteOwnerId = context.Quote.OwnerId
quoteStatusName = context.Quote.StatusName
-------------------------------------------
changeStatus = context.Quote.ChangeStatus("Closed Won")
-------------------------------------------------------
To Get Custom Field Value
opptyName = context.Quote.GetCustomField("Opporunity_Name")
-----------------------------------------------------------
another way to get Quote Custom field value
region = context.Quote["Custom Field Name"]
--------------------------------------------------------------
To Set the value for a custom field
region = context.Quote.GetCustomField("Custom Field Name").Value = "Changed Name"
----------------------------------------------------------------------------------
currentRow = context.Cells[0].Row
if context.Cells[0].ColumnName == 'Principal' or context.Cells[0].ColumnName == 'Time_Period' or context.Cells[0].ColumnName == 'Rate_Of_Interest':
    for i in context.Cells[0].Row.Cells:
        if i.ColumnName == 'Final_Amount':
            i.Value = (((currentRow.GetColumnValue('Principal') * currentRow.GetColumnValue('Time_Period')) * currentRow.GetColumnValue('Rate_Of_Interest')) / 100) + currentRow.GetColumnValue('Principal')
        if i.ColumnName == 'Interest':
            i.Value = ((currentRow.GetColumnValue('Principal') * currentRow.GetColumnValue('Time_Period')) * currentRow.GetColumnValue('Rate_Of_Interest')) / 100
--------------------------------------------------------------------------------------------------------------------
a = SqlHelper.GetList("select top 1000 * from (select *, ROW_NUMBER() over (order by SYSTEM_ID) as r_n_n from products) xx where r_n_n >=1001")
------------------------------------------------------------------------------------------------------------------------
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
----------------------------------------------------------------------------------------------------------------------------------
productTypes = SqlHelper.GetFirst('select a.PRODUCTTYPE_NAME  from products as p inner join PRODUCT_TYPES_DEFN as a on p.PRODUCTTYPE_CD = A.PRODUCTTYPE_CD ')



for i in context.Quote.GetAllItems():
    ca = SqlHelper.GetFirst("select * from directory as a join directory_defn as b on a.DIRECTORY_CD = b.DIRECTORY_CD where a.PRODUCT_ID ='"+str(i.ProductId)+"'")
    Trace.Write(str(ca.DIR_NAME))
    
dir = SqlHelper.GetList("select * from(select *, ROW_NUMBER() OVER(  ORDER BY PRODUCT_ID) AS row from directory) as a where row > 1000")



cc= SqlHelper.GetList("select Distinct directory_cd as a from directory")
d=0
for i in cc:
    a=SqlHelper.GetFirst("select count(*) as b from directory inner join directory_defn on directory.directory_cd = directory_defn.directory_cd inner join products on directory.PRODUCT_ID = products.Product_Id where directory.directory_cd = '"+str(i.a)+"'")
    Trace.Write(str(a.b) + "====")
    d += a.b
Trace.Write("--"+str(d))----
------------------------------------
a = 0
lis = []
for i in range(9):
    quotes = SqlHelper.GetList("select top 1000 * from (select *, ROW_NUMBER() over (order by QuoteNumber) as r_n_n from sys_quote) xx where r_n_n >='"+str(a)+"'")
    a =  a + 1000
    for i in quotes:
        q = QuoteHelper.Get(str(i.QuoteNumber))
        if q.GetCustomField('ALS_LATAM_Tax_Total_quote') is not None:
            if q.GetCustomField('ALS_LATAM_Tax_Total_quote').Value != '0.00':
                Trace.Write(str(q.GetCustomField('ALS_LATAM_Tax_Total_quote').Value))
                lis.append(str(i.QuoteNumber))
Trace.Write(str(lis))
Trace.Write(len(lis))
-----------------------------------------------------------------------------------------------------------------------
def Create_Product(header,cpqUrl,i):
    body = {"SystemId":str(i.Item_Name + "_cpq"),"Name":i.Item_Name,"ProductTypeId":41,
            "Description":i.Item_Disc,
            "Categories":[{"Id":i.Category_ID,"Name":i.Category_Name,"Rank":i.Category_Rank}]}
    CPurl = cpqUrl+ "/setup/api/v1/admin/products"
    RestClient.Post(CPurl,body,header)


def Create_Attribute(header,cpqUrl,att,valueQ):
    if valueQ != None:
        lis = []
        dic = {}
        for val in valueQ:
            dic = {"valueCode":val.Value_Code,"value":val.Value,"systemId":str(val.Value_Code)+"_cpq","rank":val.Rank}
            lis.append(dic)
    body = {"name":att.Attribute_Name,"systemId":str(att.Attribute_Name)+"_cpq","type":att.Attribute_type,"typeLabel":att.Type_Label,
            "numberOfValues":att.No_Of_Values,"values":lis}
    CAurl = cpqUrl + "/api/products/v1/attributes"
    RestClient.Post(CAurl,body,header)

def MapAttributes(header,cpqUrl,ProductId,AttributeCode):
    MAurl = cpqUrl + "/setup/api/v1/admin/products/"+str(ProductId)+"/attributes/"+str(AttributeCode)+""
    RestClient.Post(MAurl,'',header)

def deleteProduct(id,headers):
    url = "https://sandbox.webcomcpq.com/setup/api/v1/admin/products/"+str(id)
    res = RestClient.Delete(url,headers)
    return None

def deleteAttribute(i,headers):
    url = "https://sandbox.webcomcpq.com/api/products/v1/attributes/"+str(i)
    res = RestClient.Delete(url,headers)
    return None

def GetProductAttributes(ProductId,headers):
    url = "https://sandbox.webcomcpq.com/setup/api/v1/admin/products/"+str(ProductId)+"/attributes"
    Response = RestClient.Get(url,headers)
    return Response

x
'''products = SqlHelper.GetList("select Distinct Item_Name from PRD_ATT_TEST_SK")
for i in products:
    productId = SqlHelper.GetFirst("select * from products where SYSTEM_ID = '"+str(i.Item_Name)+"_cpq"+"'")
    if productId == None or len(productId) == 0:
        pass
    else:
        deleteProduct(productId.PRODUCT_ID,header)

Attributes = SqlHelper.GetList("select Distinct Attribute_Name from PRD_ATT_TEST_SK")
for i in Attributes:
    a=str(i.Attribute_Name) + "_cpq"
    AttrId = SqlHelper.GetFirst("select * from ATTRIBUTE_DEFN where SYSTEM_ID = '"+a+"'")
    if AttrId == None or len(AttrId) == 0:
    
        pass
    else:
        deleteAttribute(AttrId.STANDARD_ATTRIBUTE_CODE,header)'''

Item_List = SqlHelper.GetList("select * from(select *, ROW_NUMBER() OVER(PARTITION BY Item_Name ORDER BY CpqTableEntryId) AS row from PRD_ATT_TEST_SK) as a where row = 1")
for i in Item_List:
    Item_id = SqlHelper.GetFirst("select * from products where SYSTEM_ID = '"+str(i.Item_Name)+"_cpq"+"'")
    if Item_id == None or len(Item_id)==0:
        ResP = Create_Product(header,cpqUrl,i)
        Attribute_List = SqlHelper.GetList("select * from(select *, ROW_NUMBER() OVER(PARTITION BY Attribute_Name ORDER BY CpqTableEntryId) AS row from PRD_ATT_TEST_SK) as a where row = 1")
        Attribute_L = SqlHelper.GetList("select * from PRD_ATT_TEST_SK where Item_Name = '"+i.Item_Name+"'")
        At_Li = []
        for data in Attribute_L:
            At_Li.append(data.Attribute_Name)
        for att in Attribute_List:
            if att.Attribute_Name in At_Li:
                Att_Code = SqlHelper.GetFirst("select STANDARD_ATTRIBUTE_CODE from ATTRIBUTE_DEFN where SYSTEM_ID='"+str(att.Attribute_Name)+"_cpq"+"' ")
                if Att_Code == None or len(Att_Code) == 0:
                    valueQ = SqlHelper.GetList("select Value_Code,Value,Rank from PRD_ATT_TEST_SK where Attribute_Name = '"+str(att.Attribute_Name)+"'")
                    ResA = Create_Attribute(header,cpqUrl,att,valueQ)
                    Product_Id = SqlHelper.GetFirst("select * from products where SYSTEM_ID = '"+str(i.Item_Name)+"_cpq"+"'")
                    Attribute_Code = SqlHelper.GetFirst("select * from ATTRIBUTE_DEFN where SYSTEM_ID = '"+str(att.Attribute_Name) + "_cpq"+"' ")
                    ProductAttributes = GetProductAttributes(Product_Id.PRODUCT_ID,header)
                    art = ProductAttributes.pagedRecords
                    lisa = []
                    for j in art:
                        lisa.append(int(j.standardAttributeCode))
                    if Attribute_Code is not None:
                        if Attribute_Code.STANDARD_ATTRIBUTE_CODE not in lisa:
                            ResPAM = MapAttributes(header,cpqUrl,Product_Id.PRODUCT_ID,Attribute_Code.STANDARD_ATTRIBUTE_CODE)
                        else:
                            pass
                else:
                    Product_Id = SqlHelper.GetFirst("select * from products where SYSTEM_ID = '"+str(i.Item_Name)+"_cpq"+"'")
                    Attribute_Code = SqlHelper.GetFirst("select * from ATTRIBUTE_DEFN where SYSTEM_ID = '"+str(att.Attribute_Name) + "_cpq"+"' ")
                    ProductAttributes = GetProductAttributes(Product_Id.PRODUCT_ID,header)
                    art = ProductAttributes.pagedRecords
                    lisa = []
                    for j in art:
                        lisa.append(int(j.standardAttributeCode))
                    if Attribute_Code is not None:
                        if Attribute_Code.STANDARD_ATTRIBUTE_CODE not in lisa:
                            ResPAM = MapAttributes(header,cpqUrl,Product_Id.PRODUCT_ID,Attribute_Code.STANDARD_ATTRIBUTE_CODE)
                        else:
                            pass
    else:
        Attribute_List = SqlHelper.GetList("select * from(select *, ROW_NUMBER() OVER(PARTITION BY Attribute_Name ORDER BY CpqTableEntryId) AS row from PRD_ATT_TEST_SK) as a where row = 1")
        Attribute_L = SqlHelper.GetList("select * from PRD_ATT_TEST_SK where Item_Name = '"+i.Item_Name+"'")
        At_Li = []
        for data in Attribute_L:
            At_Li.append(data.Attribute_Name)
        for att in Attribute_List:
            if att.Attribute_Name in At_Li:
                Att_Code = SqlHelper.GetFirst("select STANDARD_ATTRIBUTE_CODE from ATTRIBUTE_DEFN where SYSTEM_ID='"+str(att.Attribute_Name)+"_cpq"+"' ")
                if Att_Code == None or len(Att_Code) == 0:
                    valueQ = SqlHelper.GetList("select Value_Code,Value,Rank from PRD_ATT_TEST_SK where Attribute_Name = '"+str(att.Attribute_Name)+"'")
                    ResA = Create_Attribute(header,cpqUrl,att,valueQ)
                    Product_Id = SqlHelper.GetFirst("select * from products where SYSTEM_ID = '"+str(i.Item_Name)+"_cpq"+"'")
                    Attribute_Code = SqlHelper.GetFirst("select * from ATTRIBUTE_DEFN where SYSTEM_ID = '"+str(att.Attribute_Name) + "_cpq"+"' ")
                    ProductAttributes = GetProductAttributes(Product_Id.PRODUCT_ID,header)
                    art = ProductAttributes.pagedRecords
                    lisa = []
                    for j in art:
                        lisa.append(int(j.standardAttributeCode))
                    if Attribute_Code is not None:
                        if Attribute_Code.STANDARD_ATTRIBUTE_CODE not in lisa:
                            ResPAM = MapAttributes(header,cpqUrl,Product_Id.PRODUCT_ID,Attribute_Code.STANDARD_ATTRIBUTE_CODE)
                        else:
                            pass
                else:
                    Product_Id = SqlHelper.GetFirst("select * from products where SYSTEM_ID = '"+str(i.Item_Name)+"_cpq"+"'")
                    Attribute_Code = SqlHelper.GetFirst("select * from ATTRIBUTE_DEFN where SYSTEM_ID = '"+str(att.Attribute_Name) + "_cpq"+"' ")
                    ProductAttributes = GetProductAttributes(Product_Id.PRODUCT_ID,header)
                    art = ProductAttributes.pagedRecords
                    lisa = []
                    for j in art:
                        lisa.append(int(j.standardAttributeCode))
                    if Attribute_Code is not None:
                        if Attribute_Code.STANDARD_ATTRIBUTE_CODE not in lisa:
                            ResPAM = MapAttributes(header,cpqUrl,Product_Id.PRODUCT_ID,Attribute_Code.STANDARD_ATTRIBUTE_CODE)
                        else:
                            pass
