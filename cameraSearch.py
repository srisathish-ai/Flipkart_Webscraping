import requests
def getCameraHTML(**kwargs):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.flipkart.com/',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
    }

    params = (
        ('q', 'camera'),
        ('otracker', 'search'),
        ('otracker1', 'search'),
        ('marketplace', 'FLIPKART'),
        ('as-show', 'on'),
        ('as', 'off'),
        ('as-pos', '1'),
        ('as-type', 'HISTORY'),
    )

    response = requests.get('https://www.flipkart.com/search', headers=headers, params=params)
    return response.text