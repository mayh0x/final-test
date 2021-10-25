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

class TestFinancialStrategy(unittest.TestCase):
    
    def test_get_financial_strategy(self):
        header = {'Authorization': get_authorization_token(self)}
        ID = get_company_id(self, header)

        response = requests.get(f'{URL}/financial-strategy/{ID}', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        assert_in('salePrice', json_data)
        sale = json_data['salePrice']

        assert_in('id', sale)
        assert_equal(type(sale['id']), int)
        assert_equal(sale['id'], 1851)

        assert_in('company', sale)
        company = sale['company']

        assert_in('id', company)
        assert_equal(type(company['id']), int)
        assert_equal(company['id'], 1566)

        assert_in('fixedCost', json_data)
        cost = json_data['fixedCost']

        assert_in('office_supplies', cost)
        assert_equal(type(cost['office_supplies']), float)
        assert_equal(cost['office_supplies'], 0)


        assert_in('formulas', json_data)
        formulas = json_data['formulas']

        assert_in('sumOfRentFixedCosts', formulas)
        assert_equal(type(formulas['sumOfRentFixedCosts']), float)
        assert_equal(formulas['sumOfRentFixedCosts'], 0)

        assert_in('sumSalaryFixedCosts', formulas)
        assert_equal(type(formulas['sumSalaryFixedCosts']), float)
        assert_equal(formulas['sumSalaryFixedCosts'], 0)

        assert_in('sumOfSocialChargesFixedCosts', formulas)
        assert_equal(type(formulas['sumOfSocialChargesFixedCosts']), float)
        assert_equal(formulas['sumOfSocialChargesFixedCosts'], 0)

        assert_in('otherFixedCosts', formulas)
        assert_equal(type(formulas['otherFixedCosts']), float)
        assert_equal(formulas['otherFixedCosts'], 0)

        assert_in('sumCommission', formulas)
        assert_equal(type(formulas['sumCommission']), float)
        assert_equal(formulas['sumCommission'], 0)

        assert_in('sumCommissionCharges', formulas)
        assert_equal(type(formulas['sumCommissionCharges']), float)
        assert_equal(formulas['sumCommissionCharges'], 0)

        assert_in('sumTaxForSale', formulas)
        assert_equal(type(formulas['sumTaxForSale']), float)
        assert_equal(formulas['sumTaxForSale'], 0)

        assert_in('otherVariableCosts', formulas)
        assert_equal(type(formulas['otherVariableCosts']), float)
        assert_equal(formulas['otherVariableCosts'], 0)

        assert_in('contribution', formulas)
        assert_equal(type(formulas['contribution']), float)
        assert_equal(formulas['contribution'], 0)

        assert_in('balance', formulas)
        assert_equal(type(formulas['balance']), float)
        assert_equal(formulas['balance'], 0)

        assert_in('balanceNetProfit', formulas)
        assert_equal(type(formulas['balanceNetProfit']), float)
        assert_equal(formulas['balanceNetProfit'], 0)

        assert_in('profit', formulas)
        assert_equal(type(formulas['profit']), float)
        assert_equal(formulas['profit'], 0)

        assert_in('unitsToProduce', formulas)
        assert_equal(type(formulas['unitsToProduce']), float)
        assert_equal(formulas['unitsToProduce'], 0)

        
        assert_in('verifySalesGoalAndBreakevenPoint', json_data)
        assert_equal(type(json_data['verifySalesGoalAndBreakevenPoint']), bool)
        assert_equal(json_data['verifySalesGoalAndBreakevenPoint'], False)

        assert_in('hasActionsPermission', json_data)
        assert_equal(type(json_data['hasActionsPermission']), bool)
        assert_equal(json_data['hasActionsPermission'], True)

        