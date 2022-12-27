import math
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY="5HDIXYBE1ISOVV8T"
from requests import *
parametros={
    'function':"TIME_SERIES_DAILY_ADJUSTED",
    'symbol':STOCK_NAME,
    'outputsize':'compact',
    'apikey':API_KEY
}
resposta=requests.get(url=STOCK_ENDPOINT,params=parametros)
resposta.raise_for_status()
dados=resposta.json()
dias=list(dict.keys(dados['Time Series (Daily)']))
print(dados['Time Series (Daily)'])
ontem_anteontem=[]
for i in range(2):
    ontem_anteontem.append(dias[i])
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
fecho_anteontem=float(dados['Time Series (Daily)'][ontem_anteontem[1]]['4. close'])
fecho_ontem=float(dados['Time Series (Daily)'][ontem_anteontem[0]]['4. close'])-7
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if fecho_ontem-fecho_anteontem> fecho_anteontem*0.05 or fecho_ontem-fecho_anteontem<-fecho_anteontem*0.05:
    alteração_valor=math.floor(((fecho_ontem-fecho_anteontem)/fecho_anteontem)*100)
    news_key='9414defd32984a599e70bdba555726a3'
    parametros_news={
        'q':COMPANY_NAME,
        'from':ontem_anteontem[0],
        'language':'pt',
        'apiKey':news_key
    }
    print('Get news')
    resposta_news=requests.get(url=f"https://newsapi.org/v2/everything",params=parametros_news)
    resposta_news.raise_for_status()
    noticias=resposta_news.json()
    print(noticias)
    primeiros3=[[]]
    for news in range(3):
        primeiros3.append(noticias['articles'][news]['title'])
        primeiros3.append(noticias['articles'][news]['description'])
        primeiros3.append(noticias['articles'][news]['url'])
    print(primeiros3)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    from twilio.rest import Client
    sid_conta=ACCOUNT_SID_TWILLIO
    token=MY_AUTH_TOKEN_TWILLIO
    Twillio_Api='gyDc1kXy43ioe4oyCiAGG4LgQRjKrrMY'
    cliente=Client(sid_conta,token)
    if alteração_valor>0:
        for i in range(len(primeiros3)-1):
            if i<4:
                mensagem=cliente.messages.create(
                    to="DESTINARARIO_NUMERO",from_='MEU_NUMERO',
                    body=f'\n\n TSLA sofre alteração de 🔺{alteração_valor}\n\n'
                         f'{primeiros3[1]}'
                         f'{primeiros3[2]}'
                         f'{primeiros3[3]}')
            if i<7:
                mensagem = cliente.messages.create(
                    to="+5533988012359", from_='+16198536328',
                    body=f'\n\n TSLA sofre alteração de 🔺{alteração_valor}\n\n'
                         f'{primeiros3[4]}'
                         f'{primeiros3[5]}'
                         f'{primeiros3[6]}')
            if i<10:
                mensagem = cliente.messages.create(
                    to="+5533988012359", from_='+16198536328',
                    body=f'\n\n TSLA sofre alteração de 🔺{alteração_valor}\n\n'
                         f'{primeiros3[7]}'
                         f'{primeiros3[8]}'
                         f'{primeiros3[9]}')
            else:
                if alteração_valor > 0:
                    for i in range(len(primeiros3) - 1):
                        if i < 4:
                            mensagem = cliente.messages.create(
                                to="+5533988012359", from_='+16198536328',
                                body=f'\n\n TSLA sofre alteração de 🔻{alteração_valor}\n\n'
                                     f'{primeiros3[1]}'
                                     f'{primeiros3[2]}'
                                     f'{primeiros3[3]}')
                        if i < 7:
                            mensagem = cliente.messages.create(
                                to="+5533988012359", from_='+16198536328',
                                body=f'\n\n TSLA sofre alteração de 🔻{alteração_valor}\n\n'
                                     f'{primeiros3[4]}'
                                     f'{primeiros3[5]}'
                                     f'{primeiros3[6]}')
                        if i < 10:
                            mensagem = cliente.messages.create(
                                to="+5533988012359", from_='+16198536328',
                                body=f'\n\n TSLA sofre alteração de 🔻{alteração_valor}\n\n'
                                     f'{primeiros3[7]}'
                                     f'{primeiros3[8]}'
                                     f'{primeiros3[9]}')

