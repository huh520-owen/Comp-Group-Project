import ast
import requests

# Sending an HTTP GET request to fetch data from the specified API URL
web = requests.get("https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TML&sta=HOM")
# Change the element scraped from the URL to dictionary
dictionary = ast.literal_eval(web.text)

print(dictionary)
