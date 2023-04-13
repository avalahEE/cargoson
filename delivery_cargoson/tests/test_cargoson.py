from odoo.tests import tagged, TransactionCase
from odoo.addons.delivery_cargoson.models.schema import AvailablePrices # noqa

import logging
logger = logging.getLogger(__name__)


@tagged('cargoson', 'post_install', '-at_install')
class TestPayslipBase(TransactionCase):
    def test_cargoson_available_prices(self):
        data: AvailablePrices = AvailablePrices.from_dict({
          "status": 200,
          "object": {
            "prices": [
              {
                "carrier": "DSV Estonia AS",
                "reg_no": "10342368",
                "id": 3,
                "service": "Main",
                "service_id": 85,
                "price": "19.13",
                "unit": "payable_weight",
                "type": "price_list"
              },
              {
                "carrier": "DSV Estonia AS",
                "reg_no": "10342368",
                "id": 3,
                "service": "Express Service",
                "service_id": 123,
                "price": "32.50",
                "unit": "real_weight",
                "type": "online"
              },
              {
                "carrier": "DPD Eesti AS",
                "reg_no": "10092256",
                "id": 10,
                "service": "Main",
                "service_id": 555,
                "price": "20.00",
                "unit": "payable_weight",
                "type": "price_list"
              }
            ]
          }
        })
        self.assertEqual(data.status, 200)
        self.assertEqual(len(data.object.prices), 3)
        self.assertEqual(data.object.prices[0].carrier, 'DSV Estonia AS')
        self.assertEqual(data.object.prices[1].carrier, 'DSV Estonia AS')
        self.assertEqual(data.object.prices[2].carrier, 'DPD Eesti AS')
