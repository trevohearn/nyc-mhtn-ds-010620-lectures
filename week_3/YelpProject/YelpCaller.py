import config
from rauth import OAuth1Service
import requests
from YelpAPI import get_my_key

business_id=
api_key=get_my_key()
endpoint=config.credentials.BusinessSearch
headers={‘Authorization’:‘bearer %s’% API_KEY}
parameters={‘term’:‘pizza’,
              ‘location’:‘New York City ’}


businessEndpoint = 'https://api.yelp.com/v3/businesses/search'
reviewEndpoint = 'GET https://api.yelp.com/v3/businesses/{id}/reviews'

#import requests
def businessCallGET(args):
    businessEndpoint = 'https://api.yelp.com/v3/businesses/search'
    return requests.get(businessEndpoint, params=args).content

#import requests
def reviewCallGET(id, args):
    reviewEndpoint = 'https://api.yelp.com/v3/businesses/{id}/reviews'
    return requests.get(reviewEndpoint, params=args).content
