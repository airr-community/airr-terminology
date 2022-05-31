import requests
import hashlib
import os

config = {
    'zenodo_token': os.environ['ZENODO_TOKEN'],
    'zenodo_host': 'sandbox.zenodo.org',
    'original_record_id': 1066300,
    'filename_pdf': 'airrcommunityterminology.pdf'
}

original_record_url = 'https://' + config['zenodo_host'] + '/api/records/' + str(config['original_record_id'])
original_record = requests.get(
    original_record_url,
    params={'access_token': config['zenodo_token']}
)
# Response 200

latest_record_url = original_record.json()['links']['latest']
latest_record = requests.get(
    latest_record_url,
    params={'access_token': config['zenodo_token']}
)
# Response 200
latest_record_id = latest_record.json()['id']

new_record_request = 'https://' + config['zenodo_host'] + '/api/deposit/depositions/' + str(latest_record_id) + '/actions/newversion'
new_record_request_response = requests.post(
    new_record_request,
    params={'access_token': config['zenodo_token']}
)
# Response 201

draft_record_url = new_record_request_response.json()['links']['latest_draft']
draft_record = requests.get(
    draft_record_url,
    params={'access_token': config['zenodo_token']}
)
# Response 200
draft_record_id = draft_record.json()['id']

draft_record_file_list = requests.get(
    'https://' + config['zenodo_host'] + '/api/deposit/depositions/' + str(draft_record_id) + '/files',
    params={'access_token': config['zenodo_token']}
)
# Response 200

responses_file_delete = []
for current_file in draft_record_file_list.json():
    responses_file_delete.append(requests.delete(
        'https://' + config['zenodo_host'] + '/api/deposit/depositions/' + str(draft_record_id) + '/files/' + current_file['id'],
        params={'access_token': config['zenodo_token']}
    ))
# Response 204

with open(config['filename_pdf'], 'rb') as file_upload:
    response_file_deposition = requests.post(
        'https://' + config['zenodo_host'] + '/api/deposit/depositions/' + str(draft_record_id) + '/files',
        data={'name': 'AIRR-Community-Terminology.pdf'},
        files={'file': file_upload},
        params={'access_token': config['zenodo_token']}
    )
    # Response 201
    file_upload.seek(0, 0)
    file_upload_checksum = (
        hashlib.md5(file_upload.read()).hexdigest() == response_file_deposition.json()['checksum']
    )
    # Hash comparison True

# Update Version tag in metadata

publish_request = requests.post(
    'https://' + config['zenodo_host'] + '/api/deposit/depositions/' + str(draft_record_id) + '/actions/publish',
    params={'access_token': config['zenodo_token']}
)
