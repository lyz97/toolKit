import http.client
import hashlib
import urllib
import random
import json


def translator(q):

    appid = '20210609000858443'  # 填写你的appid
    secretKey = 'i0q3y_cNbwLIasnOGGEU'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'en'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        result = result['trans_result'][0]['dst']

        return result

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()


if __name__ == '__main__':
    text = translator('apple')
    print(text)
