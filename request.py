import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=c611c55e1083269987ca650f3025ddce7004057c"

answer = {'answer': open('answer.json', 'rb')}
response = requests.post(url=url, files=answer)
print(response.status_code)
print(response.json())