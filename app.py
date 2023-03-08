import re
#import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ssl_cn():
    print("Root method")
    ssl_client_dn_cn = request.environ.get('SSL_CLIENT_S_DN_CN')
    if ssl_client_dn_cn is not None:
        return f"SSL CN: {ssl_client_dn_cn}"
    else:
        return "No SSL CN found in client certificate."

'''
def grant_client_access(headers):
    """
    We need to check for:
     * 'Ssl-Client-Verify' = 'SUCCESS'
     * 'Ssl-Client' = 'CN=x.d.wott.local,O=Web of Trusted Things\\, Ltd,ST=London,C=UK')
    """
    
    if not headers.get('Content-Type') == 'application/json':
        print(headers)
        print(headers.get('Content-Type'))
        print("Content Type not found")
        return False
    else:
        print("Header found")


    if not headers.get('Ssl-Client-Verify') == 'SUCCESS':
        print("return here")
        return False

    whitelist = generate_whitelist()
    print('Device whitelist: {}'.format(whitelist))

    # Extract the Common Name from the certificate
    matchObj = re.match(
        r'.*CN=(.*.d.wott.local)',
        headers.get('Ssl-Client'),
        re.M | re.I
    )

    print('Got request from {}'.format(matchObj.group(1)))

    # Match the device against the whitelist
    if matchObj.group(1) in whitelist:
        print('{} found in whitelist'.format(matchObj.group(1)))
        return True

    return False

@app.route('/')
def index():
    print(request.headers.get('Ssl-Client'))
    print(request.url)
    if grant_client_access(request.headers):
        return 'Access granted!\n'
    else:
        return 'Access denied!\n'
'''
