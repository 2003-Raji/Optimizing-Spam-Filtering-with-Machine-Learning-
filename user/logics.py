from email_admin.models import SpamModel

def check():
    l=[]
    op={}
    gok=SpamModel.objects.values('spam_category').distinct()
    for t in gok:
        for tz,cc in t.items():
            for z in SpamModel.objects.filter(spam_category=cc):
                l.append(z.spam_list)
                op[tz]=l