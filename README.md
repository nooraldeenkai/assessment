### FastApi Model Deployment into Heroku 
The app provides a callable endpoint that runs a machine learning model on the input text to determine the languge of the text


main app url : 

https://language-detection-tcdx.herokuapp.com


## Supported Languages : 
[
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]

## Endpoints

### /

-method : GET

#### Request Parameters

N/A 

#### Expected Response
{"healthcheck": "OK"}

Curl Example : 
``` curl -X 'GET'  'https://language-detection-tcdx.herokuapp.com/'  -H 'accept: application/json'``` 


==============================================================================================================


### /language

-method : POST

#### Request Parameters

- text: str (required)

#### Expected Response

- Language: str


Curl Example : 
``` curl -X 'POST'  'https://language-detection-tcdx.herokuapp.com/language'  -H 'accept: application/json'  -H 'Content-Type: application/json'  -d '{ "text": "Hello World" }'``` 
