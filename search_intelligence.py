import requests

intelligence_list = {}

def get_search_hero(name):
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}')
        intelligence_list[name] = int(response.json()['results'][0]['powerstats']['intelligence'])
        

if __name__  in '__main__':
        get_search_hero('Hulk')
        get_search_hero('Captain America')
        get_search_hero('Thanos')
        print(f'The smartest character is {max(intelligence_list.items(), key=lambda x: x[1])[0]}')