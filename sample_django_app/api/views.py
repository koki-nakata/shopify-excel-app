from django.http import JsonResponse
from shopify_app.decorators import session_token_required

import shopify

import json


@session_token_required
def products(request):
    print("c-1")
    products = shopify.Product.find()
    #GraphQL
    client = shopify.GraphQL()
    query = '''
        {
          products(first: 10, reverse: true) {
            edges {
              node {
                id
                title
                handle
                resourcePublicationOnCurrentPublication {
                  publication {
                    name
                    id
                  }
                  publishDate
                  isPublished
                }
              }
            }
          }
        }

    '''
    result = client.execute(query)
    data = json.loads(result)
    print("data",data["data"])
    return JsonResponse({'products': [p.to_dict() for p in products]})

@session_token_required
def orders(request):
    print("c-2")
    orders = shopify.Order.find(status='any')

    return JsonResponse({'orders': [o.to_dict() for o in orders]})
