#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import playlist

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCc2rYk80b092uXrZkeQy8yIWdjLVSEfAg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
new_response_list = []
image_urls_list = []

country_playlist = {
      'Argentina-AR':'PLqOwx1vS-4dlenIYc1Qm0OiQpUrKUWbo_',
   #          'Australia-AU':'PLPWE2uZOmZQFbnFuZNFFRJcJRxH35qxis',
   #          'Austria-AT':'PLrMLyg9tDGAU3OjVm772TayaNi73doDct',
   #          'Belgium-BE':'PLBFwpcUbtP9ocPDsCfWoyKnzdRM5rWSvZ',
   #          'Brazil-BR':'PLcHQhiTqGSdLg0XMB4EBpmDPjii7KkDwy',
   #          'Canada-CA':'PLp12xt0S4J0UYXerKrIPCLTk15ZUzFdKz',
   #          'Chile-CL':'PL_NC8HG6tjCECcGjBS390ko-n1iRHnDu8',
   #          'Colombia-CO':'PLBAGzwMi_LCwsaXwJ0jOP49eqs-HDG46m',
   #          'Czech Republic-CZ':'PLQZXQIgnJzEqw47j50IeP8A5oF4bcYE6R',
   #          'Egypt-EG':'PLx-VLqfbYK4cchuS2q6X8HaBSs52FK7ft',
   #          'France-FR':'PLsa-dEwv56FZugrkS346xMx-dBT16uM8v',
   #          'Germany-DE':'PL0sHkSjKd2roowJbtmJJdBoCLq4eE6KMP',
   #          'Great Britain-GB':'PL-DfNcB3lim9IZmUXEjE1Ov0Ir1NDa3Yr',
   #          'Hong Kong-HK':'PLWahjRCqyk73VL_rL6Ec0lg5M1jVQhOBs',
   #          'Hungary-HU':'PLW80_JNbYOKZolk3GeIA7QTRsrlpRxmyk',
   #          'India-IN':'PL_yIBWagYVjyyqx_qPkbat5zufWZOyZEZ',
   #          'Ireland-IE':'PLqG_Qt4vmaV0KpH9rG-GeUZZi3fa3k8xS',
   #          'Israel-IL':'PLRRIH66XZsffscmrXTyfeyBjQ5ERroM0F',
   #          'Italy-IT':'PLw44__SfaGzptvJny_LOJ4WYXZKtGyBv6',
   #          'Japan-JP':'None',
   #          'Jordan-JO':'PLKju-FQsIypYiX-uHrF2ajlRYkL4l71A9',
      # 'Malaysia-MY':'PLWU3HTMYxVU3kqWgK0Gp7_3t_YQ2inxJL',
      # 'Mexico-MX':'PLfk71Rp386qjb5A38Bpatldih9vuX-EpE',
      # 'Morocco-MA':'PLsvl4NMyyNiWoswbCufti4XTCFnE_YKIt',
      # 'Netherlands-NL':'PLLi0G31kZGUkYtsfDc38On4WermeAISMQ',
      # 'New Zealand-NZ':'PLdgjd1TQOlx5h0R2EeTLp6mkLA4e6pbf6',
      # 'Peru-PE':'PL-Q1jyixDN8Yr_9RMxB_Llf2kJTZZhO-p',
      # 'Philippines-PH':'PLeGljrPoR_9Bp0cqtyONUtxMOy9Cu5UB6',
      # 'Poland-PL':'PL2pzgHdrZzwY_UkORbQqcrO1eyi4T-dsZ',
      # 'Russia-RU':'PLgMaGEI-ZiiZ0ZvUtduoDRVXcU5ELjPcI',
      # 'Saudi Arabia-SA':'PLnDIaDu4wl5arOct4QGFplPRcT_MtgKK_',
      # 'Singapore-SG':'PLsn0k7lyjYpkyFgKM8EPjXBp25rB7h2t-',
      # 'South Africa-ZA':'PLh5jaQxuZZZA9rFOfzJZgZ1qLuHR7ziDs',
      # 'South Korea-KR':'PLmtapKaZsgZt3g_uAPJbsMWdkVsznn_2R',
      # 'Spain-ES':'PLFpoEtn7p2i8KD-FlXsGLIT3zeSAnfpoY',
      # 'Sweden-SE':'PLn1aPDOSlmD8vLeP8S2KDogDcmCgtTmHg',
      # 'Switzerland-CH':'PL9KVSatdJqIhpIyMhwsbTMgj1pewYLXCi',
      # 'Taiwan-TW':'PLPv96SVEnDc0Ja1b64FXjNpJ4ujJkL1pi',
      # 'United Arab Emirates-AE':'PLWf2wBjOOgX3D0yy_PvDg9kSqMfjTI0nY',
      # 'United States-US':'PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-'
      }


def youtube_search(options):
  
  pl_id = options['pl_id']
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options['q'],
    part="id,snippet",
    #chart="mostPopular",
    maxResults=2,
    regionCode="IN"
  ).execute()
  new_response =  youtube.playlistItems().list(
    part="id,snippet",
    maxResults=2,

    playlistId=pl_id
  ).execute()

  videos = []
  channels = []
  playlists = []
  new_response_list = []
  image_urls_list = []  
  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    

  for i in range(2):
    try:
      new_response_list.append(new_response['items'][i]['snippet']['title'])
      image_urls_list.append(new_response['items'][i]['snippet']['thumbnails']['default']['url'])
      
    except:
      pass  
  new_response_list = new_response_list+videos  
  
  #print new_response_list  

  return new_response_list
  #these

  
  

def image_urls():
  return image_urls_list


def start(name):
  
    parts = name.split("-")   
    pl_id = country_playlist[name]
        
    args = {'q':'Popular Right Now -'+parts[0],'auth_host_name':'localhost', 
    'auth_host_port':[8080, 8090], 'logging_level':'ERROR', 'max_results':2, 'noauth_local_webserver':False,'pl_id':pl_id}

    try:
      youtube_search(args)
      
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  


