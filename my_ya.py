import requests
def create_folder(token, path):
    resp = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers={'Content-Type': 'application/json', 'Authorization' : str(token)}, params={'path' : str(path)})
    return resp.status_code

if __name__ == "__main__":
    create_folder(input('Enter your Ya token: '), input('Enter folder name: '))