""" 
Test custom Django management command.
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Test commands. """
    
    def test_wait_database_db_ready(self, pathced_check):
        """ Test Waiting For Databases if Database Ready """
        pathced_check.return_value = True 
        
        call_command("wait_for_db")
        
        pathced_check.assert_called_once_with(database=['default'])
    
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, pathced_check):
        """ Test waiting for database when getting Operation Error """
        pathced_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
    
        call_command("wait_for_db")
        
        self.assertEqual(pathced_check.call_count, 6)
        
        pathced_check.assert_called_with(database=['default'])
        
        