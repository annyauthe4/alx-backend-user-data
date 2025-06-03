#!/usr/bin/env python3
"""Contains a basic authentication class that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64
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
