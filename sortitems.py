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
