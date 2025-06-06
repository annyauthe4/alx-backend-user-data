#!/usr/bin/env python3
"""Contains a basic authentication class that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from flask import request
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Returns user email and password from base64 decoded
        value.

        Args:
            decoded_base64_authorization_header (str):
            Function to decode base64 value.

        Returns:
            str: User email
            str: User paswword
        """
        d_b_auth_h = decoded_base64_authorization_header
        if d_b_auth_h is None or not isinstance(d_b_auth_h, str):
            return None, None

        # Check if d_b_auth_h contains ":" character
        if ":" not in d_b_auth_h:
            return None, None
        email, username = d_b_auth_h.strip().split(':', 1)
        return email, username

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the instance of User.

        Args:
            user_email (str): The email of the user.
            user_pwd (str): The user password.

        Returns:
            obj: The instance of the user.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Check user in database using email and password
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        # Validate users returned
        if not users or len(users) == 0:
            return None

        # Use the first instance of users returned
        user = users[0]
        # Check password
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance foa a request."""

        # Get authentication header
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Extract base64 authorization header
        b_auth_h = self.extract_base64_authorization_header(
            auth_header
        )
        if b_auth_h is None:
            return None

        # Decode the base64 authorization header extracted
        decoded_h = self.decode_base64_authorization_header(
            b_auth_h
        )
        if decoded_h is None:
            return None

        # Extract user credentials from the decoded header
        credentials = self.extract_user_credentials(
            decoded_h
        )
        if credentials is None:
            return None
        # Extract user email and password from credentials
        user_email, user_pwd = credentials

        # Retrieve user using email and password
        user = self.user_object_from_credentials(
            user_email, user_pwd
        )
        if user is None:
            return None
        return user
