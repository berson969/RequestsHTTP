import os
import requests
from pprint import pprint


class YaUploader:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def upload_file(self, file_name: str):
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_name.split('/').pop(), 'overwrite': True, 'fields': 'href'}
        url = f'{self.host}v1/disk/resources/upload/'
        link_response = requests.get( url, params=params, headers=headers)
        upload_link = link_response.json()['href']
        full_path = os.path.join(os.getcwd(),file_name)
        response = requests.put(upload_link, data=open(full_path, 'rb'), headers=headers)
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_for_upload = 'RequestsHTTP/yadisk.py'
    token = 'AQ______spNaAADLW8ptMO51lU-Ko0Ze0qWmaB4'
    uploader = YaUploader(token)
    result = uploader.upload_file(file_for_upload)
