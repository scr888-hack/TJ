# Please do not replace the text anything but sc.e
# Ini sc gratisan tolong hargain yg buat dict!
# Rework by Yepz
# Id : Myyepz
# Thanks to team hello world
# -*- coding: utf-8 -*-
'''
Free to use, all credits belong to me, Zero Cool.
Do not sell or rent it!
© 2018 Self Bot
'''
from important import *
import pytz, datetime, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia, html5lib
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
import requests

# Setup Argparse
parser = argparse.ArgumentParser(description='Selfbot Self Bot')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--apptype', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()


# Login Client
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
try:
    print ('##----- LOGIN CLIENT -----##')
    line = None
    if args.apptype:
        tokenPath = Path('authToken.txt')
        if tokenPath.exists():
            tokenFile = tokenPath.open('r')
        else:
            tokenFile = tokenPath.open('w+')
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else args.email
        try:
            line = LINE(idOrToken, args.passwd, appType=args.apptype, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
            tokenFile.close()
            tokenFile = tokenPath.open('w+')
            tokenFile.write(line.authToken)
            tokenFile.close()
        except TalkException as talk_error:
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            sys.exit('++ Error : %s' % talk_error.reason.replace('_', ' '))
        except Exception as error:
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit('++ Error : %s' % str(error))
    else:
        for appType in listAppType:
            tokenPath = Path('authToken.txt')
            if tokenPath.exists():
                tokenFile = tokenPath.open('r')
            else:
                tokenFile = tokenPath.open('w+')
            savedAuthToken = tokenFile.read().strip()
            authToken = savedAuthToken if savedAuthToken and not args.token else args.token
            idOrToken = authToken if authToken else args.email
            try:
                line = LINE(idOrToken, args.passwd, appType=appType, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
                tokenFile.close()
                tokenFile = tokenPath.open('w+')
                tokenFile.write(line.authToken)
                tokenFile.close()
                break
            except TalkException as talk_error:
                print ('++ Error : %s' % talk_error.reason.replace('_', ' '))
                if args.traceback: traceback.print_tb(talk_error.__traceback__)
                if talk_error.code == 1:
                    continue
                sys.exit(1)
            except Exception as error:
                print ('++ Error : %s' % str(error))
                if args.traceback: traceback.print_tb(error.__traceback__)
                sys.exit(1)
except Exception as error:
    print ('++ Error : %s' % str(error))
    if args.traceback: traceback.print_tb(error.__traceback__)
    sys.exit(1)

if line:
    print ('++ Auth Token : %s' % line.authToken)
    print ('++ Timeline Token : %s' % line.tl.channelAccessToken)
    print ('##----- LOGIN CLIENT (Success) -----##')
else:
    sys.exit('##----- LOGIN CLIENT (Failed) -----##')
#Yepzgans
myMid = line.profile.mid
programStart = time.time()
oepoll = OEPoll(line)
admin = ["u24d5f93f9113c991342c079005467e2f"]
tmp_text = []
lurking = {}
tokenz= {}
#Yepzgans
settings = livejson.File('setting.json', True, False, 4)
#Yepzgans
bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}
# Backup profile
profile = line.getContact(myMid)
settings['myProfile']['displayName'] = profile.displayName
settings['myProfile']['statusMessage'] = profile.statusMessage
settings['myProfile']['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail['result']['objectId']
settings['myProfile']['coverId'] = coverId

# Check Json Data
if not settings:
    print ('##----- LOAD DEFAULT JSON -----##')
    try:
        default_settings = line.server.getJson('https://17hosting.id/default.json')
        settings.update(default_settings)
        print ('##----- LOAD DEFAULT JSON (Success) -----##')
    except Exception:
        print ('##----- LOAD DEFAULT JSON (Failed) -----##')

def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))

def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd
   
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': myMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))
        
def changeProfileVideo(to):
    if settings['changevp']['picture'] == None:
        return yepzLove(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == None:
        return yepzLove(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = line.genOBSParams({'oid': line.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return yepzLove(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = False
        line.updateProfilePicture(path_p, 'vp')

def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')

def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')
    
#DEFFTEMPLATE
def sendTemplate(group, data):
    warna1 = ("#0000FF","#000000","#05092A","#00BFFF","#708090","#800000","#FF0000","#E9967A","#DDA0DD")
    warnanya1 = random.choice(warna1)
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    warna1 = ("#0000FF","#000000","#05092A","#00BFFF","#708090","#800000","#FF0000","#E9967A","#DDA0DD")
    warnanya1 = random.choice(warna1)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate(gr, data):
    warna1 = ("#0000FF","#000000","#05092A","#00BFFF","#708090","#800000","#FF0000","#E9967A","#DDA0DD")
    warnanya1 = random.choice(warna1)
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate2(friend, data):
    warna1 = ("#0000FF","#000000","#05092A","#00BFFF","#708090","#800000","#FF0000","#E9967A","#DDA0DD")
    warnanya1 = random.choice(warna1)
    xyz = LiffChatContext(friend)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

uagent = {
    "User-Agent": "Mozilla\t5.0"
}

def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)
    
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
    
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "</ Error >",
            "iconUrl": "https://obs.line-scdn.net/{}".format(line.getContact("u65129423a63f75ecae3ea189f9540054").pictureStatus),
            "linkUrl": "line://nv/profilePopup/mid=u65129423a63f75ecae3ea189f9540054"
        }
    }
    sendTemplate(to, data)
    
def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)

def yepzLove(to, text):
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
    "styles": {
    "footer": {
    "backgroundColor": '#ff000000'
    }
    },
    "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "baseline",
    "contents": [
    {
    "type": "icon",
    "url": "https://obs.line-scdn.net/{}".format(line.getContact(myMid).pictureStatus),
    "size": "md"
    },
    {
    "type": "text",
    "text": text,
    "color": "#000000",
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "md"
    },
    {
    "type": "icon",
    "url": "https://obs.line-scdn.net/{}".format(line.getContact(myMid).pictureStatus),
    "size": "md"
    }, 
    ]
    }
    ]
    }
    }
    }
    sendTemplate(to, data)

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '├', '│', '╰']]:
            result += '\n│ ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def mentionMembers(to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    result = '╭───「 Mention 」\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 Self Bot 」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            line.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def cloneProfile(mid):
    contact = line.getContact(mid)
    profile = line.getProfile()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile(profile)
    if contact.pictureStatus:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture(pict)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    line.updateProfile(profile)
    if settings['myProfile']['pictureStatus']:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'])
        line.updateProfilePicture(pict)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == '@logoutbot':
        yepzLove(to, 'Bot will logged out')
        sys.exit('##----- PROGRAM STOPPED -----##')
    if cmd == "creator":
        yepzLove(to,"Contact Dibawah Ini \nAdalah Creator Bot")
        line.sendContact(to,"u65129423a63f75ecae3ea189f9540054")
