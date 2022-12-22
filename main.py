import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os


def get_src(url: str) -> None:
    """
    It gets the source code of the web-page and saves it to the file

    :param url: str - the url of the web-page
    """
    headers = {'user-agent': f"{UserAgent(browsers=['edge', 'chrome']).random}"}
    request = requests.get(url=url, headers=headers)

    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/source.html', 'w', encoding='utf-8') as file:
        file.write(request.text)


def collect_data():
    with open('data/source.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')


if __name__ == '__main__':
    try:
        get_src('ENTER YOUR URL')  # Commit this line after create data/source.html
        collect_data()
    except Exception as exc:
        raise SystemExit(f'\033[34m{exc}')
