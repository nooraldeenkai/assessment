### FastApi Model Deployment into Heroku 
The app provides a callable endpoint that runs a machine learning model on the input text to determine the languge of the text


main app url : 

https://language-detection-tcdx.herokuapp.com


## Endpoints

### /
-method : #GET


#### Request Parameters

#### Expected Response
{"healthcheck": "OK"}

============================================================================================================================


### /language

-method : #POST

#### Request Parameters
- text: str (required)

#### Expected Response
- Language: str
