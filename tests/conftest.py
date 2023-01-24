import os
from fastapi.testclient import TestClient
import pytest
from main import create_app, DATABASE_URL

CREATE_USER_QUERY = """
INSERT INTO users VALUES(%s, %s, %s) RETURNING user_id;
"""

CREATE_USER_QUERY_COMMON = """
INSERT INTO USERS (username, is_deleted) VALUES(%s, %s) RETURNING user_id;
"""

GET_USER_BY_ID_QUERY = """
SELECT * FROM users WHERE user_id = %s;
"""
