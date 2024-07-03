# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_7e2baeefef2e19c7335879c26d4101b164850f43ed295130ce4b95b22aad3ce0'
# Add the files you want to upload to Edge Impulse
files = [
    'EEG_data/EEG.ojos_abiertos_cerrados.csv',
]

label = 'abrir_cerrar_ojos'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'application/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)