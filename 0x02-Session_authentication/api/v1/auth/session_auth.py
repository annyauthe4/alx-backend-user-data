#!/usr/bin/env python3
"""
This module has a class which inherits from Auth and has a new
authentication mechanism - Session authentication.
"""
from api.v1.auth.auth import Auth
import uuid


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
