#!/usr/bin/env python3
"""Contains a basic authentication class that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from flask import request


class BasicAuth(Auth):
    """Inherits from Auth class"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Returns base64 part of the authorization header."""
        auth_header = authorization_header
        if auth_header is None or not isinstance(auth_header, str):
            return None

        if not auth_header.startswith('Basic '):
            return None
        else:
            return auth_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Returns the decoded value of a Base64 string.

        Args:
            base64_authorization_header (str):
            The Base64 string to decode.

        Returns:
            str: The decoded UTF-8 string or None if invalid.
        """
        b_auth_h = base64_authorization_header
        if b_auth_h is None or not isinstance(b_auth_h, str):
            return None

        try:
            decoded = base64.b64decode(b_auth_h).decode('utf-8')
            return decoded
        except (binascii.Error, UnicodeDecodeError):
            return None
