import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Overall rank': "1",   
                            'Country or region': "",   
                            'Score': "1",   
                            'GDP per capita': "1",   
                            'Social support': "1",   
                            'Healthy life expectancy': "1",   
                            'Freedom to make life choices': "1",   
                            'Generosity': "1",   
                            'Perceptions of corruption': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7aae641fe8b5420f859df420875b5dd5/services/d9c36a9fdf984fc38b5417eb42d8df66/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
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
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Overall rank': "1",   
                            'Country or region': "",   
                            'Score': "1",   
                            'GDP per capita': "1",   
                            'Social support': "1",   
                            'Healthy life expectancy': "1",   
                            'Freedom to make life choices': "1",   
                            'Generosity': "1",   
                            'Perceptions of corruption': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7aae641fe8b5420f859df420875b5dd5/services/d9c36a9fdf984fc38b5417eb42d8df66/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
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
