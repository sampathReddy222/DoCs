Standrad scripts modules
---------------------------
from Scripting.Quote import MessageLevel
context.Quote.AddMessage("success",MessageLevel.Success,False)
context.Quote.AddMessage("Warning",MessageLevel.Warning,False)
context.Quote.AddMessage("Error",MessageLevel.Error,False)
context.Quote.AddMessage("Info",MessageLevel.Info,False)
context.Quote.AddMessage("success",MessageLevel.Success,True)
context.Quote.AddMessage("Warning",MessageLevel.Warning,True)
context.Quote.AddMessage("Error",MessageLevel.Error,True)
context.Quote.AddMessage("Info",MessageLevel.Info,True)
----------------------------------------------------------------
from Scripting.Quote import MessageLevel
for msg in context.Quote.Messages:
    Trace.Write(str(msg.MessageLevel)+str(msg.Content))
-----------------------------------------------
from Scripting.Quote import MessageLevel
for msg in context.Quote.Messages:
    context.Quote.DeleteMessage(msg.Id)
-----------------------------------------------------
