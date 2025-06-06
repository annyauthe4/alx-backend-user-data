#!/usr/bin/env python3
"""
This module has a class which inherits from Auth and has a new
authentication mechanism - Session authentication.
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Defines the session authentication mechanism."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id

        Args:
            user_id (str): ID of the current user.

        Returns:
            A Session ID string.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves a user id based on session id

        Args:
            session_id (str): A session id

        Returns:
            A user id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.__class__.user_id_by_session_id.get(
            session_id
        )

    def current_user(self, request=None):
        """Return user instance based on cookie value"""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        # Get user id
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Get user using id
        return User.get(user_id)
