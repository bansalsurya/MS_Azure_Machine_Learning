import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Overall rank': "1",   
                            'Country or region': "Finland",   
                            'Score': "7.769",   
                            'GDP per capita': "1.34",   
                            'Social support': "1.587",   
                            'Healthy life expectancy': "0.986",   
                            'Freedom to make life choices': "0.596",   
                            'Generosity': "0.153",   
                            'Perceptions of corruption': "0.393",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7aae641fe8b5420f859df420875b5dd5/services/e9df709317814b71bf76bab07d34915c/execute?api-version=2.0&format=swagger'
api_key = 'zAs/CbLgudwsskgDtn6+GpVGIriFSlO1a6WgdDDw17cxEVNFqLEe20Rzozpdr0RSXLprdwvTzezoAa/3vcenZA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))