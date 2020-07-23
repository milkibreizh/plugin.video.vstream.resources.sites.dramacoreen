# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# 7
import re
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, DIALOG2 ,VSlog

#import sys
#import os
import time


DIALOG2=True

bVSlog=False #activation des logs

#[COLOR skyblue]Filmgratuit net[/COLOR]'
SITE_IDENTIFIER = 'dramacoreen'
SITE_NAME = 'Dramacoreen'
SITE_DESC = 'Series en streaming, streaming HD, streaming VF, séries, récent'

URL_MAIN = 'https://kdramavostfr.com/'

URL_MAIN = 'https://dramacoreen.cc/'
#https://dramacoreen.cc/
#https://kdramavostfr.com/
#https://dramacoreen.cc/
#https://myasietv.co/
#https://bondrama.com/
URL_SEARCH = (URL_MAIN + 'search?search=', 'showSeries')
URL_SEARCH_SERIES = (URL_SEARCH[0], 'showSeries')
FUNCTION_SEARCH = 'showSeries'

#https://kdramavostfr.com/?s=drama+complet  31
#https://kdramavostfr.com/?s=coreen+complet 29
#https://kdramavostfr.com/?s=japonais+complet 9
#https://kdramavostfr.com/?s=drama+chinois 3 (semble complet)
#https://kdramavostfr.com/?s=drama+taiwanais 4
URL_SEARCH = (URL_MAIN + '?s=', 'showSeries')

SERIE_SERIES = (URL_MAIN + '?s=drama+complet', 'showSeries')
SERIE_COREENS = (URL_MAIN + '?s=coreen+complet', 'showSeries')
SERIE_JAPONAIS = (URL_MAIN + '?s=japonais+complet', 'showSeries')
SERIE_CHINOIS = (URL_MAIN + '?s=drama+chinois', 'showSeries')
SERIE_TAIWANAIS = (URL_MAIN + '?s=drama+taiwanais', 'showSeries')

BLACKLIST=['go.vidfast.co','openload.co','youwatch.org','allvid.ch','vidlox.tv','streamango.com','estream.to']
#BLACKLIST=[]
#no secure site
#openload.co' ex https://openload.co/embed/c9Z1E7NBw74
#



#BLACKLIST=['go.ttrt']

#SERIE_SERIES = (URL_MAIN + 'series/page/1', 'showSeries')
#SERIE_GENRES = (True, 'showGenres')
#SERIE_NEWS = (URL_MAIN, 'showSeries')  # sur la page correspond à =' dernieres series en streaming'  ; ne contient pas les derniers episodes vf et vost du site
#SERIE_VIEWS = (URL_MAIN + 'top-series/page/1', 'showSeries')
#SERIE_ANNEES = (True, 'showYears')

def load():

    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Tous les dramas', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_COREENS [0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_COREENS [1], 'Dramas Coréens', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_JAPONAIS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_JAPONAIS[1], 'Dramas Japonais', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_CHINOIS [0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_CHINOIS [1], 'Dramas Chinois', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_TAIWANAIS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_TAIWANAIS[1], 'Dramas Taiwanais', 'series.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return

