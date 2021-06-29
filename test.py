import requests
import spotipy



CLIENT_ID = '19c1eccd1f02498faad82917e19d5042'
CLIENT_SECRET = 'be9c7e5056fc460cb1d2af8d121efce3'
auth_url = 'https://accounts.spotify.com/api/token'

data2 = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}



auth_response = requests.post(auth_url, data2)
auth_response_data = auth_response.json()
print(auth_response_data)

print(auth_response.status_code)

access_token = auth_response_data['access_token']
print(access_token)
headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'
artist_id = '7dGJo4pcD2V6oG8kP0tJRR'
print("test")
r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', headers = headers)
d = r.json()
for album in d['items']:
  print(album['name'], '---', album['total_tracks'])
