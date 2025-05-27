#!/usr/bin/env pyhon3
"""This module manages api authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class definition for api authentication."""
    def __init__(self):
        """Initialization of class object"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that handles api path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Handles authorized request header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Checks current user"""
        return request
