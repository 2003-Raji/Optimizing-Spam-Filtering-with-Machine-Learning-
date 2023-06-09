import operator
import re
from heapq import nlargest

from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from email_admin.models import SpamModel
from user.forms import RegisterForms
from user.models import RegisterModel, SendmailModel, FeedbackModel


def index(request):
    if request.method=="POST":
        usid=request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid,password=pswd)
            request.session['userid']=check.id
            return redirect('userpage')
        except:
            pass
    return render(request,'user/index.html')
def register(request):
    if request.method=="POST":
        forms=RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms=RegisterForms()
    return render(request,'user/register.html',{'form':forms})
def userpage(request):
    uid = request.session['userid']
    request_obj = RegisterModel.objects.get(id=uid)
    se=''
    pos = []
    neg=[]
    oth =[]
    mm=''
    sa=''
    ro=0
    cat=''
    ss=''
    cos=[]
    sos=[]
    tos=[]
    vos=[]

    edcount, bcount, scount, fcount, acount, ecount, hcount,ocount = 0, 0, 0, 0, 0, 0, 0,0
    edw, bw, sw, fw, aw, ew, hw,oth = [], [], [], [], [], [], [],[]
    if request.method=="POST":
        to1=request.POST.get('to')
        sub = request.POST.get('subject')
        cht = request.POST.get('chat')
        to_mail = request_obj.email
        c = (re.findall(r"[\w']+", str(cht)))
        for f in c:

            if f in ('agitate','argue','clamor','combat','contend','contest','dispute','feud','oppugn',
                     'skirmish','strive','tug','wrestle','clamor','contest','dispute','feud','oppugn',
                     'skirmish','agitate','argue','clamor','combat','contend','carnage','purge','slaughter',
                     'argue','battle','brawl','buckcombat','conflict','contend','crossswords','differ','disagree',
                     'encounter','feud','fret','gall','grapple','grate','quarrel','wrangle','buck','clash','contend',
                     'contest','cope','defy','dispute','battle',' duel','engage','fight','oppose','repel','bom','attack',):

                pos.append(f)
            elif f in ('weapon','doomsday ','machine','mininuke','mirv','nuke','H-bomb','nuke','Dagger','Falchion','Katana','Knife','Longsword','Shortsword','Ulfberht','Estoc','Rapier','Club','Flail','Mace','Pernach','Shestophor','Maul','Quarterstaff','Bludgeon','Ahlspiess','Bardiche','Bill','Glaive','Guisarme','Lance','hammer','Partisan','Pike','Ranseur','Sovnya','Spetum','Swordstaff','Voulge','War-scythe','hammer','Bow','Longbow','Crossbow','Arbalest','Ballista','crossbow','Sling','weapons','Chakram','Francisca','Kunai','Spear','Shuriken','Culverin','cannon','Arquebus','Musket','Ranged',):

                neg.append(f)
            elif f in (
            'brutal', 'crazy', 'cruel', 'fierce', 'homicidal', 'hysterical', 'murderous', 'passionate', 'potent',
            'powerful', 'savage', 'uncontrollable', 'vicious', 'agitated', 'aroused', 'berserk', 'bloodthirsty',
            'coercive', 'demoniac', 'desperate', 'distraught', 'disturbed', 'enraged', 'fiery', 'forceful', 'forcible',
            'frantic', 'fuming', 'furious', 'great', 'headstrong', 'hotheaded', 'impassioned', 'impetuous', 'inflamed',
            'intemperate', 'mad', 'maddened', 'maniacal', 'mighty', 'raging', 'riotous', 'rough', 'strong',
            'ungovernable', 'unrestrained', 'urgent', 'vehement', 'wild', 'acute', 'cutting', 'distressing',
            'excruciating', 'exquisite', 'fierce', 'keen', 'overpowering', 'overwhelming', 'piercing', 'poignant',
            'powerful', 'racking', 'severe', 'sharp', 'shooting', 'stabbing', 'sudden', 'violent', 'agonizing',
            'disturbing', 'excruciating', 'extreme', 'fierce', 'harrowing', 'intense', 'racking', 'struggling',
            'tearing', 'tormenting', 'tortuous', 'torturing', 'vehement',):
                cos.append(f)
            elif f in (
                    'threateningly', 'threateners', 'threatening', 'threatener', 'threatened', 'threating', 'threatens',
                    'threaten', 'threated', 'threats', 'counterthreat', 'blackmail', 'hazard', 'intimidation', 'menace',
                    'peril', 'risk', 'bluff', 'commination', 'fix', 'foreboding', 'foreshadowing', 'fulmination',
                    'impendence', 'omen', 'portent', 'presage', 'thunder', 'bugbear', 'apprehension', 'bogey', 'bogy',
                    'boogeyman', 'bugaboo', 'dread', 'fear', 'goblin', 'gremlin', 'hobgoblin', 'loup-garou', 'ogre',
                    'problem', 'scare', 'specter', 'terror', 'threat', 'wraith', 'dare', 'defiance', 'demanding',
                    'demur', 'ultimatum', 'remonstrance', 'summons to contest', 'coercion', 'browbeating',):
                sos.append(f)
            elif f in (
            'corrupt', 'deplorable', 'illegal', 'illegitimate', 'illicit', 'immoral', 'scandalous', 'senseless',
            'unlawful', 'vicious', 'bent', 'heavy', 'racket', 'wildcat', 'wrong', 'caught', 'crooked', 'culpable',
            'dirty', 'hung up', 'indictable', 'iniquitous', 'nefarious', 'peccant', 'shady', 'unrighteous',
            'villainous', 'wicked', 'banned', 'criminal', 'illicit', 'unconstitutional', 'unlawful', 'base', 'corrupt',
            'criminal', 'delinquent', 'evil', 'iniquitous', 'mean', 'reprobate', 'sinful', 'vicious', 'vile',
            'villainous', 'wicked', 'wrong', 'brigand', 'criminal', 'crook', 'desperado', 'forager', 'gangster',
            'gunperson', 'highwayperson',):
                 tos.append(f)
            elif f in (
                    'smuggling', 'rum-running', 'stealing', 'prostitution', 'slavery', 'bootlegging', 'counterfeiting',
                     'dealing', 'goods', 'moonshine', 'piracy', 'plunder', 'poaching', 'rum-running',
                    'smuggling', 'stuff', 'swag', 'theft', 'trafficking', 'violation', 'wetbacking',
                    'hijacking''infringement', 'plagiarism', 'theft', 'bootlegging', 'buccaneering', 'rapine',
                    'stealing', 'swashbuckling', 'commandeering', 'freebooting', 'marauding', 'pirating', 'bootlegging',
                    'counterfeiting', 'moonshine', 'piracy', 'plunder', 'poaching', 'rum-running', 'smuggling',
                    'stuff', 'swag', 'theft', 'trafficking', 'violation', 'wetbacking', 'carjack', 'commandeer',
                    'kidnap', 'steal', 'shanghai', 'skyjack', 'annex', 'borrow', 'clap', 'confiscate', 'cop',
                    'embezzle', 'filch', 'grab', 'hijack', 'liberate', 'lift', 'misappropriate', 'pilfer',):
                vos.append(f)

        if len(pos)>len(neg) and len(pos)>len(cos) and len(pos)>len(sos) and len(pos)>len(tos) and len(pos)>len(vos):
            cat="war"
        elif len(neg)>len(pos) and len(neg)>len(cos) and len(neg)>len(sos) and len(neg)>len(tos) and len(neg)>len(vos):
            cat="Weapon"
        elif len(cos)>len(pos) and len(cos)>len(neg) and len(cos)>len(sos) and len(cos)>len(tos) and len(cos)>len(vos):
            cat="Violence"
        elif len(sos)>len(pos) and len(sos)>len(neg) and len(sos)>len(cos) and len(sos)>len(tos) and len(sos)>len(vos):
            cat="Threat"
        elif len(tos)>len(pos) and len(tos) > len(neg) and len(tos) > len(cos) and len(tos) > len(sos) and len(tos) > len(vos):
            cat = "Crime"
        elif len(vos)>len(pos) and len(vos) > len(neg) and len(vos) > len(cos) and len(vos) > len(sos) and len(vos) > len(tos):
            cat = "trafficking"
        else:
            cat="other"
        ss=len(pos)

    if (len(pos)>0):
        sa='spam'
    elif(len(neg)>0):
        sa='spam'
    elif(len(cos)>0):
        sa='spam'
    elif (len(sos) > 0):
        sa = 'spam'
    elif (len(tos) > 0):
        sa = 'spam'
    elif (len(vos) > 0):
        sa = 'spam'
    else:
        sa='inbox'
    if request.method=="POST":
        to1=request.POST.get('to')
        sub = request.POST.get('subject')
        cht = request.POST.get('chat')
        to_mail = request_obj.email
        SendmailModel.objects.create(sendermail=to_mail, to=to1, subject=sub, chat=cht, spam=sa, category=cat)
    return render(request,'user/userpage.html',{'obj':ss,'a':cat,'ji':sa,})
