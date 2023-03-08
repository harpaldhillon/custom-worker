from gunicorn.workers.sync import SyncWorker
import logging
from cryptography import x509
from cryptography.x509 import load_der_x509_certificate
from cryptography.x509.name import _NAME_TO_NAMEOID
from cryptography.x509.oid import NameOID
logging.basicConfig(level=logging.DEBUG)

def _check_cert(a, b, c, d):
    return True

class CustomSyncWorker(SyncWorker):
    def handle_request(self, listener, req, client, addr):
        # Log some messages
        logging.debug('handle request starting')
        client_cert = client.getpeercert(binary_form=True)
        if not client_cert:
            return headers

        cert = load_der_x509_certificate(client_cert)
        print("HARPALAAAAAAAAAAAAA")
        headers = dict(req.headers)
        headers['ISSUER-COMMON-NAME'] = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
        headers['REQUESTER_DN'] = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
        print(cert.subject.rfc4514_string())

        print(f'headers: {headers}')
        print(dict(client.getpeercert()))
        subject = dict(client.getpeercert().get('subject')[0])
        print(subject)
        headers['X-USER'] = subject.get('commonName')
        print(headers)
        req.headers = list(headers.items())
        
        if not _check_cert(headers['ISSUER-COMMON-NAME'], headers['REQUESTER_DN'], 'my-ca', 'my-client'):
            logging.debug('X-USER-X1 is not foundddd')
            return

        super(CustomSyncWorker, self).handle_request(listener, req, client, addr)
