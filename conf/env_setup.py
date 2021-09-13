import os


class EnvSetup(object):

    # Environment variable of API host and endpoint with default values
    API_HOST = os.getenv('API_URL', 'http://localhost:8081')
    ENDPOINT = os.getenv('END_POINT', '/?q=simpsons%20characters&format=json')