#    if cmd == "mytoken":
    if msg.text.lower().startswith("/Token "):
      if 'MENTION' in msg.contentMetadata.keys()!= None:
          names = re.findall(r'@(\w+)', text)
          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
          mentionees = mention['MENTIONEES']
          lists = []
          for mention in mentionees:
              if mention["M"] not in lists:
                  lists.append(mention["M"])
          for ls in lists:
              contact = line.getToken(ls)
              line.sendMessage(msg.to, + contact.Token)
    if msg.text.lower().startswith("/ข้อมูล "):
      if 'MENTION' in msg.contentMetadata.keys()!= None:
          names = re.findall(r'@(\w+)', text)
          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
          mentionees = mention['MENTIONEES']
          lists = []
          for mention in mentionees:
              if mention["M"] not in lists:
                  lists.append(mention["M"])
          for ls in lists:
              dan = line.getContact(ls)
              contact = line.getContact(ls)
              sender_profile = line.getContact(ls)
              dataProfile = [
                  {
                      "type": "bubble",
                      "styles": {
                          "header": {"backgroundColor": "#FFFFFF"},
                          "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"},
                          "footer": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"}
                      },
                      "header": {
                          "type": "box",
                          "layout": "vertical",
                          "spacing": "sm",
                          "contents": [
                              {
                                  "type": "image",
                                  "url": "https://obs.line-scdn.net/{}".format(line.getContact(ls).pictureStatus),
                                  "size": "full",
                                  "aspectMode": "cover",
                                  "aspectRatio": "1:1",
                                  "gravity": "center"
                              },
                              {
                                  "type": "text",
                                  "text": "「 Token 」",
                                  "size": "lg",
                                  "weight": "bold",
                                  "align": "center",
                                  "color": "#000000"
                              },
                              {
                                  "type": "text",
                                  "text": "• Win10",
                                  "color": "#000000",
                                  'flex': 1,
                              },
                              {
                                  "type": "text",
                                  "text": "• Iospad",
                                  "color": "#000000",
                                  'flex': 1,
                              },
                              {
                                  "type": "text",
                                  "text": "• Chromeos",
                                  "color": "#000000",
                                  'flex': 1,
                              },
                              {
                                  "type": "text",
                                  "text": "• Desktopwin",
                                  "color": "#000000",
                                  'flex': 1,
                              },
                              {
                                  "type": "text",
                                  "text": "• Desktopmac",
                                  "color": "#000000",
                                  'flex': 1,
                              },
                              {
                                  "type": "text",
                                  "text": "Ex : Token win10",
                                  "color": "#000000",
                                  'flex': 1,
                              },
                              {
                                  "type": "text",
                                  "text": "Jika Sudah Ketik「 Done 」",
                                  "color": "#000000",
                                  'flex': 1,
                              }
                          ]
                      },
                      "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "spacing": "sm",
                          "contents": [
                              {
                                  "type": "box",
                                  "layout": "baseline",
                                  "contents": [
                                      {
                                          "type": "icon",
                                          "url": "https://obs.line-scdn.net/{}".format(line.getContact(ls).pictureStatus),
                                          "size": "xl"
                                      },
                                      {
                                          "type": "text",
                                          "text": "HelloWorld",
                                          "align": "center",
                                          "color": "#000000",
                                          "size": "md"
                                      },
                                      {
                                          "type": "spacer",
                                          "size": "sm",
                                      }
                                  ]
                              }
                          ]
                      }
                  }
              ]
              babi = {
                  "type": "flex",
                  "altText": "Love Yepz",
                  "contents": {
                      "type": "carousel",
                      "contents": dataProfile
                  }
              }
              sendTemplate(to, babi)
    if cmd == "self":
        sender_profile = line.getContact(sender)
        dataProfile = [
            {
                "type": "bubble",
                "styles": {
                    "header": {"backgroundColor": "#FFFFFF"},
                    "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"},
                    "footer": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"}
                },
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "1:1",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": "「 Yepz 」",
                            "size": "lg",
                            "weight": "bold",
                            "align": "center",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "• Me",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Profile",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Blocklist",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Mimic",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Myprofile",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Creator",
                            "color": "#000000",
                            'flex': 1,
                        }, 
                        {
                            "type": "text",
                            "text": "• Friendlist",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Broadcast",
                            "color": "#000000",
                            'flex': 1,
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "HelloWorld",
                                    "align": "center",
                                    "color": "#000000",
                                    "size": "md"
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm",
                                }
                            ]
                        }
                    ]
                }
            }
        ]
        babi = {
            "type": "flex",
            "altText": "Love Yepz",
            "contents": {
                "type": "carousel",
                "contents": dataProfile
            }
        }
        sendTemplate(to, babi)
    if cmd == "group":
        sender_profile = line.getContact(sender)
        dataProfile = [
            {
                "type": "bubble",
                "styles": {
                    "header": {"backgroundColor": "#FFFFFF"},
                    "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"},
                    "footer": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"}
                },
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "1:1",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": "「 Group 」",
                            "size": "lg",
                            "weight": "bold",
                            "align": "center",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "• Groupinfo",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Grouplist",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Memberlist",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Openqr",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Closeqr",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• ChangeGroupName <name>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• ChangeGroupPict",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Kickall",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Cancelall",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Tagall",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Lurk",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• kick <Mention>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Vkick <Mention>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Greet",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Open <NumberGroup>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Close <NumberGroup>",
                            "color": "#000000",
                            'flex': 1,
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "HelloWorld",
                                    "align": "center",
                                    "color": "#000000",
                                    "size": "md"
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm",
                                }
                            ]
                        }
                    ]
                }
            }
        ]
        babi = {
            "type": "flex",
            "altText": "Love Yepz",
            "contents": {
                "type": "carousel",
                "contents": dataProfile
            }
        }
        sendTemplate(to, babi)
    if cmd == "settings":
        sender_profile = line.getContact(sender)
        dataProfile = [
            {
                "type": "bubble",
                "styles": {
                    "header": {"backgroundColor": "#FFFFFF"},
                    "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"},
                    "footer": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"}
                },
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "1:1",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": "「 Settings 」",
                            "size": "lg",
                            "weight": "bold",
                            "align": "center",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "• SetKey",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• AutoAdd",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• AutoRespond",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• AutoRespondMention",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• AutoRead <On/Off>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• CheckContact <On/Off>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• CheckPost <On/Off>",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• CheckSticker <On/Off>",
                            "color": "#000000",
                            'flex': 1,
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "HelloWorld",
                                    "align": "center",
                                    "color": "#000000",
                                    "size": "md"
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm",
                                }
                            ]
                        }
                    ]
                }
            }
        ]
        babi = {
            "type": "flex",
            "altText": "Love Yepz",
            "contents": {
                "type": "carousel",
                "contents": dataProfile
            }
        }
        sendTemplate(to, babi)
        
    if cmd == "media":
        sender_profile = line.getContact(sender)
        dataProfile = [
            {
                "type": "bubble",
                "styles": {
                    "header": {"backgroundColor": "#FFFFFF"},
                    "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"},
                    "footer": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#FFFFFF"}
                },
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "1:1",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": "「 Media 」",
                            "size": "lg",
                            "weight": "bold",
                            "align": "center",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": "• Musik「Text」",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Image「Text」",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Gambar「Text」",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Playvidio「Text」",
                            "color": "#000000",
                            'flex': 1,
                        },
                        {
                            "type": "text",
                            "text": "• Listoken",
                            "color": "#000000",
                            'flex': 1,
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://obs.line-scdn.net/{}".format(line.getContact(sender).pictureStatus),
                                    "size": "xl"
                                },
                                {
                                    "type": "text",
                                    "text": "HelloWorld",
                                    "align": "center",
                                    "color": "#000000",
                                    "size": "md"
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm",
                                }
                            ]
                        }
                    ]
                }
            }
        ]
        babi = {
            "type": "flex",
            "altText": "Love Yepz",
            "contents": {
                "type": "carousel",
                "contents": dataProfile
            }
        }
        sendTemplate(to, babi)
        
    if cmd == "help":
        sender_profile = line.getContact(sender)
        dataProfile = [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(line.getContact(myMid).pictureStatus),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "center"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "image",
                                                    "url": "https://obs.line-scdn.net/{}".format(line.getContact("u65129423a63f75ecae3ea189f9540054").pictureStatus),
                                                    "aspectMode": "cover",
                                                    "size": "full",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://ti/p/~myyepz"
                                                    }
                                                }
                                            ],
                                            "cornerRadius": "100px",
                                            "width": "72px",
                                            "height": "72px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "xxl",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "🔱     SELF    🔱",
                                                            "color": "#ffffff",
                                                            "margin": "sm",
                                                            "flex": 0,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "🔱   MEDIA   🔱",
                                                            "size": "sm",
                                                            "color": "#ffffff",
                                                            "align": "end"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "🔱   GROUP   🔱",
                                                            "color": "#ffffff",
                                                            "margin": "sm",
                                                            "flex": 0,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "🔱 SETTINGS 🔱",
                                                            "size": "sm",
                                                            "color": "#ffffff",
                                                            "align": "end"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "paddingAll": "20px"
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
        babi = {
            "type": "flex",
            "altText": "Love Yepz",
            "contents": {
                "type": "carousel",
                "contents": dataProfile
            }
        }
        sendTemplate(to, babi)
        
    if cmd in ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ","ปลิว","ควย","หี","แตด","เย็ดแม่","เย็ดเข้","ค.วย","สัส","เหี้ย","ไอเหี้ย","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้เรส","ไอ้เหี้ยเรส","ไอ่เรส","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ","บอทเหี้ย","บอทควย","ควยบอท","บอทนรก","เหี้ยบอท","ควยย","ควยย"]:
