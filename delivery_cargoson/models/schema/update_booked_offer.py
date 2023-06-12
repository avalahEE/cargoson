from typing import Optional


# noinspection PyPep8Naming
class UpdateBookedOffer(object):

    __total_amount: Optional[float] = None

    def __get_total_amount(self):
        return self.__total_amount

    def __set_total_amount(self, total_amount):
        if not (isinstance(total_amount, float) or isinstance(total_amount, int) or total_amount is None):
            raise Exception(f'Cannot set field "total_amount" (type float) to {repr(total_amount)}')

        self.__total_amount = total_amount

    total_amount = property(__get_total_amount, __set_total_amount)
    """
    Updated total price of the shipment in a local currency units
    """

    __total_weight: Optional[float] = None

    def __get_total_weight(self):
        return self.__total_weight

    def __set_total_weight(self, total_weight):
        if not (isinstance(total_weight, float) or isinstance(total_weight, int) or total_weight is None):
            raise Exception(f'Cannot set field "total_weight" (type float) to {repr(total_weight)}')

        self.__total_weight = total_weight

    total_weight = property(__get_total_weight, __set_total_weight)
    """
    Updated total weight of the shipment in kilograms
    """

    # noinspection PyArgumentList
    def __init__(self, total_amount=None, total_weight=None):
        self.__set_total_amount(total_amount)
        self.__set_total_weight(total_weight)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['total_amount'] = d.get('total_amount')
        v['total_weight'] = d.get('total_weight')
        return UpdateBookedOffer(**v)

    def as_dict(self):
        res = dict()
        if self.__total_amount is not None:
            res['total_amount'] = self.__total_amount
        if self.__total_weight is not None:
            res['total_weight'] = self.__total_weight
        return res


