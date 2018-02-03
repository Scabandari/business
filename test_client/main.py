from request_for_quote_pb2 import RFQ_pb, RFP_pb
from request_for_quote_pb2 import Client_pb, Product_pb, Category_pb
import request_for_quote_pb2
import requests
import json

if __name__ == '__main__':

    local_host = 'http://127.0.0.1:8000/'
    api_endpoint_json = local_host + 'api/RFQ/'
    # code section demonstrates the web apps' JSON rest framework

    # this is my JSON for testing the rest framework
    rfq_data = {
        "quantity": 2000,
        "account_id": 1,  # Client's pk
        "product_number": 2, # Product's pk
        "product_category": 1  # Category's pk
    }

    get_response = requests.get(api_endpoint_json)
    print("Get request's status code: ", get_response.status_code)
    print("Get request get's all previous RFQ's")
    print(get_response.json())

    # Post should accept a RFQ and give back a RFP
    post_response = requests.post(url=api_endpoint_json,
                             data=rfq_data,)

    print("The POST response's status code: ", post_response.status_code)
    print("\n\n\n\n", "The POST (json) response including the response for price")
    print(post_response.json())

    get_new_response = requests.get('http://127.0.0.1:8000/api/RFQ/')
    print("After the previous POST request, GET requests now returns a list"
          " with a new RFQ")
    print(get_new_response.json())

    # this code section demonstrates the protobuf REST rest functionality
    headers = {
        'Content-Type': 'application-octet-stream',
    }

    api_endpoint_pb = local_host + 'api/RFQ/pb/'

    ### now try to POST
    category = Category_pb()
    category.name = 'sports'
    product = Product_pb(category=category)
    product.name = 'hockey stick'
    product.price = 110
    product.product_number = 1

    client = Client_pb()
    client.business_name = "Canadian Tire"
    rfq_pb = request_for_quote_pb2.RFQ_pb(account_id=client,
                                          quantity=300,
                                          product_number=product,
                                          product_category=category)

    rfq_pb = rfq_pb.SerializeToString()

    rfq_post = requests.post(url=api_endpoint_pb,
                             data=rfq_pb,
                             headers=headers)
    #rfp_pb = RFP_pb()
    #rfp_pb = RFP_pb.ParseFromString(rfq_post)
    print("\n\n\n\n")
    print("After sending a POST request with protobuf instead of JSON, the "
          "resulting response's status code is: ",  rfq_post.status_code)

    print('The resulting RFP in parsed from the protobuf object is: ' )
    print(rfq_post.content)

