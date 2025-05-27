#!/usr/bin/env pyhon3
"""This module manages api authentication."""
from flask import request
from typing import List, TypeVar


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
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure trailing slash for comparison
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded in excluded_paths:
            if excluded == normalized_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Handles authorized request header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Checks current user"""
        return request
