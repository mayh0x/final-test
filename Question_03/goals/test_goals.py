import json
import os
import requests
from nose.tools import *
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)

from main_functions import *

class TestGoals(unittest.TestCase):
    
    def test_get_goals(self):
        header = {'Authorization': get_authorization_token(self)}
        ID = get_company_id(self, header)

        response = requests.get(f'{URL}/dashboard/goals/{ID}', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        assert_in('breakevenPoint', json_data)
        assert_equal(type(json_data['breakevenPoint']), float)
        assert_equal(json_data['breakevenPoint'], 0)

        assert_in('salesGoal', json_data)
        assert_equal(type(json_data['salesGoal']), float)
        assert_equal(json_data['salesGoal'], 0)

        assert_in('totalTaxForSale', json_data)
        assert_equal(type(json_data['totalTaxForSale']), float)
        assert_equal(json_data['totalTaxForSale'], 0)

        assert_in('unitBP', json_data)
        assert_equal(type(json_data['unitBP']), float)
        assert_equal(json_data['unitBP'], 0)

        assert_in('unitSG', json_data)
        assert_equal(type(json_data['unitSG']), float)
        assert_equal(json_data['unitSG'], 0)