
BASE_URL = 'https://api-gtm.grubhub.com/'
AUTH_BASE_URL = BASE_URL + 'auth'
REST_BASE_URL = BASE_URL + 'restaurants/'
RATINGS_BASE_URL = 'ratings/'

AUTH_REQUEST_HEADERS = {
    'Authorization':'Bearer',
    'Content-type':'application/json;charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://www.seamless.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}


AUTH_PAYLOAD = '{"brand":"SEAMLESS","client_id":"beta_seamless_ayNyuFxxVQYefSAhFYCryvXBPQc","scope":"anonymous"}'
