import requests

def parse_json_response(jre):
    for it in jre['data']:
        for k , v in it.items():
            print('%s : %s' %(k,v))
        print('*****************')

def generate_links():
    links = list()
    base_url = 'https://www.topuniversities.com/sites/default/files/qs-rankings-data/'
    alink = dict()
    alink['sub'] = 'anatomy-physiology'
    alink['url'] =  base_url+'926873.txt?_=1586339371982'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'computer-science-information-systems'
    alink['url'] = base_url+'930690.txt?_=1586339550172'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'chemistry'
    alink['url'] = base_url+'926880.txt?_=1586339778910'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'materials-sciences'
    alink['url'] = base_url+'936993.txt?_=1586340275333'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'life-sciences-medicine'
    alink['url'] = base_url+'940526.txt?_=1586342483464'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'life-sciences-medicine'
    alink['url'] = base_url+'940526.txt?_=1586342483464'
    links.append(alink)

    alink = dict()
    alink['sub'] = 'engineering-chemical'
    alink['url'] = base_url+'930696.txt?_=1586342561890'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'mathematics'
    alink['url'] = base_url+'933825.txt?_=1586342751948'
    links.append(alink)
    alink = dict()
    alink['sub'] = 'physics-astronomy'
    alink['url'] = base_url+'939008.txt?_=1586342805434'
    links.append(alink)

    return links

    

def get_data():
    links= generate_links()
    print(len(links))
    for link in links:
        resp = requests.get(link['url'])
        print(resp.status_code)
        print(len(resp.json()['data']))
    #resp = requests.get(url)

    #print(resp.status_code)

    #jre = resp.json()

#print(jre.keys())
#print(type(jre['data']))

def get_data_in_physics_subj():
    links= generate_links()
    for link in links:
        if link['sub'] == 'physics-astronomy':
            resp = requests.get(link['url'])
            print(resp.status_code)
            print(len(resp.json()['data']))
            return resp.json()['data']


if __name__ == '__main__':
    data = get_data_in_physics_subj()
    for it in data:
        if 'Iran' in it['country']:
            for k, v in it.items():
                print("%s: %s" %(k,v))
