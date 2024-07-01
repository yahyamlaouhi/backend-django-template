"""
Django Command to wait for the database to be available
"""

import time
from typing import Any

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Waiting for database....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Available"))


# Is This a Unit Test or Integration Test?

# This is a unit test. Here's why:

# Focus on Isolation: The test isolates the wait_for_db command from actual database interactions by mocking the check method. It doesn't require the actual database to be up or accessible.
# Mocking Dependencies: By using patch, the test controls and verifies how check is used, rather than relying on the real implementation of the database connection check.
