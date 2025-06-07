#!/usr/bin/env python3
"""This module manages api authentication."""
import re
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Class definition for api authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines whether authentication is required for
        a given path.

        Returns:
          - True if path is None
          - True if excluded_paths is None or empty
          - False if path matches (with or without trailing slash) any in
          excluded_paths
        """
        if path is not None and excluded_paths is not None:
            for excluded_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if excluded_path[-1] == '*':
                    pattern = f"{excluded_path[0:-1]}.*"
                elif excluded_path[-1] == '/':
                    pattern = f"{excluded_path[0:-1]}/*"
                else:
                    pattern = f"{excluded_path}/*"
                # Use Regular Expression to match pattern
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Handles authorized request header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from request"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from request."""
        if request is None:
            return None

        # Set my_session_id through env var, SESSION_NAME
        SESSION_NAME = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(SESSION_NAME, None)