def showGenres():
    oGui = cGui()

    liste = []
    liste.append(['Action', URL_MAIN + 'series/genre/action_1'])
    liste.append(['Animation', URL_MAIN + 'series/genre/animation_1'])
    liste.append(['Aventure', URL_MAIN + 'series/genre/aventure_1'])
    liste.append(['Biopic', URL_MAIN + 'series/genre/biopic_1'])
    liste.append(['Comédie', URL_MAIN + 'series/genre/comaedie_1'])
    liste.append(['Comédie Musicale', URL_MAIN + 'series/genre/comaedie-musicale_1'])
    liste.append(['Documentaire', URL_MAIN + 'series/genre/documentaire_1'])
    liste.append(['Drame', URL_MAIN + 'series/genre/drame_1'])
    liste.append(['Epouvante Horreur', URL_MAIN + 'series/genre/epouvante-horreur_1'])
    liste.append(['Famille', URL_MAIN + 'series/genre/famille_1'])
    liste.append(['Fantastique', URL_MAIN + 'series/genre/fantastique_1'])
    liste.append(['Guerre', URL_MAIN + '/series/genre/guerre_1'])
    liste.append(['Policier', URL_MAIN + 'series/genre/policier_1'])
    liste.append(['Romance', URL_MAIN + 'series/genre/romance_1'])
    liste.append(['Science Fiction', URL_MAIN + 'series/genre/science-fiction_1'])
    liste.append(['Thriller', URL_MAIN + 'series/genre/thriller_1'])
    liste.append(['Western', URL_MAIN + 'series/genre/western_1'])
    liste.append(['Divers', URL_MAIN + 'series/genre/divers_1'])
    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSeries(sSearch=''):
    oGui = cGui()

    if sSearch:
        sUrl = sSearch.replace(' ', '+')
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    #teste
    #sUrl='https://kdramavostfr.com/page/2/?s=coreen+complet'
    
    ifVSlog('')
    ifVSlog('showSeries request='+sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    #VSlog(sHtmlContent)
    
    # url image title
    sPattern = 'moviefilm">\s*.+?href="([^"]*).+?src="([^"]*).+?alt="([^"]*)'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
        ifVSlog('pass1 showSeries no find')

    if (aResult[0] == True):
        ifVSlog('pass2')
         
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME+' check  pages....wait ')
        #progress_ .DIALOG2=True
        timestart= int(time.time())
        ivalide=0
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN )
        oGui.addNext(SITE_IDENTIFIER, 'load', '[COLOR teal]Page ' + 'Home'+' [/COLOR]', oOutputParameterHandler)
        
        for aEntry in aResult[1]:
            pr=''
            pr='  Valide = '+ str(ivalide)+'\r\n controle url : '+ str(aEntry[0])
            progress_.VSupdate(progress_, total,pr)
            
            if progress_.iscanceled():
                break
            
            if False :
                b=quickchek(aEntry[0])
                ifVSlog(str(b))
                sUrl2 = aEntry[0]
                ifVSlog('showSeries End call page contains valide host ...........................'+sUrl2 )
                sTitle = aEntry[2]
                sThumb = aEntry[1]
                if b :
                    ivalide=ivalide+1
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl2)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
                    
                    if '-saison-' in sUrl2 : 
                        oGui.addTV(SITE_IDENTIFIER, 'showSearchSaisons', sTitle, '', sThumb, '', oOutputParameterHandler)
                        ifVSlog('ADD showSearchSaisons')
                    else :
                        ifVSlog('ADD showEpisodes ')
                        oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, '', oOutputParameterHandler)     
                
                continue
            
            ifVSlog('pas normal si quickchek')
            sUrl2 = aEntry[0]
            ifVSlog('')
            ifVSlog('showSeries  call GetCheckHoster.............')
            bvalidehoster,toto= GetCheckHoster(sUrl2,True)
            ifVSlog('bvalidehoster' +str(bvalidehoster))
            if not bvalidehoster :
                ifVSlog('showSeries:...............End call page contains invalide host '+sUrl2 )
                continue
  
            ivalide=ivalide+1
            ifVSlog('showSeries End call page contains valide host ...........................'+sUrl2 )
            sTitle = aEntry[2]
            sThumb = aEntry[1]
            #if sThumb.startswith('/'):
                #sThumb = URL_MAIN[:-1] + sThumb
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            
            if '-saison-' in sUrl2 : 
                oGui.addTV(SITE_IDENTIFIER, 'showSearchSaisons', sTitle, '', sThumb, '', oOutputParameterHandler)
                ifVSlog('ADD showSearchSaisons')
            else :
                ifVSlog('ADD showEpisodes ')
                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, '', oOutputParameterHandler)  
            
        timestop= int(time.time())    
        timespan=timestop-timestart
        
        ifVSlog('time  :'+str(timespan))
        progress_.VSclose(progress_)

        sNextPage = __checkForNextPage(sHtmlContent)
        ifVSlog('(sNextPage1')
        ifVSlog('(link next sNextPage'+sNextPage[0][0])
        if (sNextPage != False and not sSearch):
            baddnext=True
            try :
                number = re.search('([0-9]+)',  sNextPage[0][0]).group(1)
                numbermax = re.search('([0-9]+)', sNextPage[0][1]).group(1)
                sl='/'
            except :
                ifVSlog('(exception sNextPage1')
                baddnext=False
                pass
            
            if baddnext:
                ifVSlog('(link next sNextPage'+sNextPage[0][0])
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage[0][0])
                oGui.addNext(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Page ' + str(number) + sl + str(numbermax)+' >>>[/COLOR]', oOutputParameterHandler)
           
            #try:
            #   number = re.search('([0-9]+)$', sNextPage).group(1)
            #   oGui.addNext(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Page ' + str(number) + ' >>>[/COLOR]', oOutputParameterHandler)
            #except :
                #VSlog('parse sNextPage failed')
                #pass
                
    if not sSearch:
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    sPattern = 'nextpostslink" rel="next".+?href="([^"]*)"'
    sPattern = 'class="nextpostslink".+?.+?href="([^"]*)".+?class="last".+?href="([^"]*)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return aResult[1]#[0]
    return False


def showEpisodes():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    # description
    sPattern = 'colo_cont">.+?>([^<]*)</p>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sDesc = aResult[1][0]
        sDesc = ('[COLOR coral]%s[/COLOR] %s') % (' SYNOPSIS : \r\n\r\n', sDesc)
    else:
        sDesc = ''
    
    #c'est de l'aproximation on prends juste le numero episode
    #https://kdramavostfr.com/melting-me-softly-vostfr-drama-complet/6/
    #req https://kdramavostfr.com/title/1 2 3 etc 
    #remarque le hoster du premier episode est accessible
    sPattern = '<div><span>Episode([^<]*)<'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        ifVSlog(len(aResult[1]))
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle',  sMovieTitle)
        oOutputParameterHandler.addParameter('sThumb', sThumb)
        oOutputParameterHandler.addParameter('sDesc', sDesc)    
        oGui.addEpisode(SITE_IDENTIFIER, 'showSearchSaisons', sMovieTitle, '', sThumb, sDesc, oOutputParameterHandler)
        
        
        for aEntry in aResult[1]:
            
            aEntry=str(aEntry).replace(' ', '')
            ifVSlog(aEntry)
            sUrl2 = sUrl+str(aEntry)
            sTitle = sMovieTitle + ' ' + 'Episode '+ str(aEntry)
            ifVSlog(sUrl2 )
            ifVSlog(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)  
            oGui.addEpisode(SITE_IDENTIFIER, 'seriesHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)   

    oGui.setEndOfDirectory()


def showSearchSaisons():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')

    #vu que le site est mal foutu on est oblige de faire une requete
    #pour savoir si il existe plusieur saisons
    # il peu exister aussi des doublons episode series
    ifVSlog('search =' + sMovieTitle)
    search=str(sMovieTitle).lower()
    search=search.replace('complet','')
    search=search.replace('drama','')
    search=search.replace('vostfr','')
    search=search.replace('saison','')
    search=search.replace('japonais','')
    search=search.replace('coréen','')
    
    ifVSlog('search =' + search)
    surlsearch = URL_MAIN + '?s='+search
    ifVSlog(surlsearch)
    oRequestHandler = cRequestHandler(surlsearch)
    sHtmlContent = oRequestHandler.request()
    #VSlog(sHtmlContent )
    #url img nom
    sPattern = 'moviefilm">\s*.+?href="([^"]*).+?src="([^"]*).+?alt="([^"]*)'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    AvailableSaison=[]
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
    
    if (aResult[0] == True):
        ifVSlog('Total Find'+str(len(aResult[1])))
        
        for aEntry in aResult[1]:
            ifVSlog('Find ='+aEntry[0])

            #saison-([^-]*)
            try :
                number = re.search('([0-9]+)', aEntry[0]).group(1)
                #number = re.search('saison-([^-]*)', aEntry[0]).group(1)
            except:
                ifVSlog('except')
                #continue #no pass ya pas de number
                number='0'
                pass

            number=str(number).replace(' ', '')
            
            #VSlog(number)
            #restricl link must contains  saison
            #if (not number in AvailableSaison) : #and ( 'saison' in aEntry[0] ):  if saison-([^-]*)
            
            if (not number in AvailableSaison)  and ( 'saison' in aEntry[0] ):  
                ifVSlog('pass4')
                AvailableSaison.append(number)
                sUrl = aEntry[0]
                sTitle=aEntry[2]
                sThumb=aEntry[1]  ## image can change (plusieurs version
            else:
                ifVSlog('not number or saison')
                continue
                
            ifVSlog('pass5')
            
            ifVSlog(sUrl )
            #sUrl = aEntry[0]
            #sTitle =  sMovieTitle + ' E' + aEntry[1]
            sdisplayTitle=sTitle
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sdisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def seriesHosters():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')

    ifVSlog('seriesHosters()')
    ifVSlog(sUrl)
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    #sPattern = '<iframe src="([^"]*)'
    #oParser = cParser()
    #aResult = oParser.parse(sHtmlContent, sPattern)
    
    boolresutl, aResult= GetCheckHoster(sUrl,True)
    ifVSlog('#####  passe seriesHosters')
    if ( boolresutl and len(aResult)>0):
        ifVSlog(len(aResult))
        ifVSlog(aResult)
        #ifVSlog('seriesHosters()'+str(len(aResult[1])))
        for aEntry in aResult:
            #https:..([^\/]*)
            
            ifVSlog(aEntry)
            sUrlhoster=aEntry
            #sHosterName = re.search('https:..([^\/]*)', sUrlhoster).group(1)
            sHosterName = re.search('https:..([^\/]*)', sUrlhoster).group(1)
            #sHosterName = re.search('https:..([^.]*)', sUrlhoster).group(1) 
            if sHosterName not in BLACKLIST:
                ifVSlog(sHosterName)
               
                sDisplayTitle = ('%s  [COLOR coral]%s[/COLOR]') % (sMovieTitle, sHosterName)
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrlhoster)
                oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oGui.addLink(SITE_IDENTIFIER, 'hostersLink', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def GetCheckHoster(sUrl,bcheck):
    
    #if len(BLACKLIST) == 0 :
        #return True,T
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = '<iframe src="([^"]*)'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    ifVSlog('GetCheckHoster : ')
    
    #blacklist=['go.vidfast.co','vidbm']
    #blacklist=['vidfast','vidbm']
    if (aResult[0] == True and not bcheck):
       
        ifVSlog('seriesHosters()'+str(len(aResult[1])))
        for aEntry in aResult[1]:
            #https:..([^\/]*)
            #https:..([^.]*)
            sUrlhoster=aEntry
            sHosterName = re.search('https:..([^\/]*)', sUrlhoster).group(1)
            #sHosterName = re.search('https:..([^.]*)', sUrlhoster).group(1)

        return True , aResult[1]

    else : False , False
    
    if (aResult[0] == True and bcheck):
        ifVSlog('GetCheckHoster: Hosters()' +sUrl)
        ifVSlog('GetCheckHoster: Hosters()' +str(len(aResult[1])))
        
        bvalidehost=False
        for aEntry in aResult[1]:
            #https:..([^\/]*)
            #https:..([^.]*)
            
            #if sUrlhoster not
            sUrlhoster=aEntry
            ifVSlog('GetCheckHoster: valide hoste : ' + sUrlhoster)
            if not 'https:' in sUrlhoster:
                sUrlhoster='https:'+sUrlhoster
                 
            try:
                sHosterName = re.search('https:..([^\/]*)', sUrlhoster).group(1)
                #sHosterName = re.search('https:..([^.]*)', sUrlhoster).group(1)
                #if  sHosterName not
                if sHosterName in BLACKLIST :
                    ifVSlog('GetCheckHoster: fin black site !!!! ; '+sHosterName )
                else :
                    
                    ifVSlog('GetCheckHoster: page = ok with host name ='+str(sHosterName ))
                    ifVSlog('#### GetCheckHoster:  page = ok with host url ='+str(sUrlhoster))
                    ifVSlog('GetCheckHoster : page = ok ')
                    bvalidehost=True
                    
                    return bvalidehost , aResult[1]
                
            except:
                ifVSlog('GetCheckHoster: execption !!!!!!!!!!! ')
                ifVSlog('GetCheckHoster: execption url result'+str(sUrl))
                ifVSlog('GetCheckHoster: execption  '+str(len(aResult[1])))
                ifVSlog('GetCheckHoster: execption with host url ='+str(sUrlhoster))
                continue
        
        ifVSlog('GetCheckHoster:  page = 1 ko ')
        return bvalidehost , aResult[1]

    
    else : 
        ifVSlog('GetCheckHoster: page = 2 ko ')
        return False , 'False'

def quickchek(sUrl):
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    #https://uqload
    #https://clipwatching
    #ok.ru 
    
    if( ('https://ok.ru' or 'https://uqload' or 'https://clipwatching') in sHtmlContent):
        ifVSlog('OK teste quick '+sUrl )
        return True
    else : 
        ifVSlog('KO teste quick '+sUrl )
        return False

def bCheckHosterpage(sHtmlContent):
    
    
    if len(BLACKLIST) == 0 :
        
        return True
    
    sPattern = '<iframe src="([^"]*)'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   

    for aEntry in aResult[1]:
        #https:..([^\/]*)
        #https:..([^.]*)
        
        #if sUrlhoster not
        sUrlhoster=aEntry
        
        sHosterName = re.search('https:..([^\/]*)', sUrlhoster).group(1)
        #sHosterName = re.search('https:..([^.]*)', sUrlhoster).group(1)
        #if  sHosterName not
        if sHosterName in BLACKLIST :
            ifVSlog('############## black site ; '+sHosterName )
        else :
            
            return True
       
    return False
    
def hostersLink():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    #oRequestHandler = cRequestHandler(sUrl)
    #oRequestHandler.request()
    #sHosterUrl = oRequestHandler.getRealUrl()
    ifVSlog('sHosterUrl =' + str(sHosterUrl))
    
    
    oHoster = cHosterGui().checkHoster(sHosterUrl) 
   
    if (oHoster != False):
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()

def ifVSlog(log):
    if bVSlog:
        try:  # si no import VSlog from resources.lib.comaddon
            VSlog(str(log)) 
        except:
            pass
    
    
    
