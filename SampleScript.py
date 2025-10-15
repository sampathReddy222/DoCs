Apply Product Changes to save configuration on the container.

contWithChildProduct = Product.GetContainerByName("Container Name 1")
if contWithChildProduct is not None: 
    row1 = contWithChildProduct.AddNewRow("Container Row 1") 
    row1.Product.Attributes.GetByName("Attribute 1").AssignValue("1234") 
    row1.ApplyProductChanges()
    
        -----------------------------------------------------------------------------------------------------------------------------------

Edit Existing Configuration Without Opening Quote

In environments using Quote 2.0, you can use an endpoint to open an existing configuration of a quote item without having to open that quote first.
The endpoint can be used to directly edit the configuration by using the quoteId, itemId, and configurationId in the query string.
Consequently, users can now be redirected to the Configurator and the configuration can now be edited without executing the Edit action on a quote item.
In addition, you can use this endpoint to initiate a new configuration in the context of a specific quote.

This is a generic example URL for the new endpoint:

https://{installationUrl}/configurator/edit?quoteId={quoteId}&itemId={itemId}&configurationId={configurationId}

This example depicts what the URL looks like using real IDs:

https://devfl.webcomcpq.com/configurator/edit?quoteId=5491&itemId=2010&configurationId=be96b71c-8211-4546-abb5-6a2f87a4ae8b

        -------------------------------------------------------------------------------------------------------------------------------------

AddNewRow() method of IContainer triggers execution of rules by default.
If it's not needed, make sure to provide False parameter to optimize performance.

        -------------------------------------------------------------------------------------------------------------------------------------

Delete Quote Items  
    
for item in context.Quote.GetAllItems():
    context.Quote.DeleteItem(item.Id)
    
        -------------------------------------------------------------------------------------------------------------------------------------

Copy and reassign Quotes code

QuoteHelper.Reassign(str(QuoteHelper.Copy('03950051').QuoteNumber),'kolasam01')

        --------------------------------------------------------------------------------------------------------------------------------------
        
Works only on tab change event

a1 = context.PreviousTabId
Trace.Write('---------------' + str(a1)

        --------------------------------------------------------------------------------------------------------------------------------------

control Access Level of Quote Table based on custom field Value. works if it is executed as very end of all the script executions.

from Scripting.QuoteTables import AccessLevel
qt = context.Quote.QuoteTables['Well_Details']
wellName = context.Quote.GetCustomField('Well_Name').Value
if wellName == 'yes':
    qt.AccessLevel = AccessLevel.Hidden
elif wellName == 'no':
    qt.AccessLevel = AccessLevel.Editable
else:
    qt.AccessLevel = AccessLevel.ReadOnly
	

from Scripting.QuoteTables import AccessLevel, IQuoteTableCell, IQuoteTableRow
x = Quote.QuoteTables['PPC_Configurations'].Rows
for row in x:
    #Trace.Write(1)
    for cell in row.Cells:
        #Trace.Write(11)
        if cell.ColumnName == "Proposed_Rate":
            cell.AccessLevel = AccessLevel.Editable
            #Trace.Write(111)
    
        --------------------------------------------------------------------------------------------------------------------------------------

Control Access Level of Custom Fields. works if it is executed as very end of all the script executions.
   
Trace.Write('Script Started')
from Scripting.Quote import AccessLevel
testValue = context.Quote.GetCustomField("Quote_Name").Value
if testValue == "yes":
    Trace.Write("hide Access Level kkkkkkkkkkkkkkkk------------------------------")
    context.Quote.GetCustomField("Quote_Validity_(Days)").AccessLevel = AccessLevel.Hidden
else:
    Trace.Write("edit Access Level kkkkkkkkkkkkkkkk------------------------------")
    context.Quote.GetCustomField("Quote_Validity_(Days)").AccessLevel = AccessLevel.Editable
Trace.Write(str(context.Quote.GetCustomField("Quote_Validity_(Days)").AccessLevel))

        --------------------------------------------------------------------------------------------------------------------------------------
        
Sort Items in Items Table based on List Price

a = context.Quote.GetAllItems()
l = len(a)
b = filter(lambda x: x.RolledUpQuoteItem.Contains(".") == False, a)
b.sort(key=lambda x: float(x.ListPrice), reverse=True)
idList = []
for i,item in enumerate(b):
    idList.append(item.Id)
Trace.Write(str(idList))
x = len(b)
for i in range(x):
    for j in range(x-i-1):
        item = context.Quote.GetItemByItemId(idList[i])
        if item.RolledUpQuoteItem == str(x-i):
            break
        item.MoveDown()

        --------------------------------------------------------------------------------------------------------------------------------------
       
Calculate Section numbering and section wise totals

quote = QuoteHelper.Get('03120104')
sections = quote.GetSections()
for section in sections:
    items = quote.GetSectionItems(section)
    a = items[0]
    x = 1
    iSectionTotal = 0
    for item in items:
        item['ORIGINAL_OR_COPY'] = str(x)
        x += 1
        iSectionTotal += item['TEST_SECTION_CALC']
    quote.GetSection(section.SectionPath).Item['TEST_SECTION_CALC'] = iSectionTotal
    quote.GetSection(section.SectionPath).Item['List_Price'] = iSectionTotal
#x = context.Quote.Totals
#for i in context.Quote.GetAllItems():
#    i['TEST_SECTION_CALC'] = 1000
'''quote = QuoteHelper.Get('03120104')
sections = quote.GetSections()
for section in sections:
    quote.GetSection(section.SectionPath).Item['TEST_SECTION_CALC'] = 2000'''
    
        ----------------------------------------------------------------------------------------------------------------------------------------
        
Replace Tag
<*Eval(Replace("<*Value(Well Tool Size)*>","|","',"))*>

        ----------------------------------------------------------------------------------------------------------------------------------------
ApiResponseFactory.HtmlResponse(response.GetElementsByTagName("LoginKey")[0].InnerText)
        ----------------------------------------------------------------------------------------------------------------------------------------
Trace.Write(str(dir(context))) - gets all the properties and methods in the context. (try this in custom field change event script)
        ----------------------------------------------------------------------------------------------------------------------------------------
X = globals() - This will give all the objects available in the context
        ----------------------------------------------------------------------------------------------------------------------------------------
To find out which table has which columns, do an action while dev console is open in full mode and track the console by doing any action in quote. (mainly check the dbgateway in logger)
        -----------------------------------------------------------------------------------------------------------------------------------------
