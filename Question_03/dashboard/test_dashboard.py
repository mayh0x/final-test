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

class TestDashboard(unittest.TestCase):
    
    def test_get_dashboard(self):
        header = {'Authorization': get_authorization_token(self)}
        ID = get_company_id(self, header)

        response = requests.get(f'{URL}/dashboard/{ID}', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        assert_in('journeys', json_data)
        journeys = json_data['journeys']

        first = journeys[0]
        assert_in('id', first)
        assert_equal(type(first['id']), int)
        assert_equal(first['id'], 10576)

        assert_in('sort_order', first)
        assert_equal(type(first['sort_order']), int)
        assert_equal(first['sort_order'], 1)

        assert_in('current', first)
        assert_equal(type(first['current']), bool)
        assert_equal(first['current'], False)

        assert_in('open', first)
        assert_equal(type(first['open']), bool)
        assert_equal(first['open'], False)


        sec = journeys[1]
        assert_in('id', sec)
        assert_equal(type(sec['id']), int)
        assert_equal(sec['id'], 10577)

        assert_in('sort_order', sec)
        assert_equal(type(sec['sort_order']), int)
        assert_equal(sec['sort_order'], 2)

        assert_in('current', sec)
        assert_equal(type(sec['current']), bool)
        assert_equal(sec['current'], False)

        assert_in('open', sec)
        assert_equal(type(sec['open']), bool)
        assert_equal(sec['open'], False)


        third = journeys[2]
        assert_in('id', third)
        assert_equal(type(third['id']), int)
        assert_equal(third['id'], 10578)

        assert_in('sort_order', third)
        assert_equal(type(third['sort_order']), int)
        assert_equal(third['sort_order'], 3)

        assert_in('current', third)
        assert_equal(type(third['current']), bool)
        assert_equal(third['current'], False)

        assert_in('open', third)
        assert_equal(type(third['open']), bool)
        assert_equal(third['open'], False)


        assert_in('goals', json_data)
        goals = json_data['goals']

        assert_in('breakevenPoint', goals)
        assert_equal(type(goals['breakevenPoint']), float)
        assert_equal(goals['breakevenPoint'], 0)

        assert_in('salesGoal', goals)
        assert_equal(type(goals['salesGoal']), float)
        assert_equal(goals['salesGoal'], 0)

        assert_in('totalTaxForSale', goals)
        assert_equal(type(goals['totalTaxForSale']), float)
        assert_equal(goals['totalTaxForSale'], 0)

        assert_in('unitBP', goals)
        assert_equal(type(goals['unitBP']), float)
        assert_equal(goals['unitBP'], 0)

        assert_in('unitSG', goals)
        assert_equal(type(goals['unitSG']), float)
        assert_equal(goals['unitSG'], 0)


        assert_in('progress', json_data)
        progress = json_data['progress']

        assert_in('progressPlaning', progress)
        assert_equal(type(progress['progressPlaning']), float)
        assert_equal(progress['progressPlaning'], 0)

        assert_in('progressRH', progress)
        assert_equal(type(progress['progressRH']), float)
        assert_equal(progress['progressRH'], 0)

        assert_in('progressProduction', progress)
        assert_equal(type(progress['progressProduction']), int)
        assert_equal(progress['progressProduction'], 0)

        assert_in('progressMarketing', progress)
        assert_equal(type(progress['progressMarketing']), int)
        assert_equal(progress['progressMarketing'], 0)

        assert_in('progressFinancial', progress)
        assert_equal(type(progress['progressFinancial']), float)
        assert_equal(progress['progressFinancial'], 0)

        
        assert_in('saleDevolutionInfo', json_data)
        sale = json_data['saleDevolutionInfo']

        assert_in('retired', sale)
        assert_equal(type(sale['retired']), int)
        assert_equal(sale['retired'], 0)

        assert_in('stock', sale)
        assert_equal(type(sale['stock']), int)
        assert_equal(sale['stock'], 0)


        assert_in('totalProductsSelled', json_data)
        total = json_data['totalProductsSelled']
        assert_equal(type(total), float)
        assert_equal(total, 0)


        assert_in('percentAveragePresence', json_data)
        percent = json_data['percentAveragePresence']
        assert_equal(type(percent), float)
        assert_equal(percent, 0)


        assert_in('formulas', json_data)
        formulas = json_data['formulas']

        assert_in('actionsProfitability', formulas)
        assert_equal(type(formulas['actionsProfitability']), float)
        assert_equal(formulas['actionsProfitability'], 0)

        assert_in('totalShareCapital', formulas)
        assert_equal(type(formulas['totalShareCapital']), float)
        assert_equal(formulas['totalShareCapital'], 0)

        assert_in('productionGoal', formulas)
        assert_equal(type(formulas['productionGoal']), float)
        assert_equal(formulas['productionGoal'], 0)

        assert_in('saleGoal', formulas)
        assert_equal(type(formulas['saleGoal']), float)
        assert_equal(formulas['saleGoal'], 0)


        assert_in('dre1', json_data)
        dre1 = json_data['dre1']

        assert_in('provider', dre1)
        assert_equal(type(dre1['provider']), float)
        assert_equal(dre1['provider'], 0)

        assert_in('income', dre1)
        assert_equal(type(dre1['income']), float)
        assert_equal(dre1['income'], 0)

        assert_in('sales', dre1)
        assert_equal(type(dre1['sales']), float)
        assert_equal(dre1['sales'], 0)

        assert_in('rent', dre1)
        assert_equal(type(dre1['rent']), float)
        assert_equal(dre1['rent'], 0)

        assert_in('taxForSales', dre1)
        assert_equal(type(dre1['taxForSales']), float)
        assert_equal(dre1['taxForSales'], 0)

        assert_in('socialCompanyCharges', dre1)
        assert_equal(type(dre1['socialCompanyCharges']), float)
        assert_equal(dre1['socialCompanyCharges'], 0)

        assert_in('socialEmployeeCharges', dre1)
        assert_equal(type(dre1['socialEmployeeCharges']), float)
        assert_equal(dre1['socialEmployeeCharges'], 0)

        assert_in('comissions', dre1)
        assert_equal(type(dre1['comissions']), float)
        assert_equal(dre1['comissions'], 0)

        assert_in('netProfit', dre1)
        assert_equal(type(dre1['netProfit']), float)
        assert_equal(dre1['netProfit'], 0)

        assert_in('taxes', dre1)
        assert_equal(type(dre1['taxes']), float)
        assert_equal(dre1['taxes'], 0)

        assert_in('finalProfit', dre1)
        assert_equal(type(dre1['finalProfit']), float)
        assert_equal(dre1['finalProfit'], 0)


        assert_in('dre2', json_data)
        dre2 = json_data['dre2']

        assert_in('provider', dre2)
        assert_equal(type(dre2['provider']), float)
        assert_equal(dre2['provider'], 0)

        assert_in('income', dre2)
        assert_equal(type(dre2['income']), float)
        assert_equal(dre2['income'], 0)

        assert_in('sales', dre2)
        assert_equal(type(dre2['sales']), float)
        assert_equal(dre2['sales'], 0)

        assert_in('rent', dre2)
        assert_equal(type(dre2['rent']), float)
        assert_equal(dre2['rent'], 0)

        assert_in('taxForSales', dre2)
        assert_equal(type(dre2['taxForSales']), float)
        assert_equal(dre2['taxForSales'], 0)

        assert_in('socialCompanyCharges', dre2)
        assert_equal(type(dre2['socialCompanyCharges']), float)
        assert_equal(dre2['socialCompanyCharges'], 0)

        assert_in('socialEmployeeCharges', dre2)
        assert_equal(type(dre2['socialEmployeeCharges']), float)
        assert_equal(dre2['socialEmployeeCharges'], 0)

        assert_in('comissions', dre2)
        assert_equal(type(dre2['comissions']), float)
        assert_equal(dre2['comissions'], 0)

        assert_in('netProfit', dre2)
        assert_equal(type(dre2['netProfit']), float)
        assert_equal(dre2['netProfit'], 0)

        assert_in('taxes', dre2)
        assert_equal(type(dre2['taxes']), float)
        assert_equal(dre2['taxes'], 0)

        assert_in('finalProfit', dre2)
        assert_equal(type(dre2['finalProfit']), float)
        assert_equal(dre2['finalProfit'], 0)

