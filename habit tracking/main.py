import requests
import datetime

token = "e17pk2110064"
username = "rajeevprakash"
url = " https://pixe.la/v1/users"
graphid = "graph1"
parameters = {
    "token" : token,
    "username":username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=url,json=parameters)
# print(response.text)


graph_url_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

header = {"X-USER-TOKEN":token}
graph_parameters = {
    "id" : "graph1",
    "name":"coding hours",
    "unit" : "hour",
    "type": "float",
    "color":"ajisai",

}
# response2 = requests.post(url=graph_url_endpoint,json=graph_parameters,headers=header)
#
# print(response2.text)
today_date = datetime.datetime.now()
today_date = datetime.datetime(year=2021,month=1,day=25)


pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graphid}"
pixel_parameters = {
    "date": datetime.datetime.strftime(today_date,"%Y%m%d"),
    "quantity" : "4",


}
response3 = requests.post(url=pixel_endpoint,json=pixel_parameters,headers=header)
print(response3.text)