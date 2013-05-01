# Email program
# Reads emails

# Methods for all mailboxes
class EmailSystem:
    pass
    
    
# A single users mailbox / A user for the purposes of mail
class UserEmail:
    
    name = ""
    long_name = ""
    pwd = ""
    
    # Each email user maintains their own list
    sent_mail = []
    recieved_mail = []
    
    # TODO: Implement me later?
    # Do I even want this? Too ez?
    contacts = []
        
        
        
# A single email object
class Email:
    
    sender = None
    reciever = None
    contents = ""
    cc = []
    bcc = []
    access_tokens_required = ""
    draft = False
    read = False
    
    # Should only need this to make emails, no other setters or such
    def __init__(self, sender, reciever, contents, cc, bcc, access_tokens_required, draft):
        self.sender = sender
        self.reciever = reciever
        self.contents = contents
        self.cc = cc
        self.bcc = bcc
        self.access_tokens_required = access_tokens_required
        self.draft = draft
    
    