def perm1(lst):
    if len(lst) == 0:
        return []       
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
            	l.append([x] + p)
            	print(l)
        return l
lst = ["a","b","c"]
a = perm1(lst)
'''x = "123"
print(x[:1])'''
------------------------------------------------------------------------------
# Function to create combinations
# without itertools
def n_length_combo(lst, n):
	
	if n == 0:
		return [[]]
	
	l =[]
	for i in range(0, len(lst)):
		
		m = lst[i]
		remLst = lst[i + 1:]
		
		remainlst_combo = n_length_combo(remLst, n-1)
		for p in remainlst_combo:
			l.append([m, *p])
		
	return l

# Driver code
if __name__=="__main__":
	arr ="abc"
	print(n_length_combo([x for x in arr], 2))
---------------------------------------------------------------------------------------------
from IET_AuthenticationModule import GetSFAuthToken
opId = context.Quote.GetCustomField('CPQ_SF_OPPORTUNITY_ID').Value
oppId = context.Quote.GetCustomField('IET_OpportunityId').Value
AUTH,ReqToken =  GetSFAuthToken()
headers = { 'Authorization': "Bearer " +str(ReqToken.access_token) }
OpportunityRes = RestClient.Get(str(AUTH.URL)+"/services/apexrest/IETCPQ/opportunityData/"+str(opId), headers)
----------------------------------------------------------------------------
from IET_AuthenticationModule import GetSFAuthToken
opId = context.Quote.GetCustomField('CPQ_SF_OPPORTUNITY_ID').Value
oppId = context.Quote.GetCustomField('IET_OpportunityId').Value
AUTH,ReqToken =  GetSFAuthToken()
headers = { 'Authorization': "Bearer " +str(ReqToken.access_token) }
OpportunityRes = RestClient.Get(str(AUTH.URL)+"/services/apexrest/IETCPQ/opportunityData/"+str(oppId), headers)
oppDetail = OpportunityRes.opportunityDetail
Trace.Write('-----'+str(oppDetail.opportunitySellingLegalEntityStreet)+'---------')
y = 
x = (str(oppDetail.opportunitySellingLegalEntityStreet) + ", ") if str(oppDetail.opportunitySellingLegalEntityStreet) != '' else '' + (str(oppDetail.opportunitySellingLegalEntityStreet) + ", ") if str(oppDetail.opportunitySellingLegalEntityStreet) != '' else '' + (str(oppDetail.opportunitySellingLegalEntityStreet) + ", ") if str(oppDetail.opportunitySellingLegalEntityStreet) != '' else '' + (str(oppDetail.opportunitySellingLegalEntityStreet) + ", ") if str(oppDetail.opportunitySellingLegalEntityStreet) != '' else ''
Trace.Write(x)
----------------------------------
from IET_AuthenticationModule import GetSFAuthToken
opId = context.Quote.GetCustomField('CPQ_SF_OPPORTUNITY_ID').Value
oppId = context.Quote.GetCustomField('IET_OpportunityId').Value
AUTH,ReqToken =  GetSFAuthToken()
headers = { 'Authorization': "Bearer " +str(ReqToken.access_token) }
OpportunityRes = RestClient.Get(str(AUTH.URL)+"/services/apexrest/IETCPQ/opportunityData/"+str(opId), headers)
oppDetail = OpportunityRes.opportunityDetail
Trace.Write('-----'+str(oppDetail.opportunitySellingLegalEntityStreet)+'---------')
custAddress = OpportunityRes.accountPrimaryContact
ab = str(custAddress.mainPhone) + ' ' + '''
    '''if str(custAddress.mainPhone) != '' else ''
ac = str(custAddress.mailingStreet) + '' + '''
    '''if str(custAddress.mailingStreet) != '' else ''
ad = str(custAddress.mailingPostalCode) + '' + '''
    '''if str(custAddress.mailingPostalCode) != '' else ''
ae = str(custAddress.mailingCountry) + '.' + '''
    '''if str(custAddress.mailingCountry) != '' else ''
af = str(custAddress.mailingCity) + ',' + '''
    '''if str(custAddress.mailingCity) != '' else ''
Trace.Write(ab)
r = (ab + ac + ad)
Trace.Write(r)
------------------------
a = SqlHelper.GetList("Select * from sys_Quote")
l = []
qm = []
for i in a:
    x=QuoteHelper.Get(str(i.QuoteNumber))
    #Trace.Write(str(x.Code))
    if str(x.SelectedMarket.Code) == "CAD":
        Trace.Write(str(i.QuoteNumber))
    if x.PricebookId == 1:
        #Trace.Write(str(i.QuoteNumber)[1:4])
        l.append(str(i.QuoteNumber)[1:4])
        qm.append(str(i.QuoteNumber))
Trace.Write(str(list(set(l))))
Trace.Write(str(len(qm)))
lis = list(set(l))
for j in lis:
    user = SqlHelper.GetFirst("Select name from Users where id = '"+str(j)+"'")
    Trace.Write(str(user.name))
[IF]([EQ](<*CTX( Quote.CustomField(IET_Is_Quote_Currency_Exists) )*>,Yes)){1}{0}[ENDIF]
