import requests
def getLaptopHTML(**kwargs):
    queries = []
    data = dict()
    for i in kwargs.items():
        data.update({i[0]:i[1]})
    print('data',data)

    if 'brand' in data:
        if data['brand'] != None:
            queries.append('facets.brand%5B%5D={}'.format(data['brand']))
    if 'lapprocessor' in data:
        if data['lapprocessor'] != 'All':
            queries.append('facets.processor%5B%5D={}'.format(data['lapprocessor']))


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
    print(queries)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.flipkart.com/',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
    }

    params = (
        ('q', 'laptops'),
        ('otracker', 'search'),
        ('otracker1', 'search'),
        ('marketplace', 'FLIPKART'),
        ('as-show', 'on'),
        ('as', 'off'),
        ('as-pos', '1'),
        ('as-type', 'HISTORY'),
        ('p[]', queries),
        ('sort', sort),
        #'facets.brand%5B%5D=HP'
        #'facets.processor%5B%5D=Core+i5']
    )

    response = requests.get('https://www.flipkart.com/search', headers=headers, params=params)
    return response.text