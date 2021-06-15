import requests

url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=welcome to Python workshop on 25-7&language=english&route=p&numbers=9763978679"
headers = {
'authorization': "aECuj2pb1lt8GWXRyL5gdBmnoIxqVZ9DASrPiwh70zeQHc4fJ2cwonXBkAR40USFVhf7YIPqby9x",

'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
