import requests
import json
from time import sleep
import csv

session = requests.Session()
with open('test_numbers1.txt', 'r') as f:
    headers = { 
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With':'XMLHttpRequest',
                'cookie':'',
        }
    for number in f:
        number = number.strip()
        url = 'https://www.giffgaff.com/top-up/another-ggnumber?phone_number='+str(number)
        cookie = 'BIGipServerPOOL-giffgaff.com=!6X9/leZmK36jXjUitK9EmXm5liXu5u1nZmikaCN2vUejBzT8okAiPgsOwcOkbguVKnnbekorVmKlWiY=; visid_incap_2118422=WorDggjCQTGj0mRF0Ul7S4j/LV0AAAAAQUIPAAAAAADhVycwUSYKHfo+wAVRkwnJ; _ga=GA1.2.758262434.1563296733; _gid=GA1.2.1454056186.1563296733; visid_incap_1274813=j7ePbIhRQQqPBYWjlp6iv9wDLl0AAAAAQUIPAAAAAACrqxRsorS1E88tWZCvbxGz; _gcl_au=1.1.1322303299.1563296734; _cs_c=1; _fbp=fb.1.1563296735441.184043889; remember_login=b%3A0%3B; _gaexp=GAX1.2.4cxT6nKHSf6abmCuDYe2Zw.18151.0!9wBNdLR3SayKIN5b1yK5Yw.18185.1; incap_ses_969_1274813=UjAeZf1ijxgluI+UMZVyDVEFLl0AAAAA//EU9FEjtw6kZQXRJbd6ZQ==; visid_incap_925109=okQ/8YRcSuO2meZY27QhbFYFLl0AAAAAQUIPAAAAAABmsKvpz6F3rhJfyoZyLpjn; incap_ses_969_925109=olkUccJSmhn4uY+UMZVyDVcFLl0AAAAAwEChUKtYLzXfslZVBqqqLg==; nlbi_1274813=kQpFS7I/nC2FRibIR65ayQAAAAAjIVgAdD2yCGYPeVFpcuNL; __ggUtmz=(organic); ggM=True; __s_idk__=e1861866-ccc1-49c7-88f2-4330f9ca11a1; RateSetterSSO=~2NQdkUhGdih3DwtDR~Lejzzwd0ECpdykKO8uB-e47vRqdovqK2t5nXcENVFD4u1-WKv0DhlHrLMGomwr40; esportsSSO=~2O0fMarSzxS0X6T5h~SgFZOgIA4MYkBdoxoqboiL-CuXehkZ-dM_U0585dweOBo8yWeuSx4yoF01lzfbCB; ideaLabs=~2UPoL9f1hZEbRjwPh~QHmPbXFvJ67UFgP1ZXQ8kiAOo98SUsE6hsqpEIqvhj0.; expertHelpers=~25gzF4kWv1RMOQGHD~uRL4SoOLJ8tfVI2rlZlYlnZ_SomhZs8qCto7sDigqhM.; moneySSO=~2P7GUqEZTJ8Ol4gld~9UZQ0fpY8w5_dmOq3klf9Le4IXP5UDbmNCcRceEpkS0.; lithiumSSO%3Anapa=~2odKqG33FMZ7Ao5Um~1nR64YPbHSDz6TRcVXQy0TVViKdlTEUUAWRo8Daa-v0_HdmG99xEMuNwZIxK7uP0OtHhDigLG-OKsIBBwJs9VWI4LhcIUrdaidBNLCXCRIk6zxwffCSS41N8oSK4xD8KKNLCdfSw8AWXWyxV0lFYzxPC8s_q1Tn5tV9i1m_Ptnm0Ec3nwNZK5qgxHQ6boSeI3TFoWllt8iiuOqeQ_ZzWY5MAELIPzVpwxOxXV8LmA3ZI3dGT-pWa-gckfUPIljK4Bnj4exKdYueXUKWwCjNjkUS2f3SUpghWzyRDRbezE7AEhZamoY2Kx0CsVCn0h5khnF2vwm5Spkx2lr0k9UtTCw..; giffgaff=sotljg519like7f15q5rgbb8ft; incap_ses_741_2118422=5QGWcOHURw4T8gIMmpBICkofLl0AAAAA3xsdllwUdBYEQQjmW0yV5A==; AMP_TOKEN=%24NOT_FOUND; napaId=14429582; napaUser=kubac60; lithiumSSO:napa=~2yl1sDuvhBBYiOZVK~tN9zORQiMy5K8GiYOwYnTECtbdoAxBTXwC1xBTZVW_Q8Gs89QOj7hcyE7z2SiMqnc57At9P5_JahIIy1loUCYOKa4C1C7y-Q2OrrnR3cFUS65bZw-iNuRks2aA4Plb7M9rhK-j7ZHmEimLCk44C81Iai9xXb0uIdb3VyvBV7nnzAL9tdQHfM_a7tr_2Gy9jSh1qPZj08XZspjqlCAKONTmJaSdrfDgVc45eHhUKCtdLe82ZUPgxVmNhIIkcW-4oaz6wA7UYsWEpmybSmUGr38XtzU5NfaVY0p3XdVqfKaX8.; _tq_id.TV-54908127-1.8ff1=b0e21dd9fd5df235.1563296735.0.1563310271..; _cs_id=42997e8c-45c3-a8d5-eeba-1b4bd0fb6ce1.1563296734.3.1563310270.1563305809.1.1597460734697; _cs_s=6.0; _gat_UA-10328417-1=1' 
        headers['cookie'] = cookie
        r1 = requests.request('GET', url, headers=headers)
        print(r1.text) 
        if 'html style' not in r1.text:
            output = json.loads(r1.text)['msg']
            if output == 'Enter a valid giffgaff mobile number (starting 07)':
                print('Invalid Number',number)
                f1 = csv.writer(open('InvalidOutput.txt','a'))
                f1.writerow([str(number)])
            elif 'Fellow giffgaffer' in output:
                print('Valid Number',number)
                f2 = csv.writer(open('ValidOutput.txt','a'))
                f2.writerow([str(number)])
        sleep(10)