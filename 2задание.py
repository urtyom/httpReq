import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params_1 = {'path': '/'+file_path}
        headers_1 = {'Authorization': 'OAuth '+self.token}
        response = requests.get(url, headers=headers_1, params=params_1)

        if 200 <= response.status_code < 300:
            data = response.json()
            url = data['href']
            with open(file_path, 'rb') as f:
                requests.post(url, files={'file': f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = open('path.txt').read()
    token = open('token.txt').read()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
