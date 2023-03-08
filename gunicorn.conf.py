bind = '0.0.0.0:8080'
workers = 1
accesslog = '-'

import ssl
from custom_auth_worker import CustomSyncWorker

# mTLS configuration with TLSv1.2 and requiring and validating client
# certificates
ssl_version = 5 # ssl.PROTOCOL_TLSv1_2
cert_reqs = ssl.CERT_REQUIRED
#ciphers = 'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256'
ca_certs = '/certs/ca.crt'
certfile = '/certs/server.crt'
keyfile = '/certs/server.key'
do_handshake_on_connect = True

worker_class = 'custom_auth_worker.CustomSyncWorker'