#                    settings["Aip"] == True
      line.kickoutFromGroup(receiver,[sender])
      line.sendMessage(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม\n           หรือ\n ตรวจพบคำพูดหยาบคายไม่สุภาพ\nจำเป็นต้องนำออกเพื่อความปลอดภัย\nและความสงบสุขของสมาชิก (｀・ω・´)")
    if cmd == "/เตือน":
        groups = line.getGroupIdsJoined()
        for group in groups:
          gifnya = ["https://www.img.in.th/images/c1731afa90e387880d9d9754daa71978.jpg","https://www.img.in.th/images/f2a9556f728a9ce69945fdc606e44492.jpg","https://www.img.in.th/images/c1061b99b6afb412cb50cc924ae6045d.jpg","https://www.img.in.th/images/c639f8f85a13a10bf8efb97e2a0761d1.jpg","https://www.img.in.th/images/adee3112952d366c23d1ef615c6a6b61.jpg","https://www.img.in.th/images/31404944c120827925179123a7b90556.jpg","https://www.img.in.th/images/554b556492888867853cc67de99651d5.jpg","https://www.img.in.th/images/7e43ce82d8f328819cf76bc8f2627e88.jpg","https://www.img.in.th/images/0a44779345c22adcb4494e32cd00ece2.jpg","https://www.img.in.th/images/2de660a2ed3216438a836892329ea754.jpg","https://www.img.in.th/images/21b2922c33a55eca0836006b9804e6ec.jpg",]
          data = {
              "type": "template",
              "altText": "⚜️⚜️  เพจอันตรายห้ามเล่น ⚜️⚜️\n อัพเดต By.SLOT THAI ️",
              "template": {
                  "type": "image_carousel",
                  "columns": [
                      {
#                          "imageUrl": "{}".format(str(gifnya)),
                          "imageUrl": "{}".format(random.choice(gifnya)),
                          "size": "full",
                         # "imageUrl":"https://www.img.in.th/images/751a1c5fdf28c3465c6c1c19473ce49c.jpg",
                          #"size": "full",
                          "action": {
                              "type": "uri",
                              "uri":"https://www.img.in.th/images/748c8477e2a64092846697af47959274.jpg"
                           }
                      }
                  ]
              }
          }
          sendTemplate(group, data)
    if text.lower() == "Allscanwin" or text.lower() == "/อัพเดต":
        groups = line.getGroupIdsJoined()
        for group in groups:
                dataProfile = [
                    {
                        "type": "bubble",
                        "styles": {
                            "header": {"backgroundColor":"#000000"},
                            "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                            "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                        },
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xxl",
                            "contents": [
                                {
                                    "type":"image",
                                    "url":"https://data.bloggif.com/distant/user/store/2/9/a/1/b1811c978876e890d6cc2ee86d261a92.gif",
                                    "aspectMode":"cover",
                                    "margin":"xxl",
                                    "aspectRatio":"16:25",
                                    "size":"full",
                                    "action":{
                                        "type":"uri",
                                        "uri":"https://lin.ee/sVQoXGF"
                                     },
                                },
                            ]
                        },
                    },
                ]
                data = {
                    "type": "flex",
                    "altText": "⚜️⚜️ แจ้งข่าวสาร อัพเดตเพจโกง ⚜️⚜️",
                    "contents": {
                        "type": "carousel",
                        "contents": dataProfile
                    }
                }
                sendTemplate(group, data)
        
        
    if cmd == "flex":
        yepzLove(to, "Test Flex")
        
    if cmd == "gif":
        gifnya = ["https://i.ibb.co/pLyQpdr/anime-bailando-gif-7.gif","https://media.giphy.com/media/VBWnFEMtMD5Is/giphy.gif","https://media2.giphy.com/media/jUg8D7Yy0Qi4w/giphy.gif?cid=19f5b51a7c82acd6815fb74cf569fcd11ee54e9eda64cd86&rid=giphy.gif","https://media0.giphy.com/media/aRU66OhuzbD8s/giphy.gif?cid=19f5b51a37402afce56510eaaa6933d2a733168ab4b8cc0c&rid=giphy.gif","https://media0.giphy.com/media/cMxycqtqIDe12/giphy.gif?cid=19f5b51a92ef14399121f2370dc759ef21cdef7e7533e89c&rid=giphy.gif","https://media3.giphy.com/media/Bw48Wu7cgnO2Q/giphy.gif?cid=19f5b51a2e1e948efb871a4d2b899cf1cd60e91355cf0336&rid=giphy.gif","https://media0.giphy.com/media/G37ktbRBJHsB2/giphy.gif?cid=19f5b51a3390c27cd173ce1d1232e905a9a502e82d78118d&rid=giphy.gif","https://media3.giphy.com/media/y1cCpkyb1IdNu/giphy.gif?cid=19f5b51a1d3f424efdfd0bb504586d0e6e2e940113e666a0&rid=giphy.gif"]
        data = {
            "type": "template",
            "altText": "Norak Lo !",
            "template": {
                "type": "image_carousel",
                "columns": [
                    {
                        "imageUrl": "{}".format(random.choice(gifnya)),
                        "size": "full",
                        "action": {
                            "type": "uri",
                            "uri": "line://ti/p/~vipscanner_win"
                        }
                    }
                ]
            }
        }
        sendTemplate(to, data)
        
    elif cmd == '@logoutdevicee':
        line.logout()
        sys.exit('##----- CLIENT LOGOUT -----##')
    elif cmd == 'restart':
        yepzLove(to, 'Bot will restarting, please wait until the bot can operate ♪')
        settings['restartPoint'] = to
        restartProgram()
    elif cmd == 'speed':
        start = time.time()
        yepzLove(to, 'Checking speed')
        elapse = time.time() - start
        yepzLove(to, 'Speed sending message took %s seconds' % str(elapse))
    elif cmd == 'me':
        contact = line.getContact(sender)
        sendTemplate(to,{"type":"flex","altText": "꧁༺ஆืਹໂ√န༻꧂","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#FF69B4","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1636169025-yQ7bGMVA?type=profile"},"type":"text","text":"꧁༺ஆืਹໂ√န༻꧂","align":"center","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#FF69B4","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://ti/p/~vipscanner_win"},"type":"text","text":"ติดต่อเช่าบอท","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#FFD2E6"},"body":{"backgroundColor":"#ffffff"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://i.ibb.co/ZXzddDh/Pics-Art-01-07-05-35-09.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.ibb.co/GdwQtdS/Screenshot-2018-1215-233501.png"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://media.giphy.com/media/qqWB4u3mrTlrG/giphy.gif"},{"type":"separator","color":"#FF69B4"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.pinimg.com/originals/a6/94/ec/a694ec9773292abec803f07befd73e74.gif"},{"type":"separator","color":"#FF69B4"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF69B4"},{"type":"box","contents":[{"type":"separator","color":"#FF69B4"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"ข้อมูล สมาชิก","weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#413877","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF69B4"},{"color":"#FF69B4","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#422002"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})
#=======================================================================================
    elif cmd.startswith("bye "):
        if msg._from in admin:
           targets = []
           key = eval(msg.contentMetadata["MENTION"])
           key["MENTIONEES"][0]["M"]
           for x in key["MENTIONEES"]:
               targets.append(x["M"])
           for target in targets:
               if not target in admin:
                   try:
                       line.kickoutFromGroup(msg.to,[target])
                   except:
                       line.sendMessage(msg.to,"Error")
    elif cmd.startswith("แปลไทย "):
        sep = text.split(" ")
        isi = text.replace(sep[0] + " ","")
        translator = Translator()
        hasil = translator.translate(isi, dest='th')
        A = hasil.text
#        line.sendMessage(msg.to, A)
        yepzLove(to, "แปลว่า\n""➡️"+A+"⬅️\n\n    ขับเคลื่อนบอทโดย\n    ꧁༺ஆืਹໂ√န༻꧂")
    elif cmd in ["ไปๆ"]:
      if msg._from in admin:
        line.leaveGroup(msg.to)
    elif msg.text in ["เชิญ"]:
        if msg._from in admin:
            settings["winvite"] = True
            line.sendMessage(msg.to,"ส่งคอนแทคเพื่อเชิญได้เลยคับ")
        else:
            line.sendMessage(msg.to,"คุณไม่มีอำนาจสั่ง")
#-------------------------------------------------------------------------------
#    elif text.lower() == 'ล้างเชิญ':
 #       if msg._from in admin:
  #          group =  line.getGroup(msg.to)
   #         gMembMids = [contact.mid for contact in group.invitee]
    #        for i in gMembMids:
     #            line.cancelGroupInvitaion(msg.to,[i])
      #      else:
       #          line.sendMessage(msg.to, "*เรียบร้อย*")
#=======================================================================================
    elif cmd in ["admin","Admin","แอดมิน","แอด"]:
        line.sendMessage(msg.to,"╠♥ ✿✿✿ รายชื่อ ADMIN ✿✿✿ ♥══✪")
        line.sendContact(to, "u666c073dfb3ee3f8989e86909f92f515")
        line.sendContact(to, "u93d0b6fe5509e5724933ec82caa3f9d0")
#                    maxgie.sendContact(to, "ud9dce4f96fca36bdede21e0098720713")
        line.sendContact(to, "u5d5e07404cdf4df1c8e46cca32f954e5")
        line.sendContact(to, "u43f809951f219e710e0d19a508283d09")
        line.sendContact(to, "u6531c77c3f93662d15ad99978661e8ef")
        line.sendContact(to, "ufcfd4178ed1d4b8a2307edbbae5e07a9")
        line.sendContact(to, "u7a85e1fbda85a57b62957b2fb158b571")
        line.sendContact(to, "ue2dafef8df79815e31a7334e7198eeba")
        line.sendContact(to, "u4e337bb95540bf236e19c032a15708a4")
        line.sendMessage(msg.to,"╠♥ควบคุมระบบบอทโดย ꧁༺ஆืਹໂ√န༻꧂ ♥✪")
        line.sendContact(to, "u24d5f93f9113c991342c079005467e2f")
#    elif cmd == 'me':
 #          msg.contentType = 13
  #         msg.contentMetadata = {'mid': msg._from}
   #        line.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': msg._from}, contentType=13)
    #       path = line.getContact(msg.contentMetadata["mid"]).picturePath
    elif cmd == "changevp":
	    settings["changevp"] = True
	    client.sendReplyMessage(msg_id, to, "Kirim video nya")
    elif cmd == 'runtime':
        runtime = time.time() - programStart
        yepzLove(to, 'Bot already running on ' + format_timespan(runtime))
    elif cmd == 'author':
        yepzLove(to, 'Author is linepy')
    elif cmd == 'about':
        res = '╭───「 About 」'
        res += '\n├ Type : Self Bot'
        res += '\n├ Version : 3.0.8'
        res += '\n├ Library : linepy'
        res += '\n├ Special Thanks To'
        res += '\n├ Team Hello World'
        res += '\n╰──────────'
        line.sendReplyMessage(msg_id, to, res)
    elif cmd == 'status':
        res = '╭───「 Status 」'
        res += '\n├ Auto Add : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Auto Join : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Auto Respond : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Auto Respond Mention : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Auto Read : ' + bool_dict[settings['autoRead']][1]
        res += '\n├ Setting Key : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Mimic : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ Greetings Join : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Leave : ' + bool_dict[settings['greet']['leave']['status']][1]
        res += '\n├ Check Contact : ' + bool_dict[settings['checkContact']][1]
        res += '\n├ Check Post : ' + bool_dict[settings['checkPost']][1]
        res += '\n├ Check Sticker : ' + bool_dict[settings['checkSticker']][1]
        res += '\n╰───「 Self Bot 」'
        line.sendReplyMessage(msg_id, to, parsingRes(res))
    elif cmd == 'abort':
        aborted = False
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            yepzLove(to, 'Change group picture aborted')
            aborted = True
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            yepzLove(to, 'Change picture profile aborted')
            aborted = True
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            yepzLove(to, 'Change cover profile aborted')
            aborted = True
        if not aborted:
            yepzLove(to, 'Failed abort, nothing to abort')
    elif cmd.startswith('error'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Error 」'
        res += '\n├ Usage : '
        res += '\n│ • {key}Error'
        res += '\n│ • {key}Error Logs'
        res += '\n│ • {key}Error Reset'
        res += '\n│ • {key}Error Detail <errid>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'error':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'logs':
            try:
                filee = open('errorLog.txt', 'r')
            except FileNotFoundError:
                return yepzLove(to, 'Failed display error logs, error logs file not found')
            errors = [err.strip() for err in filee.readlines()]
            filee.close()
            if not errors: return yepzLove(to, 'Failed display error logs, empty error logs')
            res = '╭───「 Error Logs 」'
            res += '\n├ List :'
            parsed_len = len(errors)//200+1
            no = 0
            for point in range(parsed_len):
                for error in errors[point*200:(point+1)*200]:
                    if not error: continue
                    no += 1
                    res += '\n│ %i. %s' % (no, error)
                    if error == errors[-1]:
                        res += '\n╰───「 Self Bot 」'
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendReplyMessage(msg_id, to, res)
                res = ''
        elif cond[0].lower() == 'reset':
            filee = open('errorLog.txt', 'w')
            filee.write('')
            filee.close()
            shutil.rmtree('tmp/errors/', ignore_errors=True)
            os.system('mkdir tmp/errors')
            yepzLove(to, 'Success reset error logs')
        elif cond[0].lower() == 'detail':
            if len(cond) < 2:
                return yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            errid = cond[1]
            if os.path.exists('tmp/errors/%s.txt' % errid):
                with open('tmp/errors/%s.txt' % errid, 'r') as f:
                    yepzLove(to, f.read())
            else:
                return yepzLove(to, 'Failed display details error, errorid not valid')
        else:
            yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif txt.startswith('setkey'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Setting Key 」'
        res += '\n├ Status : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Key : ' + settings['setKey']['key'].title()
        res += '\n├ Usage : '
        res += '\n│ • Setkey'
        res += '\n│ • Setkey <on/off>'
        res += '\n│ • Setkey <key>'
        res += '\n╰───「 Self Bot 」'
        if txt == 'setkey':
            line.sendReplyMessage(msg_id, to, parsingRes(res))
        elif texttl == 'on':
            if settings['setKey']['status']:
                yepzLove(to, 'Failed activate setkey, setkey already active')
            else:
                settings['setKey']['status'] = True
                yepzLove(to, 'Success activated setkey')
        elif texttl == 'off':
            if not settings['setKey']['status']:
                yepzLove(to, 'Failed deactivate setkey, setkey already deactive')
            else:
                settings['setKey']['status'] = False
                yepzLove(to, 'Success deactivated setkey')
        else:
            settings['setKey']['key'] = texttl
            yepzLove(to, 'Success change set key to (%s)' % textt)
    elif cmd.startswith("musik "):
        query = msg.text.replace("musik","")
        search = query.replace(" ","+")
        result = requests.get("https://api.zicor.ooo/joox.php?song={}".format(str(search)))
        data = result.text
        data = json.loads(data)
        ret_ = "-•••>> Play Music <<•••-"
        ret_ += "\n- Judul : {}".format(data["title"])
        ret_ += "\n- Artis : {}".format(data["singer"])
        ret_ += "\n- Lirik :\n{}".format(data["lyric"])
        line.sendImageWithURL(to, data["image"])
        line.sendReplyMessage(msg_id, to, ret_)
        line.sendAudioWithURL(to, data["url"])
    elif cmd.startswith("image "):
           sep = msg.text.split(" ")
           textnya = msg.text.replace(sep[0] + " ","")
           path = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
           line.sendImageWithURL(msg.to,path)
    elif cmd.startswith("playvidio "):
   #   if msg._from in admin:
        try:
            sep = msg.text.split(" ")
            textToSearch = msg.text.replace(sep[0] + " ","")
            query = urllib.parse.quote(textToSearch)
            search_url="https://www.youtube.com/results?search_query="
            mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
            sb_url = search_url + query
            sb_get = requests.get(sb_url, headers = mozhdr)
            soupeddata = BeautifulSoup(sb_get.content, "html.parser")
            yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
            x = (yt_links[1])
            yt_href =  x.get("href")
            yt_href = yt_href.replace("watch?v=", "")
            qx = "https://youtu.be" + str(yt_href)
            vid = pafy.new(qx)
            stream = vid.streams
            best = vid.getbest()
            best.resolution, best.extension
            for s in stream:
                me = best.url
                hasil = ""
                title = "Judul [ " + vid.title + " ]"
                author = '\n\nâ Author : ' + str(vid.author)
                durasi = '\nâ Duration : ' + str(vid.duration)
                suka = '\nâ Likes : ' + str(vid.likes)
                rating = '\nâ Rating : ' + str(vid.rating)
                deskripsi = '\nâ Deskripsi : ' + str(vid.description)
                line.sendVideoWithURL(msg.to, me)
                line.sendReplyMessage(msg_id, to,title+ author+ durasi+ suka+ rating+ deskripsi)
        except Exception as e:
                line.sendReplyMessage(msg_id, to,str(e))
    elif cmd.startswith("open "):
 #     if msg._from in Owner:
        separate = text.split(" ")
        number = text.replace(separate[0] + " ","")
        groups = line.getGroupIdsJoined()
        ret_ = ""
        try:
            group = groups[int(number)-1]
            G = line.getGroup(group)
            G.preventedJoinByTicket = False
            line.updateGroup(G)
            try:
                gCreator = G.creator.mid
                dia = line.getContact(gCreator)
                zx = ""
                zxc = ""
                zx2 = []
                xpesan = '< Sukses Open Qr >\n• Creator :  '
                diaa = str(dia.displayName)
                pesan = ''
                pesan2 = pesan+"@a\n"
                xlen = str(len(zxc)+len(xpesan))
                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                zx2.append(zx)
                zxc += pesan2
            except:
                gCreator = "Tidak ditemukan"
            if G.invitee is None:
                gPending = "0"
            else:
                gPending = str(len(G.invitee))
            if G.preventedJoinByTicket == True:
                gQr = "Tertutup"
                gTicket = "Tidak ada"
            else:
                gQr = "Terbuka"
                gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(G.id)))
            timeCreated = []
            timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
            ret_ += xpesan+zxc
            ret_ += "â¢ Nama : {}".format(G.name)
            ret_ += "\nâ¢ Group Qr : {}".format(gQr)
            ret_ += "\nâ¢ Pendingan : {}".format(gPending)
            ret_ += "\nâ¢ Group Ticket : {}".format(gTicket)
            ret_ += ""
            line.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
        except:
            pass
    elif cmd.startswith("gambar "):
            query = msg.text.replace("gambar ","")
            r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
            data=r.text
            data=json.loads(r.text)
            if data != []:
                for food in data:
                    line.sendImageWithURL(msg.to, str(food["url"]))
    elif cmd.startswith('autoadd'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Add 」'
        res += '\n├ Status : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoAdd']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoAdd']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoAdd'
        res += '\n│ • {key}AutoAdd <on/off>'
        res += '\n│ • {key}AutoAdd Reply <on/off>'
        res += '\n│ • {key}AutoAdd <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'autoadd':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoAdd']['status']:
                yepzLove(to, 'Autoadd already active')
            else:
                settings['autoAdd']['status'] = True
                yepzLove(to, 'Success activated autoadd')
        elif texttl == 'off':
            if not settings['autoAdd']['status']:
                yepzLove(to, 'Autoadd already deactive')
            else:
                settings['autoAdd']['status'] = False
                yepzLove(to, 'Success deactivated autoadd')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoAdd']['reply']:
                    yepzLove(to, 'Reply message autoadd already active')
                else:
                    settings['autoAdd']['reply'] = True
                    yepzLove(to, 'Success activate reply message autoadd')
            elif cond[1].lower() == 'off':
                if not settings['autoAdd']['reply']:
                    yepzLove(to, 'Reply message autoadd already deactive')
                else:
                    settings['autoAdd']['reply'] = False
                    yepzLove(to, 'Success deactivate reply message autoadd')
            else:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoAdd']['message'] = textt
            yepzLove(to, 'Success change autoadd message to `%s`' % textt)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Join 」'
        res += '\n├ Status : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoJoin']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoJoin'
        res += '\n│ • {key}AutoJoin <on/off>'
        res += '\n│ • {key}AutoJoin Ticket <on/off>'
        res += '\n│ • {key}AutoJoin Reply <on/off>'
        res += '\n│ • {key}AutoJoin <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'autojoin':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                yepzLove(to, 'Autojoin already active')
            else:
                settings['autoJoin']['status'] = True
                yepzLove(to, 'Success activated autojoin')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                yepzLove(to, 'Autojoin already deactive')
            else:
                settings['autoJoin']['status'] = False
                yepzLove(to, 'Success deactivated autojoin')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    yepzLove(to, 'Reply message autojoin already active')
                else:
                    settings['autoJoin']['reply'] = True
                    yepzLove(to, 'Success activate reply message autojoin')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    yepzLove(to, 'Reply message autojoin already deactive')
                else:
                    settings['autoJoin']['reply'] = False
                    yepzLove(to, 'Success deactivate reply message autojoin')
            else:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'ticket':
            if len(cond) < 2:
                return yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['ticket']:
                    yepzLove(to, 'Autojoin ticket already active')
                else:
                    settings['autoJoin']['ticket'] = True
                    yepzLove(to, 'Success activate autojoin ticket')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['ticket']:
                    yepzLove(to, 'Autojoin ticket already deactive')
                else:
                    settings['autoJoin']['ticket'] = False
                    yepzLove(to, 'Success deactivate autojoin ticket')
            else:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoJoin']['message'] = textt
            yepzLove(to, 'Success change autojoin message to `%s`' % textt)
    elif cmd.startswith('autorespondmention'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespondMention']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespondMention'
        res += '\n│ • {key}AutoRespondMention <on/off>'
        res += '\n│ • {key}AutoRespondMention <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'autorespondmention':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespondMention']['status']:
                yepzLove(to, 'Autorespondmention already active')
            else:
                settings['autoRespondMention']['status'] = True
                yepzLove(to, 'Success activated autorespondmention')
        elif texttl == 'off':
            if not settings['autoRespondMention']['status']:
                yepzLove(to, 'Autorespondmention already deactive')
            else:
                settings['autoRespondMention']['status'] = False
                yepzLove(to, 'Success deactivated autorespondmention')
        else:
            settings['autoRespondMention']['message'] = textt
            yepzLove(to, 'Success change autorespondmention message to `%s`' % textt)
    elif cmd.startswith('autorespond'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespond']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespond'
        res += '\n│ • {key}AutoRespond <on/off>'
        res += '\n│ • {key}AutoRespond <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'autorespond':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespond']['status']:
                yepzLove(to, 'Autorespond already active')
            else:
                settings['autoRespond']['status'] = True
                yepzLove(to, 'Success activated autorespond')
        elif texttl == 'off':
            if not settings['autoRespond']['status']:
                yepzLove(to, 'Autorespond already deactive')
            else:
                settings['autoRespond']['status'] = False
                yepzLove(to, 'Success deactivated autorespond')
        else:
            settings['autoRespond']['message'] = textt
            yepzLove(to, 'Success change autorespond message to `%s`' % textt)
    elif cmd.startswith('autoread '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['autoRead']:
                yepzLove(to, 'Autoread already active')
            else:
                settings['autoRead'] = True
                yepzLove(to, 'Success activated autoread')
        elif texttl == 'off':
            if not settings['autoRead']:
                yepzLove(to, 'Autoread already deactive')
            else:
                settings['autoRead'] = False
                yepzLove(to, 'Success deactivated autoread')
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                yepzLove(to, 'Checkcontact already active')
            else:
                settings['checkContact'] = True
                yepzLove(to, 'Success activated checkcontact')
        elif texttl == 'off':
            if not settings['checkContact']:
                yepzLove(to, 'Checkcontact already deactive')
            else:
                settings['checkContact'] = False
                yepzLove(to, 'Success deactivated checkcontact')
    elif cmd.startswith('checkpost '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkPost']:
                yepzLove(to, 'Checkpost already active')
            else:
                settings['checkPost'] = True
                yepzLove(to, 'Success activated checkpost')
        elif texttl == 'off':
            if not settings['checkPost']:
                yepzLove(to, 'Checkpost already deactive')
            else:
                settings['checkPost'] = False
                yepzLove(to, 'Success deactivated checkpost')
    elif cmd.startswith('checksticker '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkSticker']:
                yepzLove(to, 'Checksticker already active')
            else:
                settings['checkSticker'] = True
                yepzLove(to, 'Success activated checksticker')
        elif texttl == 'off':
            if not settings['checkSticker']:
                yepzLove(to, 'Checksticker already deactive')
            else:
                settings['checkSticker'] = False
                yepzLove(to, 'Success deactivated checksticker')
    elif cmd.startswith('myprofile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getProfile()
        res = '╭───「 My Profile 」'
        res += '\n├ MID : ' + profile.mid
        res += '\n├ Display Name : ' + str(profile.displayName)
        res += '\n├ Status Message : ' + str(profile.statusMessage)
        res += '\n├ Usage : '
        res += '\n│ • {key}MyProfile'
        res += '\n│ • {key}MyProfile MID'
        res += '\n│ • {key}MyProfile Name'
        res += '\n│ • {key}MyProfile Bio'
        res += '\n│ • {key}MyProfile Pict'
        res += '\n│ • {key}MyProfile Cover'
        res += '\n│ • {key}MyProfile Change Name <name>'
        res += '\n│ • {key}MyProfile Change Bio <bio>'
        res += '\n│ • {key}MyProfile Change Pict'
        res += '\n│ • {key}MyProfile Change Cover'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'myprofile':
            if profile.pictureStatus:
                line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            yepzLove(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            yepzLove(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            yepzLove(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                yepzLove(to, '「 Picture Status 」\n' + path)
            else:
                yepzLove(to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            yepzLove(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('change '):
            texts = textt[7:]
            textsl = texts.lower()
            if textsl.startswith('name '):
                name = texts[5:]
                if len(name) <= 20:
                    profile.displayName = name
                    line.updateProfile(profile)
                    yepzLove(to, 'Success change display name, changed to `%s`' % name)
                else:
                    yepzLove(to, 'Failed change display name, the length of the name cannot be more than 20')
            elif textsl.startswith('bio '):
                bio = texts[4:]
                if len(bio) <= 500:
                    profile.statusMessage = bio
                    line.updateProfile(profile)
                    yepzLove(to, 'Success change status message, changed to `%s`' % bio)
                else:
                    yepzLove(to, 'Failed change status message, the length of the bio cannot be more than 500')
            elif textsl == 'pict':
                settings['changePictureProfile'] = True
                yepzLove(to, 'Please send the image to set in picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            elif textsl == 'cover':
                settings['changeCoverProfile'] = True
                yepzLove(to, 'Please send the image to set in cover profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            else:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('profile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getContact(to) if msg.toType == 0 else None
        res = '╭───「 My Profile 」'
        if profile:
            res += '\n├ MID : ' + profile.mid
            res += '\n├ Display Name : ' + str(profile.displayName)
            if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
            res += '\n├ Status Message : ' + str(profile.statusMessage)
        res += '\n├ Usage : '
        res += '\n│ • {key}Profile'
        res += '\n│ • {key}Profile Mid'
        res += '\n│ • {key}Profile Name'
        res += '\n│ • {key}Profile Bio'
        res += '\n│ • {key}Profile Pict'
        res += '\n│ • {key}Profile Cover'
        res += '\n│ • {key}Profile Steal Profile <mention>'
        res += '\n│ • {key}Profile Steal Mid <mention>'
        res += '\n│ • {key}Profile Steal Name <mention>'
        res += '\n│ • {key}Profile Steal Bio <mention>'
        res += '\n│ • {key}Profile Steal Pict <mention>'
        res += '\n│ • {key}Profile Steal Cover <mention>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'profile':
            if profile:
                if profile.pictureStatus:
                    line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL(profile.mid)
                line.sendImageWithURL(to, str(cover))
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            if msg.toType != 0: return yepzLove(to, 'Failed display mid user, use this command only in personal chat')
            yepzLove(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            if msg.toType != 0: return yepzLove(to, 'Failed display mid user, use this command only in personal chat')
            yepzLove(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            if msg.toType != 0: return yepzLove(to, 'Failed display mid user, use this command only in personal chat')
            yepzLove(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if msg.toType != 0: return yepzLove(to, 'Failed display mid user, use this command only in personal chat')
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                yepzLove(to, '「 Picture Status 」\n' + path)
            else:
                yepzLove(to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            if msg.toType != 0: return yepzLove(to, 'Failed display mid user, use this command only in personal chat')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            yepzLove(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('steal '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl.startswith('profile '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        if profile.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL(profile.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Profile 」'
                        res += '\n├ MID : ' + profile.mid
                        res += '\n├ Display Name : ' + str(profile.displayName)
                        if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(profile.statusMessage)
                        res += '\n╰───「 Self Bot 」'
                        line.sendReplyMessage(msg_id, to, parsingRes(res))
                else:
                    yepzLove(to, 'Failed steal profile, no one user mentioned')
            elif textsl.startswith('mid '):
                res = '╭───「 MID 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        return yepzLove(to, '「 MID 」\n' + mid)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        res += '\n│ %i. %s' % (no, mid)
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                else:
                    yepzLove(to, 'Failed steal mid, no one user mentioned')
            elif textsl.startswith('name '):
                res = '╭───「 Display Name 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return yepzLove(to, '「 Display Name 」\n' + str(profile.displayName))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.displayName)
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                else:
                    yepzLove(to, 'Failed steal display name, no one user mentioned')
            elif textsl.startswith('bio '):
                res = '╭───「 Status Message 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendReplyMessage(msg_id, to, '「 Status Message 」\n' + str(profile.statusMessage))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.statusMessage)
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                else:
                    yepzLove(to, 'Failed steal status message, no one user mentioned')
            elif textsl.startswith('pict '):
                res = '╭───「 Picture Status 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            return line.sendReplyMessage(msg_id, to, '「 Picture Status 」\n' + path)
                        else:
                            return yepzLove(to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            res += '\n│ %i. %s' % (no, path)
                        else:
                            res += '\n│ %i. Not Found' % no
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                else:
                    yepzLove(to, 'Failed steal picture status, no one user mentioned')
            elif textsl.startswith('cover '):
                res = '╭───「 Cover Picture 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        line.sendReplyMessage(msg_id, to, '「 Cover Picture 」\n' + str(cover))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        res += '\n│ %i. %s' % (no, cover)
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                else:
                    yepzLove(to, 'Failed steal cover picture, no one user mentioned')
            else:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('mimic'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        targets = ''
        if settings['mimic']['target']:
            no = 0
            for target, status in settings['mimic']['target'].items():
                no += 1
                try:
                    name = line.getContact(target).displayName
                except TalkException:
                    name = 'Unknown'
                targets += '\n│ %i. %s//%s' % (no, name, bool_dict[status][1])
        else:
            targets += '\n│ Nothing'
        res = '╭───「 Mimic 」'
        res += '\n├ Status : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ List :'
        res += targets
        res += '\n├ Usage : '
        res += '\n│ • {key}Mimic'
        res += '\n│ • {key}Mimic <on/off>'
        res += '\n│ • {key}Mimic Reset'
        res += '\n│ • {key}Mimic Add <mention>'
        res += '\n│ • {key}Mimic Del <mention>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'mimic':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['mimic']['status']:
                yepzLove(to, 'Mimic already active')
            else:
                settings['mimic']['status'] = True
                yepzLove(to, 'Success activated mimic')
        elif texttl == 'off':
            if not settings['mimic']['status']:
                yepzLove(to, 'Mimic already deactive')
            else:
                settings['mimic']['status'] = False
                yepzLove(to, 'Success deactivated mimic')
        elif texttl == 'reset':
            settings['mimic']['target'] = {}
            yepzLove(to, 'Success reset mimic list')
        elif texttl.startswith('add '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Add Target'
            res += '\n├ Added :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    settings['mimic']['target'][mid] = True
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Self Bot 」'
                line.sendReplyMessage(msg_id, to, res)
            else:
                yepzLove(to, 'Failed add mimic target, no one user mentioned')
        elif texttl.startswith('del '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Del Target'
            res += '\n├ Deleted :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in settings['mimic']['target']:
                        settings['mimic']['target'][mid] = False
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Self Bot 」'
                line.sendReplyMessage(msg_id, to, res)
            else:
                yepzLove(to, 'Failed del mimic target, no one user mentioned')
        else:
            yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('broadcast'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Broadcast 」'
        res += '\n├ Broadcast Type : '
        res += '\n│ 1 : Friends'
        res += '\n│ 2 : Groups'
        res += '\n│ 0 : All'
        res += '\n├ Usage : '
        res += '\n│ • {key}Broadcast'
        res += '\n│ • {key}Broadcast <type> <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'broadcast':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format(key=setKey.title()))
        elif cond[0] == '1':
            if len(cond) < 2:
                return yepzLove(to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 Self Bot 」'
            targets = line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            yepzLove(to, 'Success broadcast to all friends, sent to %i friends' % len(targets))
        elif cond[0] == '2':
            if len(cond) < 2:
                return yepzLove(to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 Self Bot 」'
            targets = line.getGroupIdsJoined()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            yepzLove(to, 'Success broadcast to all groups, sent to %i groups' % len(targets))
        elif cond[0] == '0':
            if len(cond) < 2:
                return yepzLove(to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 Self Bot 」'
            targets = line.getGroupIdsJoined() + line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            yepzLove(to, 'Success broadcast to all groups and friends, sent to %i groups and friends' % len(targets))
        else:
            yepzLove(to, parsingRes(res).format(key=setKey.title()))
    elif cmd.startswith('/เพื่อน'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getAllContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Friend List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}FriendList'
        res += '\n│ • {key}FriendList Info <num/name>'
        res += '\n│ • {key}FriendList Add <mention>'
        res += '\n│ • {key}FriendList Del <mention/num/name/all>'
        res += '\n╰───「 Self Bot 」'
        ress.append(res)
        if cmd == 'friendlist':
            for res in ress:
                line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return yepzLove(to, 'Failed display info friend, nothing friend in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「 Self Bot 」'
                        line.sendReplyMessage(msg_id, to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Add Friend'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.findAndAddContactsByMid(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Self Bot 」'
                line.sendReplyMessage(msg_id, to, res)
            else:
                yepzLove(to, 'Failed add contact to friend list, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return yepzLove(to, 'Failed del contact from friend list, nothing friend in list')
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Del Friend'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.deleteContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        yepzLove(to, 'Failed del friend with name `%s`, name not in list ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「 Self Bot 」'
            line.sendReplyMessage(msg_id, to, res)
        else:
            for res in ress:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('blocklist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getBlockedContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Block List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}BlockList'
        res += '\n│ • {key}BlockList Info <num/name>'
        res += '\n│ • {key}BlockList Add <mention>'
        res += '\n│ • {key}BlockList Del <mention/num/name/all>'
        res += '\n╰───「 Self Bot 」'
        ress.append(res)
        if cmd == 'blocklist':
            for res in ress:
                line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return yepzLove(to, 'Failed display info blocked user, nothing user in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「 Self Bot 」'
                        line.sendReplyMessage(msg_id, to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Block List 」'
            res += '\n├ Status : Add Block'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.blockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 Self Bot 」'
                line.sendReplyMessage(msg_id, to, res)
            else:
                yepzLove(to, 'Failed block contact, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return yepzLove(to, 'Failed unblock contact, nothing user in list')
            res = '╭───「 Block List 」'
            res += '\n├ Status : Del Block'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.unblockContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        yepzLove(to, 'Failed unblock user with name `%s`, name not in list ♪' % name)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「 Self Bot 」'
            line.sendReplyMessage(msg_id, to, res)
        else:
            for res in ress:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'แทค':
        members = []
        if msg.toType == 1:
            room = line.getCompactRoom(to)
            members = [mem.mid for mem in room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup(to)
            members = [mem.mid for mem in group.members]
        else:
            return yepzLove(to, 'Failed mentionall members, use this command only on room or group chat')
        if members:
            mentionMembers(to, members)
    elif cmd == 'ข้อมูลกลุ่ม':
        if msg.toType != 2: return yepzLove(to, 'Failed display group info, use this command only on group chat')
        group = line.getCompactGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「 Group Info 」'
        res += '\n├ ID : ' + group.id
        res += '\n├ Name : ' + group.name
        res += '\n├ Creator : ' + gcreator
        res += '\n├ Created Time : ' + created
        res += '\n├ Member Count : ' + str(len(group.members))
        res += '\n├ Pending Count : ' + str(pendings)
        res += '\n├ QR Status : ' + qr
        res += '\n├ Ticket : ' + ticket
        res += '\n╰───「 Self Bot 」'
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        line.sendReplyMessage(msg_id, to, res)
    elif cmd.startswith('/กลุ่ม'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = '╭───「 Group List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}GroupList'
        res += '\n│ • {key}GroupList Leave <num/name/all>'
        res += '\n╰───「 Self Bot 」'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return yepzLove(to, 'Failed leave group, nothing group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            yepzLove(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            yepzLove(to, 'Success leave group %s' % group.name)
                    else:
                        yepzLove(to, 'Failed leave group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            yepzLove(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            yepzLove(to, 'Success leave group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in leaved:
                                continue
                            line.leaveGroup(gid)
                            leaved.append(gid)
                            time.sleep(0.8)
                        if to not in leaved:
                            yepzLove(to, 'Success leave all group ♪')
                    else:
                        yepzLove(to, 'Failed leave group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitlist'):
        textt = removeCmd(text,setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = '╭───「 Invitation List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}InvitationList'
        res += '\n│ • {key}InvitationList Accept <num/name/all>'
        res += '\n│ • {key}InvitationList Reject <num/name/all>'
        res += '\n╰───「 Self Bot 」'
        ress.append(res)
        if cmd == 'invitlist':
            for res in ress:
                line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return yepzLove(to, 'Failed accept group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in accepted:
                            yepzLove(to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        yepzLove(to, 'Success accept group %s' % group.name)
                    else:
                        yepzLove(to, 'Failed accept group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in accepted:
                            yepzLove(to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        yepzLove(to, 'Success accept group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in accepted:
                                continue
                            line.acceptGroupInvitation(gid)
                            accepted.append(gid)
                            time.sleep(0.8)
                        yepzLove(to, 'Success accept all invitation group ♪')
                    else:
                        yepzLove(to, 'Failed accept group with name `%s`, name not in list ♪' % name)
        elif texttl.startswith('reject '):
            texts = textt[7:].split(', ')
            rejected = []
            if not gids:
                return yepzLove(to, 'Failed reject group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in rejected:
                            yepzLove(to, 'Already reject group %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        yepzLove(to, 'Success reject group %s' % group.name)
                    else:
                        yepzLove(to, 'Failed reject group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in rejected:
                            yepzLove(to, 'Already reject group %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        yepzLove(to, 'Success reject group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in rejected:
                                continue
                            line.rejectGroupInvitation(gid)
                            rejected.append(gid)
                            time.sleep(0.8)
                        yepzLove(to, 'Success reject all invitation group ♪')
                    else:
                        yepzLove(to, 'Failed reject group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'memberlist':
        if msg.toType == 1:
            room = line.getRoom(to)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup(to)
            members = group.members
        else:
            return yepzLove(to, 'Failed display member list, use this command only on room or group chat')
        if not members:
            return yepzLove(to, 'Failed display member list, no one contact')
        res = '╭───「 Member List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「 Self Bot 」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendReplyMessage(msg_id, to, res)
            res = ''
    elif cmd == 'pendinglist':
        if msg.toType != 2: return yepzLove(to, 'Failed display pending list, use this command only on group chat')
        group = line.getGroup(to)
        members = group.invitee
        if not members:
            return yepzLove(to, 'Failed display pending list, no one contact')
        res = '╭───「 Pending List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「 Self Bot 」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendReplyMessage(msg_id, to, res)
            res = ''
    elif cmd == 'เปิดลิ้ง':
        if msg.toType != 2: return yepzLove(to, 'เปิดอยู่แล้ว')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = False
        line.updateGroup(group)
        yepzLove(to, 'เปิดลิ้งเรียบร้อย')
    elif cmd == 'ปิดลิ้ง':
        if msg.toType != 2: return yepzLove(to, 'ปิดอยู่แล้ว')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = True
        line.updateGroup(group)
        yepzLove(to, 'ปิดเรียบร้อย')
    elif cmd.startswith('เปลี่ยนชื่อกลุ่ม '):
        if msg.toType != 2: return yepzLove(to, 'ล้มเหลว')
        group = line.getCompactGroup(to)
        gname = removeCmd(text, setKey)
        if len(gname) > 50:
            return yepzLove(to, 'เปลี่ยนเรียบร้อย')
        group.name = gname
        line.updateGroup(group)
        yepzLove(to, 'เปลี่ยนเรียบร้อย `%s`' % gname)
    elif cmd == 'เปลี่ยนรูปกลุ่ม':
        if msg.toType != 2: return yepzLove(to, 'Failed change group picture, use this command only on group chat')
        if to not in settings['changeGroupPicture']:
            settings['changeGroupPicture'].append(to)
            yepzLove(to, 'ส่งรูปมา'.format(key=setKey.title()))
        else:
            yepzLove(to, 'Command already active, please send the image or type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
    elif cmd == '/ปวดตับ':
        if msg.toType != 2: return yepzLove(to, 'Failed kick all members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.members:
            return yepzLove(to, 'Failed kick all members, no member in list')
        for member in group.members:
            if member.mid == myMid:
                continue
            try:
                line.kickoutFromGroup(to, [member.mid])
            except TalkException as talk_error:
                return yepzLove(to, 'Failed kick all members, the reason is `%s`' % talk_error.reason)
            time.sleep(0.8)
        yepzLove(to, 'Success kick all members, totals %i members' % len(group.members))
    elif cmd == 'ล้างเชิญ':
        if msg.toType != 2: return yepzLove(to, 'Failed cancel all pending members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.invitee:
            return yepzLove(to, 'Failed cancel all pending members, no pending member in list')
        for member in group.invitee:
            if member.mid == myMid:
                continue
            try:
                line.cancelGroupInvitation(to, [member.mid])
            except TalkException as talk_error:
                return yepzLove(to, 'Failed cancel all pending members, the reason is `%s`' % talk_error.reason)
            time.sleep(0.8)
        yepzLove(to, 'Success cancel all pending members, totals %i pending members' % len(pendings))
    elif cmd.startswith('lurk'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if msg.toType in [1, 2] and to not in lurking:
            lurking[to] = {
                'status': False,
                'time': None,
                'members': [],
                'reply': {
                    'status': False,
                    'message': settings['defaultReplyReader']
                }
            }
        res = '╭───「 Lurking 」'
        if msg.toType in [1, 2]: res += '\n├ Status : ' + bool_dict[lurking[to]['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader : ' + bool_dict[lurking[to]['reply']['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader Message : ' + lurking[to]['reply']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Lurk'
        res += '\n│ • {key}Lurk <on/off>'
        res += '\n│ • {key}Lurk Result'
        res += '\n│ • {key}Lurk Reset'
        res += '\n│ • {key}Lurk ReplyReader <on/off>'
        res += '\n│ • {key}Lurk ReplyReader <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'lurk':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif msg.toType not in [1, 2]:
            return yepzLove(to, 'Failed execute command lurking, use this command only on room or group chat')
        elif texttl == 'on':
            if lurking[to]['status']:
                yepzLove(to, 'Lurking already active')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                yepzLove(to, 'Success activated lurking')
        elif texttl == 'off':
            if not lurking[to]['status']:
                yepzLove(to, 'Lurking already deactive')
            else:
                lurking[to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
                yepzLove(to, 'Success deactivated lurking')
        elif texttl == 'result':
            if not lurking[to]['status']:
                yepzLove(to, 'Failed display lurking result, lurking has not been activated')
            else:
                if not lurking[to]['members']:
                    yepzLove(to, 'Failed display lurking result, no one members reading')
                else:
                    members = lurking[to]['members']
                    res = '╭───「 Lurking 」'
                    if msg.toType == 2: res += '\n├ Group Name : ' + line.getGroup(to).name
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            if member == members[-1]:
                                res += '\n│'
                                res += '\n├ Time Set : ' + lurking[to]['time']
                                res += '\n╰───「 Self Bot 」'
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendReplyMessage(msg_id, to, res)
                        res = ''
        elif texttl == 'reset':
            if not lurking[to]['status']:
                yepzLove(to, 'Failed reset lurking, lurking has not been activated')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                yepzLove(to, 'Success resetted lurking')
        elif texttl.startswith('replyreader '):
            texts = textt[12:]
            if texts == 'on':
                if lurking[to]['reply']['status']:
                    yepzLove(to, 'Reply reader already active')
                else:
                    lurking[to]['reply']['status'] = True
                    yepzLove(to, 'Success activated reply reader')
            elif texts == 'off':
                if not lurking[to]['reply']['status']:
                    yepzLove(to, 'Reply reader already deactive')
                else:
                    lurking[to]['reply']['status'] = False
                    yepzLove(to, 'Success deactivated reply reader')
            else:
                lurking[to]['reply']['message'] = texts
                yepzLove(to, 'Success set reply reader message to `%s`' % texts)
        else:
            yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('greet'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Greet Message 」'
        res += '\n├ Greetings Join Status : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Join Message : ' + settings['greet']['join']['message']
        res += '\n├ Greetings Leave Status : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\n├ Greetings Join Message : ' + settings['greet']['leave']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Greet'
        res += '\n│ • {key}Greet Join <on/off>'
        res += '\n│ • {key}Greet Join <message>'
        res += '\n│ • {key}Greet Leave <on/off>'
        res += '\n│ • {key}Greet Leave <message>'
        res += '\n╰───「 Self Bot 」'
        if cmd == 'greet':
            line.sendReplyMessage(msg_id, to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    yepzLove(to, 'Greetings join already active')
                else:
                    settings['greet']['join']['status'] = True
                    yepzLove(to, 'Success activated greetings join')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    yepzLove(to, 'Greetings join already deactive')
                else:
                    settings['greet']['join']['status'] = False
                    yepzLove(to, 'Success deactivated greetings join')
            else:
                settings['greet']['join']['message'] = texts
                yepzLove(to, 'Success change greetings join message to `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    yepzLove(to, 'Greetings leave already active')
                else:
                    settings['greet']['leave']['status'] = True
                    yepzLove(to, 'Success activated greetings leave')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    yepzLove(to, 'Greetings leave already deactive')
                else:
                    settings['greet']['leave']['status'] = False
                    yepzLove(to, 'Success deactivated greetings leave')
            else:
                settings['greet']['leave']['message'] = texts
                yepzLove(to, 'Success change greetings leave message to `%s`' % texts)
        else:
            yepzLove(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('kick '):
        if msg.toType != 2: return yepzLove(to, 'Failed kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                except TalkException as talk_error:
                    return yepzLove(to, 'Failed kick members, the reason is `%s`' % talk_error.reason)
                time.sleep(0.8)
            yepzLove(to, 'Success kick members, totals %i members' % len(mentions['MENTIONEES']))
        else:
            yepzLove(to, 'Failed kick member, please mention user you want to kick')
    elif cmd.startswith('vkick '):
        if msg.toType != 2: return yepzLove(to, 'Failed vultra kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                except TalkException as talk_error:
                    return yepzLove(to, 'Failed vultra kick members, the reason is `%s`' % talk_error.reason)
                time.sleep(0.8)
            yepzLove(to, 'Success vultra kick members, totals %i members' % len(mentions['MENTIONEES']))
        else:
            yepzLove(to, 'Failed vultra kick member, please mention user you want to kick')
            
    elif text.lower() == 'token chromeos':
           req = requests.get(url = 'https://api.eater.pw/token?header=CHROMEOS')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           yepzLove(to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           yepzLove(to, '{}'.format(b))
    elif text.lower() == 'token win10':
           req = requests.get(url = 'https://api.eater.pw/token?header=WIN10')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           yepzLove(to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           yepzLove(to, '{}'.format(b))
    elif text.lower() == 'token iospad':
           req = requests.get(url = 'https://api.eater.pw/token?header=IOSIPAD')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           yepzLove(to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           yepzLove(to, '{}'.format(b))
    elif text.lower() == 'token desktopwin':
           req = requests.get(url = 'https://api.eater.pw/token?header=DESKTOPWIN')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           yepzLove(to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           yepzLove(to, '{}'.format(b))
    elif text.lower() == 'token desktopmac':
           req = requests.get(url = 'https://api.eater.pw/token?header=DESKTOPMAC')
           a = req.text
           b= json.loads(a)
           link = b['result'][0]['linktkn']
           qrz = b['result'][0]['linkqr']
           tokenz['{}'.format(msg._from)]= link
           yepzLove(to, '{}'.format(qrz))
    elif text.lower() == 'done':
           a = tokenz['{}'.format(msg._from)]
           req = requests.get(url = '{}'.format(a))
           b = req.text
           yepzLove(to, '{}'.format(b))  
    elif text.lower() == "help" or text.lower() == "คำสั่ง":
                            s = "#FF0000"
                            sa = "🐭คท\n"
                            sa += "🐭ไอดีเรา\n"
                            sa += "🐭ชื่อเรา\n"
                            sa += "🐭ตัสเรา\n"
                            sa += "🐭รูปเรา\n"
                            sa += "🐭รูปวีดีโอเรา\n"
                            sa += "🐭ปกเรา\n"
                            sa += "🐭ข้อมูล\n"
                            sa += "🐭รีบอท\n"
                            sa += "🐭ออน\n"
                            sa += "🐭/ลบรัน\n"
                            sa += "🐭เชคค่า\n"
                            sa += "🐭แทค\n"
                            sa += "🐭ยกเชิญ\n"
                            ss = "\n"
                            sa += ""
                            ss += "🐰ตั้งapi [พิมเพื่อดูวิธี]\n"
                            ss += "🐰ล้างapi [คำที่จะลบ]\n"
                            ss += "🐰เชคapi\n"
                            ss += "🐰ล้างapi [คำที่จะลบ]\n"
                            ss += "🐰ก็อป @user\n"
                            ss += "🐰กลับร่าง\n"
                            ss += "🐰แปรงคท [MID]\n"
                            ss += "🐰ยูทูป [ข้อความ]\n"
                            ss += "🐰image [text(ภาษาอังกฤษ)]\n"
                            ss += "🐰ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                            ss += "🐰ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                            ss += "🐰ยกเลิก [ใส่จำนวนที่จะยกเลิก]\n"
                            ss += "\n"
                            ss += ""
                            sd = "🐷ดำ ส่งคท.\n"
                            sd += "🐷ขาว ส่งคท.\n"
                            sd += "🐷ดำ @user\n"
                            sd += "🐷ล้าง @user\n"
                            sd += "🐷เชคดำ\n"
                            sd += "🐷คทดำ\n"
                            sd += "🐷ล้างดำ\n"
                            sd += "🐷บินกลุ่ม\n"
                            sd += "🐷คิกเข้า\n"
                            sd += "🐷ตั้งแอด [ข้อความ]\n"
                            sd += "🐷ตั้งแทค [ข้อความ]\n"
                            sd += "🐷ตั้งคอมเม้น [ข้อความ]\n"
                            sd += "🐷ตั้งค้างเชิญ [จำนวน]\n"
                            sd += "🐷ตั้งมุดลิ้ง [ข้อความ]\n"
                            sd += "🐷ตั้งคนบล็อค [ข้อความ]"
                            se = "🐯เปิดแทค/ปิดแทค\n"
                            se += "🐯เปิดไลค์/ปิดไลค์\n"
                            se += "🐯เปิดไลค์/ปิดไลค์\n"
                            se += "🐯เปิดคอมเม้น/ปิดคอมเม้น\n"
                            se += "🐯เปิดบล็อค/ปิดบล็อค\n"
                            se += "🐯เปิดแอด/ปิดแอด\n"
                            se += "🐯เปิดกันรัน/ปิดกันรัน\n"
                            se += "🐯เปิดต้อนรับ/ปิดต้อนรับ\n"
                            se += "🐯เปิดคนออก/ปิดคนออก\n"
                            se += "🐯เปิดกาดนางฟ้า/ปิด\n"
                            se += "🐯เปิดคนออก/ปิดคนออก\n"
                            se += "🐯เปิดยกเลิก/ปิดยกเลิก\n"
                            se += "🐯เปิดติ๊กคนเข้า/ปิดติ๊กคนเข้า\n"
                            se += "🐯เปิดติ๊กคนออก/ปิดติ๊กคนออก\n"
                            se += "🐯เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                            sti = "🐘เปิดมุดลิ้ง/ปิดมุดลิ้ง\n"
                            sti += "🐘ตั้งติ๊กคนแอด\n"
                            sti += "🐘ลบติ๊กคนแอด\n"
                            sti += "• ตั้งติ๊กแทคแชท\n"
                            sti += "• ลบติ๊กแทคแชท\n"
                            sti += "🐘ตั้งติ๊กคนแทค\n"
                            sti += "🐘ลบติ๊กคนแทค\n"
                            sti += "🐘ตั้งติ๊กคนเข้า\n"
                            sti += "🐘ลบติ๊กคนเข้า\n"
                            sti += "🐘ตั้งติ๊กคนออก\n"
                            sti += "🐘ลบติ๊กคนออก\n"
                            sti += "🐘เขียน [ข้อความ]\n"
                            sti += "🐘ไอดีไลน์ [idline]\n"
                            sti += "🐘ดึง @user\n"
                            sti += "🐘บล็อค @user\n"
                            sti += "🐘เพิ่มเพื่อน @user\n"
                            sti += "🐘ลบเพื่อน @user"
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://i.pinimg.com/originals/df/97/3b/df973b04f198ff959f3cfba155f928a2.gif',
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🇹🇭คำสั่งส่วนตัว🇹🇭",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#990000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"꧁༺ஆืਹໂ√န༻꧂",
                                                     "uri":"https://line.me/ti/p/kK--UL9zvR"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://i.pinimg.com/originals/df/97/3b/df973b04f198ff959f3cfba155f928a2.gif',
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🇹🇭คำสั่งพิเศษ🇹🇭",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#FF0000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"꧁༺ஆืਹໂ√န༻꧂",
                                                     "uri":"https://line.me/ti/p/kK--UL9zvR"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://i.pinimg.com/originals/df/97/3b/df973b04f198ff959f3cfba155f928a2.gif',
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🇹🇭คำสั่งเปิด/ปิด🇹🇭",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": se, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#990000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"꧁༺ஆืਹໂ√န༻꧂",
                                                     "uri":"https://line.me/ti/p/kK--UL9zvR"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://i.pinimg.com/originals/df/97/3b/df973b04f198ff959f3cfba155f928a2.gif',
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🇹🇭คำสั่งตั้งค่า/ติดดำ🇹🇭",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                           #     "text": " "
                                         #   },
                                         #   {
                                            #    "type": "text",
                                           #     "text": " "
                                          #  },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
                                           #     "size": "lg",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            #{
                                            #    "type": "text",
                                            #    "text": " "
                                           # },
                                          #  {
                                           #     "type": "text",
                                            #    "text": " "
                                           # },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                          #      "text": "สนใจบอท ติดต่อได้ที่ปุ่มเลยค้ะ >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#FF0000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"꧁༺ஆืਹໂ√န༻꧂",
                                                     "uri":"https://line.me/ti/p/kK--UL9zvR"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://i.pinimg.com/originals/df/97/3b/df973b04f198ff959f3cfba155f928a2.gif',
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "🇹🇭คำสั่งทั่วไป🇹🇭",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#990000",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"꧁༺ஆืਹໂ√န༻꧂",
                                                     "uri":"https://line.me/ti/p/kK--UL9zvR"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Help Message",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
    elif text.lower() == "///ด่วน" or text.lower() == "/689":
                          groups = line.getGroupIdsJoined()
                          for group in groups:
                            s = "#FF0000"
                            sa = """🔥 โปรสมาชิกใหม่จัดไปโบนัส50%
🏰 SLOTTJ689 รวมทุกค่ายเกมส์
🎀 ภายใต้บริการไว้ในเว็บเดียว
---------------------------
🔥 การันตีเรื่องความชัวร์
🔥 ฝากไว-ถอนเร็ว ต้องที่นี่เท่านั้น
🔥 มีเกมหลากหลายค่ายให้คุณเลือก เช่น
     -918 Kiss 
     -Joker
     -Slotxo
     -Pussy888
     -SlotX
     -ยิงปลา 
     -และอื่นๆอีกมากมายให้ท่านเลือก
------------------------------"""
                            sa += """\n 👉สมัครง่ายๆผ่านระบบอัตโนมัติ 
------------------------------>"""
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://data.bloggif.com/distant/user/store/5/2/f/0/7a1b58cecaa8c64d1baa5c2d85300f25.jpeg',
 #                                               "aspectMode":"cover",
#                                                "margin":"xxl",
  #                                              "aspectRatio":"1:1",
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "SLOTTJ689",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#990000",
                                                "action":{
                                                    "type":"uri",
                                                    "label":"คลิ๊ก",
                                                    "uri":"https://secure.slottj689.com/register/5342"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "⚜️⚜️ เพจใหญ่ชัวสุดๆ ⚜️⚜️",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(group, data)
    elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#000000"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#000000",
                                                "separator": True,
                                               "separatorColor": "#000000"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#CC0033",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#CC0033"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#CC0033",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#CC0033",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#CC0033",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#CC0033",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#CC0033",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
    elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
    elif msg.text.lower().startswith("เพลสโต "):
                                query = removeCmd("เพลสโต", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
    elif msg.text.lower().startswith("รูป "):
                                query = removeCmd("รูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
    elif 'คท: ' in msg.text:
                  if msg._from in admin and Owner:
                     spl = msg.text.replace('คท: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "❋ตั้งข้อความเรียบร้อยแล้ว❋")
                     else:
                          settings["คอนแทค"] = spl
                          line.sendContact(to, "{}".format(str(spl)))

    elif msg.text.lower().startswith("#gbc: "):
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    groups = line.groups
                    for group in groups:
                        line.sendMessage(group, "{}".format(str(text_)))
                    else:
                        time.sleep(5)
                       # nadya.sendMessage(msg.to, str(settings["จำนวนกลุ่ม"]))
#                        nadya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))

    elif msg.text.lower().startswith("#pbc: "):
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    groups = line.groups
                    for group in groups:
                        line.sendImageWithURL(group, "{}".format(str(text_)))
                        line.sendContact(group, str(settings["คอนแทค"]))
#                    else:
 #                       nadya.sendMessage(to, "ส่งแล้ว ทั้งหมด {} กลุ่ม".format(str(len(groups))))
    elif msg.text.lower().startswith("#fbc: "):
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, "{}".format(str(text_)))
#                        nadya.sendImageWithURL(i, bc)
                        line.sendContact(i, str(settings["คอนแทค"]))
    elif msg.text.lower().startswith("#kbc: "):
                    sep = text.split(" ")
                    text_ = text.replace(sep[0] + " ","")
                    groups = line.groups
                    for group in groups:
                        line.sendImageWithURL(group, "{}".format(str(text_)))
def executeOp(op):
    try:
        print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 13:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])
#        if op.type == 15:
 #           if settings['greet']['leave']['status']:
  #              if '@!' not in settings['greet']['leave']['message']:
   #                 line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name))
    #            else:
     #               line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
      #  if op.type == 17:
       #     if settings['greet']['join']['status']:
        #        if '@!' not in settings['greet']['join']['message']:
         #           line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name))
          #      else:
           #         line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 15:
                          if settings["Welcome"] == True:
                            if op.param2 in op.param1:
                                return
                            g = line.getGroup(op.param1)
                            contact = line.getContact(op.param2)
                            cover = line.getProfileCoverURL(op.param2)
                            gname = g.name
                            name = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://www.img.in.th/images/06c596cc10f90b4f078efd2251460489.jpg',
                                                "aspectMode":"cover",
                                                "margin":"xxl",
                                                "aspectRatio":"16:25",
                                                "size": "full"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#990000",
                                                "action":{
                                                    "type":"uri",
                                                    "label":"คลิ๊ก",
                                                    "uri":"https://secure.slottj689.com/register/5342"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "⚜️⚜️ เพจใหญ่ชัวสุดๆ ⚜️⚜️",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(op.param1, data)
        if op.type == 17:
          #if settings['greet']['join']['status']:
                          if settings["Welcome"] == True:
                            if op.param2 in op.param1:
                                return
                            g = line.getGroup(op.param1)
                            contact = line.getContact(op.param2)
                            cover = line.getProfileCoverURL(op.param2)
                            gname = g.name
                            name = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#FF0000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://www.img.in.th/images/06c596cc10f90b4f078efd2251460489.jpg',
                                                "aspectMode":"cover",
                                                "margin":"xxl",
                                                "aspectRatio":"16:25",
                                                "size": "full"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type":"button",
                                                "style":"primary",
                                                "color":"#990000",
                                                "action":{
                                                    "type":"uri",
                                                    "label":"คลิ๊ก",
                                                    "uri":"https://secure.slottj689.com/register/5342"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "⚜️⚜️ เพจใหญ่ชัวสุดๆ ⚜️⚜️",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(op.param1, data)
        if op.type in [25,26]:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            yepzLove(to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                yepzLove(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        yepzLove(to, 'Success join to group ' + group.name)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    yepzLove(to, 'Execute command error, ' + str(talk_error))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    yepzLove(to, 'Execute command error, ' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    yepzLove(to, 'Success change picture profile')
                    settings['changePictureProfile'] = False
                elif settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    yepzLove(to, 'Success change cover profile')
                    settings['changeCoverProfile'] = False
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    yepzLove(to, 'Success change group picture')
                    settings['changeGroupPicture'].remove(to)
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = '╭───「 Sticker Info 」'
                    res += '\n├ Sticker ID : ' + msg.contentMetadata['STKID']
                    res += '\n├ Sticker Packages ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\n├ Sticker Version : ' + msg.contentMetadata['STKVER']
                    res += '\n├ Sticker Link : line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    res += '\n╰───「 Self Bot 」'
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return yepzLove(to, 'Failed get details contact with mid ' + mid)
                    res = '╭───「 Details Contact 」'
                    res += '\n├ MID : ' + mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 Self Bot 」'
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendReplyMessage(msg_id, to, parsingRes(res))
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                            contact = line.getContact(sender)
                            author = contact.displayName
                        else:
                            author = msg.contentMetadata['serviceName']
                        posturl = msg.contentMetadata['postEndUrl']
                        res = '╭───「 Details Post 」'
                        res += '\n├ Creator : ' + author
                        res += '\n├ Post Link : ' + posturl
                        res += '\n╰───「 Self Bot 」'
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if settings['autoRead']:
                line.sendChatChecked(to, msg_id)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            yepzLove(to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                yepzLove(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        yepzLove(to, 'Success join to group ' + group.name)
                if settings['mimic']['status']:
                    if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            tmp_text.append(text)
                        except:
                            pass
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendMessage(to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV2(to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendMessage(to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoRespond']['message'], [sender])
        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendReplyMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

def runningProgram():
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                executeOp(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()