def viewmailpage(request):
    uid = request.session['userid']
    request_obj = RegisterModel.objects.get(id=uid)
    to_mail = request_obj.email
    obj=SendmailModel.objects.filter(to=to_mail,spam='inbox')
    return render(request,'user/viewmailpage.html',{'form':obj})
def spampage(request):
    uid = request.session['userid']
    request_obj = RegisterModel.objects.get(id=uid)
    to_mail = request_obj.email
    obj = SendmailModel.objects.filter(to=to_mail, spam='spam')
    return render(request,'user/spampage.html',{'objects':obj})

def logout(request):
    return redirect('index')

def deleteobj(request,pk):
    obj = get_object_or_404(SendmailModel, pk=pk)
    obj.delete()
    return redirect('viewmailpage')
def spamdeleteobj(request,pk):
    obj = get_object_or_404(SendmailModel, pk=pk)
    obj.delete()
    return redirect('spampage')

def mydetails(request):
    usid=request.session['userid']
    us_id=RegisterModel.objects.get(id=usid)
    return render(request,'user/mydetails.html',{'obje':us_id})
def updatemydetails(request):
    userid = request.session['userid']
    objec = RegisterModel.objects.get(id=userid)
    if request.method == "POST":
        FirstName = request.POST.get('FirstName', '')
        LastName = request.POST.get('LastName', '')
        UserId = request.POST.get('UserId', '')
        Password = request.POST.get('Password', '')
        MobileNumber = request.POST.get('MobileNumber', '')
        EmailId = request.POST.get('EmailId', '')
        Gender = request.POST.get('Gender', '')

        obj = get_object_or_404(RegisterModel, id=userid)
        obj.firstname = FirstName
        obj.lastname = LastName
        obj.userid = UserId
        obj.password = Password
        obj.mblenum = MobileNumber
        obj.email = EmailId
        obj.gender = Gender

        obj.save(update_fields=["firstname", "lastname", "userid", "password", "mblenum", "email",
                                "gender", ])
        return redirect('mydetails')

    return render(request,'user/updatemydetails.html',{'obj': objec})

def feedback(request):
    uid = request.session['userid']
    objec = RegisterModel.objects.get(id=uid)
    if request.method == "POST":
        feed = request.POST.get('feedback')
        FeedbackModel.objects.create(username=objec, feedback=feed)
    return render(request,'user/feedback.html')

