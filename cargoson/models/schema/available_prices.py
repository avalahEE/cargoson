from typing import List
from typing import Optional
import enum


# noinspection PyPep8Naming
class AvailablePricesObjectPricesItemType(enum.Enum):
    """
    The source of this price
    """

    PRICE_LIST = 'price_list'
    ONLINE = 'online'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return AvailablePricesObjectPricesItemType(value)


# noinspection PyPep8Naming
class AvailablePricesObjectPricesItemUnit(enum.Enum):
    """
    The measurement unit by which the price was calculated
    """

    PAYABLE_WEIGHT = 'payable_weight'
    REAL_WEIGHT = 'real_weight'
    PARCEL = 'parcel'
    EUR_PLL = 'eur_pll'
    FIN_PLL = 'fin_pll'
    XL_PLL = 'xl_pll'
    HALF_PLL = 'half_pll'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return AvailablePricesObjectPricesItemUnit(value)


# noinspection PyPep8Naming
class AvailablePricesObjectPricesItem(object):

    __carrier: Optional[str] = None

    def __get_carrier(self):
        return self.__carrier

    def __set_carrier(self, carrier):
        if not (isinstance(carrier, str) or carrier is None):
            raise Exception(f'Cannot set field "carrier" (type str) to {repr(carrier)}')

        self.__carrier = carrier

    carrier = property(__get_carrier, __set_carrier)
    """
    The name of the carrier from which the price is from
    """

    __id: Optional[int] = None

    def __get_id(self):
        return self.__id

    def __set_id(self, id):
        if not (isinstance(id, int) or id is None):
            raise Exception(f'Cannot set field "id" (type int) to {repr(id)}')

        self.__id = id

    id = property(__get_id, __set_id)
    """
    The numeric ID of the carrier for more reliable identification
    """

    __reg_no: Optional[str] = None

    def __get_reg_no(self):
        return self.__reg_no

    def __set_reg_no(self, reg_no):
        if not (isinstance(reg_no, str) or reg_no is None):
            raise Exception(f'Cannot set field "reg_no" (type str) to {repr(reg_no)}')

        self.__reg_no = reg_no

    reg_no = property(__get_reg_no, __set_reg_no)
    """
    The business registration number of the carrier
    """

    __service: Optional[str] = None

    def __get_service(self):
        return self.__service

    def __set_service(self, service):
        if not (isinstance(service, str) or service is None):
            raise Exception(f'Cannot set field "service" (type str) to {repr(service)}')

        self.__service = service

    service = property(__get_service, __set_service)
    """
    The name of the carrier service that the price is related to. One carrier can have multiple prices if they have multiple services defined
    """

    __service_id: Optional[int] = None

    def __get_service_id(self):
        return self.__service_id

    def __set_service_id(self, service_id):
        if not (isinstance(service_id, int) or service_id is None):
            raise Exception(f'Cannot set field "service_id" (type int) to {repr(service_id)}')

        self.__service_id = service_id

    service_id = property(__get_service_id, __set_service_id)
    """
    The numeric ID of the carrier service for more reliable identification
    """

    __price: Optional[str] = None

    def __get_price(self):
        return self.__price

    def __set_price(self, price):
        if not (isinstance(price, str) or price is None):
            raise Exception(f'Cannot set field "price" (type str) to {repr(price)}')

        self.__price = price

    price = property(__get_price, __set_price)
    """
    The price for the requested shipment related to this carrier and service. The price is a float rounded to two decimal places, represented as a string
    """

    __unit: Optional[AvailablePricesObjectPricesItemUnit] = None

    def __get_unit(self):
        return self.__unit

    def __set_unit(self, unit):
        if not (unit in ['payable_weight', 'real_weight', 'parcel', 'eur_pll', 'fin_pll', 'xl_pll', 'half_pll'] or unit is None):
            raise Exception(f'Cannot set field AvailablePricesObjectPricesItemUnit.unit to {repr(unit)}')

        self.__unit = unit

    unit = property(__get_unit, __set_unit)
    """
    The measurement unit by which the price was calculated
    """

    __type: Optional[AvailablePricesObjectPricesItemType] = None

    def __get_type(self):
        return self.__type

    def __set_type(self, type):
        if not (type in ['price_list', 'online'] or type is None):
            raise Exception(f'Cannot set field AvailablePricesObjectPricesItemType.type to {repr(type)}')

        self.__type = type

    type = property(__get_type, __set_type)
    """
    The source of this price
    """

    # noinspection PyArgumentList
    def __init__(self, carrier=None, id=None, reg_no=None, service=None, service_id=None, price=None, unit=None, type=None):
        self.__set_carrier(carrier)
        self.__set_id(id)
        self.__set_reg_no(reg_no)
        self.__set_service(service)
        self.__set_service_id(service_id)
        self.__set_price(price)
        self.__set_unit(unit)
        self.__set_type(type)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['carrier'] = d.get('carrier')
        v['id'] = d.get('id')
        v['reg_no'] = d.get('reg_no')
        v['service'] = d.get('service')
        v['service_id'] = d.get('service_id')
        v['price'] = d.get('price')
        v['unit'] = d.get('unit')
        v['type'] = d.get('type')
        return AvailablePricesObjectPricesItem(**v)

    def as_dict(self):
        return dict(
            carrier=self.__carrier,
            id=self.__id,
            reg_no=self.__reg_no,
            service=self.__service,
            service_id=self.__service_id,
            price=self.__price,
            unit=self.__unit,
            type=self.__type
        )


# noinspection PyPep8Naming
class AvailablePricesObject(object):
    """
    The object containing the prices array
    """

    __prices: Optional[List["AvailablePricesObjectPricesItem"]] = []

    def __get_prices(self):
        return self.__prices

    def __set_prices(self, prices):
        if not (isinstance(prices, list) or prices is None):
            raise Exception(f'Cannot set field List["AvailablePricesObjectPricesItem"].prices to {repr(prices)}')

        self.__prices = prices

    prices = property(__get_prices, __set_prices)

    # noinspection PyArgumentList
    def __init__(self, prices=None):
        self.__set_prices(prices)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['prices'] = [AvailablePricesObjectPricesItem.from_dict(item) for item in d.get('prices')]
        return AvailablePricesObject(**v)

    def as_dict(self):
        return dict(
            prices=[item.as_dict() for item in self.__prices] if self.__prices is not None else None
        )


# noinspection PyPep8Naming
class AvailablePrices(object):

    __status: Optional[int] = None

    def __get_status(self):
        return self.__status

    def __set_status(self, status):
        if not (isinstance(status, int) or status is None):
            raise Exception(f'Cannot set field "status" (type int) to {repr(status)}')

        self.__status = status

    status = property(__get_status, __set_status)
    """
    Status code
    """

    __object: Optional[AvailablePricesObject] = None

    def __get_object(self):
        return self.__object

    def __set_object(self, object):
        if not (isinstance(object, AvailablePricesObject) or object is None):
            raise Exception(f'Cannot set field AvailablePricesObject.object to {repr(object)}')

        self.__object = object

    object = property(__get_object, __set_object)
    """
    The object containing the prices array
    """

    # noinspection PyArgumentList
    def __init__(self, status=None, object=None):
        self.__set_status(status)
        self.__set_object(object)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['status'] = d.get('status')
        v['object'] = AvailablePricesObject.from_dict(d.get('object'))
        return AvailablePrices(**v)

    def as_dict(self):
        return dict(
            status=self.__status,
            object=self.__object.as_dict() if self.__object is not None else None
        )


