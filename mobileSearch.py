import requests
def getMobileHTML(**kwargs):
    queries = ['facets.availability%5B%5D=Exclude+Out+of+Stock']
    
    data = dict()
    for i in kwargs.items():
        data.update({i[0]:i[1]})

    print(data)

    if 'brand' in data:
        if data['brand'] != None:
            queries.append('facets.brand%5B%5D={}'.format(data['brand']))

    if 'ram' in data:
        if data['ram'] != None:
            if data['brand'].lower() != 'apple':
                if int(data['ram']) <= 4:
                    queries.append('facets.ram%5B%5D={}+GB'.format(int(data['ram'])))
                elif int(data['ram']) == 6:
                    queries.append('facets.ram%5B%5D={}+GB+%26+Above'.format(int(data['ram'])))
                else:
                    queries.append('facets.ram%5B%5D=6+GB+%26+Above')


    if 'MinBudget' in data and 'MaxBudget' in data:
        queries.append('facets.price_range.from={}'.format(data['MinBudget']))
        queries.append('facets.price_range.to={}'.format(data['MaxBudget']))
    elif 'MinBudget' in data:
        queries.append('facets.price_range.from={}'.format(data['MinBudget']))
        queries.append('facets.price_range.to=Max')
    elif 'MaxBudget' in data:
        queries.append('facets.price_range.from=Min')
        queries.append('facets.price_range.to={}'.format(data['MaxBudget']))
    
    if 'sortBy' not in data:
        sort = 'relavance'
    else:
        sort = data['sortBy']

    print('queries -->',queries)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.flipkart.com/',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
    }

    params = (
        ('q', 'mobiles'),
        ('otracker', 'search'),
        ('otracker1', 'search'),
        ('marketplace', 'FLIPKART'),
        ('as-show', 'on'),
        ('as', 'off'),
        ('as-pos', '1'),
        ('as-type', 'HISTORY'),
        ('p[]', queries),
        ('sort', sort),
        #('page', '{}'.format(page)),
        #'facets.features%5B%5D=NFC'
        # facets.rating%5B%5D=4%E2%98%85+%26+above
        # facets.rating%5B%5D=3%E2%98%85+%26+above
    )

    response = requests.get('https://www.flipkart.com/search', headers=headers, params=params)
    return response.text