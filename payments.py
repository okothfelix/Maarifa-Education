import requests
from requests.auth import HTTPBasicAuth
import json
import secrets


# payment credentials
consumer_key = '2d7696ac-a10a-4873-8fd0-55dd6d61a6b4'
consumer_secret = 'ZQ8Keu59mtzAbac3OyvJEzn0'


def _access_token():
    endpoint = "https://api-v2.tanda.africa/accounts/v1/oauth/token"

    payload = {"grant_type": "client_credentials"}
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }
    r = requests.post(endpoint, data=payload, headers=headers, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return json.loads(r.text)['access_token']


def c2b_payments(agent, amount, phone_number):
    url = "https://api-v2.tanda.africa/io/v2/organizations/9324d7b8-9f61-4333-8e5b-57fd82aa3389/requests"
    payload = {
        "commandId": "CustomerPayment",
        "serviceProviderId": agent,
        "reference": "ref" + secrets.token_hex(12),
        "requestParameters": [
            {
                "id": "amount",
                "value": str(amount),
                "label": "Amount"
            },
            {
                "id": "accountNumber",
                "value": phone_number,
                "label": "A/c"
            }
        ],
        "referenceParameters": [
            {
                "id": "resultUrl",
                "value": "https://onespacemall.co.ke/order-callback-section",
                "label": "Ref"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer %s" % _access_token()
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response, 67)


def b2c_section(agent, amount, phone_number):
    url = "https://api-v2.tanda.africa/io/v2/organizations/9324d7b8-9f61-4333-8e5b-57fd82aa3389/requests"

    payload = {
        "commandId": "MerchantToMobilePayment",
        "serviceProviderId": agent,
        "reference": "ref" + secrets.token_hex(12),
        "requestParameters": [
            {
                "id": "merchantWallet",
                "value": "123456",
                "label": "Sub wallet"
            },
            {
                "id": "amount",
                "value": str(amount),
                "label": "Amt"
            },
            {
                "id": "accountNumber",
                "value": phone_number[1:],
                "label": "A/c"
            }
        ],
        "referenceParameters": [
            {
                "id": "resultUrl",
                "value": "https://onespacemall.co.ke/b2c/callback",
                "label": "Hook"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer %s" % _access_token()
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response.text)

