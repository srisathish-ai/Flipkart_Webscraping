import pandas as pd
import numpy as np
import json

def cameraSoupToDataframe(soup, ishome):
    products=[] 
    prices=[]
    ratings=[]
    reviews=[]
    pixels=[]
    zoom=[]
    links=[]
    for containers in soup.findAll('a',class_='_1fQZEK'):
        name=containers.find('div', attrs={'class':'_4rR01T'})
        price=containers.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=containers.find('div', attrs={'class':'_3LWZlK'})
        review = containers.find('span', {'class':'_2_R_DZ'})
        specification = containers.find('div', attrs={'class':'fMghEO'})
        for container in specification:
            spec=container.find_all('li', attrs={'class':'rgWa7D'})
            pixel = spec[0].text
            lens = spec[1].text
        link = "https://flipkart.com"+containers['href']
        if ishome:
            if len(products) < 6:
                products.append(name.text)
                ratings.append(float(rating.text)) if rating is not None  else ratings.append(float(0))
                prices.append(int(price.text.strip('₹').replace(',','')))
                reviews.append(review.text) if review is not None else reviews.append('0 ratings & 0 reviews')    
                pixels.append(pixel)
                zoom.append(lens)
                links.append(link)

        else:
            products.append(name.text)
            ratings.append(float(rating.text)) if rating is not None  else ratings.append(float(0))
            prices.append(int(price.text.strip('₹').replace(',','')))
            reviews.append(review.text) if review is not None else reviews.append('0 ratings & 0 reviews')    
            pixels.append(pixel)
            zoom.append(lens)
            links.append(link)
    df = pd.DataFrame({
        'Products' : products,
        'Prices' : prices,
        'Ratings' : ratings,
        'Reviews' : reviews,
        'Pixels' : pixels,
        'Zoom' : zoom,
        'Link' : links
        })
    result = df.to_json(orient='records')
    data=json.loads(result)
    return data