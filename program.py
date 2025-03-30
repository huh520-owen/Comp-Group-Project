import ast
import requests
web = requests.get("https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TML&sta=HOM")
dictionary = ast.literal_eval(web.text)
print(dictionary)
