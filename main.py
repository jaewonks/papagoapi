from flask import Flask, render_template, request, jsonify
import sys
import requests
import re

application = Flask(__name__)

def init(name):
  if '구찌' in name:
    return 'GC'
  elif '로저비비에' in name:
    return 'RV'
  elif '루이비통' in name:
    return 'LV' 
  elif '마르니' in name:
    return 'MR' 
  elif '멀버리' in name:
    return 'MUL' 
  elif '몽클레어' in name:
    return 'MC' 
  elif '미우미우' in name:
    return 'MIU' 
  elif '발렌시아가' in name:
    return 'BG' 
  elif '발렌티노' in name:
    return 'VT' 
  elif '보테가베네타' in name:
    return 'BV' 
  elif '생로랑' in name:
    return 'YSL' 
  elif '샤넬' in name:
    return 'CH'   
  elif '셀린느' in name:
    return 'CEL' 
  elif '아르켓' in name:
    return 'AK' 
  elif '알렉산더맥퀸' in name:
    return 'MQ' 
  elif '에르메스' in name:
    return 'H'   
  elif '토리버치' in name:
    return 'TORY'   
  elif '토즈' in name:
    return 'TOD' 
  elif '톰브라운' in name:
    return 'TB' 
  elif '페라가모' in name:
    return 'FR' 
  elif '펜디' in name:
    return 'FD' 
  elif '프라다' in name:
    return 'PR' 
  elif '버버리' in name:
    return 'BBR' 
  elif '지안비토로시' in name:
    return 'GVT' 
  elif '아크네스튜디오' in name:
    return 'ACN' 
  elif '로에베' in name:
    return 'LEW' 
  elif '디올' in name:
    return 'DR' 
  elif '스텔라매카트니' in name:
    return 'STM' 
  elif '마놀로블라닉' in name:
    return 'MNB' 
  elif '메종 마르지엘라' in name:
    return 'MM' 
  elif '로로피아나' in name:
    return 'LRP' 
  elif '막스마라' in name:
    return 'MAX'
                    

def char(name):
  spname = name.split(' ')[1] 
  if len(spname) < 4: 
    spname = name.split(' ')[1] + name.split(' ')[2]

  pattern = '[^\w\s]'                                          
  text = re.sub(pattern=pattern, repl=' ', string=spname).replace(' ','')
  return text

def abbre(name):
  if 'BOTTEGA VENETA' in name:
    return name.replace('BOTTEGA VENETA','BOTTEGAVENETA')
  elif 'ROGER VIVIER' in name:
    return name.replace('ROGER VIVIER','ROGERVIVIER')
  elif 'SAINT LAURENT' in name:
    return name.replace('SAINT LAURENT','SAINTLAURENT')
  elif 'MIU MIU' in name:
    return name.replace('MIU MIU','MIUMIU')
  elif 'TOM BROWN' in name:
    return name.replace('TOM BROWN','TOMBROWN')
  elif 'MAX MARA ' in name:
    return name.replace('MAX MARA','MAXMARA')
  else : 
    return name

def shoseSize(size): 
  if 'EU' in size:
    re = size.replace('EU','')
  elif 'UK' in size: 
    re = size.replace('UK','')
  elif 'US' in size: 
    re = size.replace('US','')
  else : 
    re = size  
  if '.' in re: 
    return re.replace('.','') 
  else :
    return re   

def papago(text):
  request_url = "https://openapi.naver.com/v1/papago/n2mt"
  headers = {"X-Naver-Client-Id": "2Cudld_dW4HaSzleLPTT", "X-Naver-Client-Secret": "3VnQ1L_7Ld"}
  params = {"source": "ko", "target": "en", "text": text}
  response = requests.post(request_url, headers=headers, data=params)
  result = response.json()
  result1 = result['message']['result']['translatedText']
  translated = result1.upper()
  print(translated)
  return translated

@application.route('/')
def index():
  return render_template('index.html')

@application.route('/trans', methods=['GET'])
def trans():
  if request.method == 'GET':
    name = request.args.get('name')
    color = request.args.get('color')
    size = request.args.get('size')
    print('name :', name)
    print('color :', color)
    print('size :', size)
    first = init(name)
    traname = papago(name)
    orgname = abbre(traname)
    second = char(orgname)[:4]
    third = papago(color)[:2]
    forth = shoseSize(size)

    code = str(first) + str(second) + str(third) + 'S' + str(forth)
    return code

if __name__ == '__main__':
  application.run(host='0.0.0.0', port=5000)
