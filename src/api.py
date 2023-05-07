from bs4 import BeautifulSoup
import requests
from urllib import parse

BASE_URL = 'http://www.bxwa.com'


class API:
    def __init__(self):
        pass

    @staticmethod
    def get_project_page_url(city_id):
        if city_id == 'glue_16':  # Thurston is whack
            return 'http://www.bxwa.com/bxwa_toc/pub/1440/toc.html'

        city_page_url = f'http://www.bxwa.com/bxwa_toc/pub/{city_id}.html'
        resp = requests.get(city_page_url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        terms_url = None
        for a in soup.find_all('a'):
            if 'Projects Bidding' in a.text:  # Point of weakness
                terms_url = a['href']
        # If not found, just take first link and hope it works
        if not terms_url:
            terms_url = soup.find('a')['href']

        query = parse.parse_qsl(parse.urlsplit(terms_url).query)
        return BASE_URL + query[0][1]

    @staticmethod
    def get_projects(city_id):
        project_page_url = API.get_project_page_url(city_id)

        resp = requests.get(project_page_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        base_url = project_page_url.replace('/toc.html', '')

        projects = []
        for item in soup.find_all('tr'):
            time_element, name_element = item.find_all('td')
            a = time_element.find('a')
            url = base_url + '/' + a['href']
            time = a.text
            name = name_element.text
            projects.append({'time': time, 'name': name, 'url': url})
        return projects
