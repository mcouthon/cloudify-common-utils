from base64 import urlsafe_b64encode

from .constants import BASIC_AUTH_PREFIX, AUTH_HEADER


def get_auth_header(username, password):
    header = {}

    if username and password:
        credentials = '{0}:{1}'.format(username, password)
        encoded_credentials = urlsafe_b64encode(credentials)
        header = {AUTH_HEADER: BASIC_AUTH_PREFIX + ' ' + encoded_credentials}

    return header
