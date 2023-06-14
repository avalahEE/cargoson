from typing import List
from typing import Optional
import enum


# noinspection PyPep8Naming
class AvailablePricesObjectPricesItemService_Type(enum.Enum):
    """
    Service type
    """

    NORMAL = 'normal'
    PARCEL_MACHINE = 'parcel_machine'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return AvailablePricesObjectPricesItemService_Type(value)


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
        if not (unit.as_dict() if hasattr(unit, "as_dict") else unit in ['payable_weight', 'real_weight', 'parcel', 'eur_pll', 'fin_pll', 'xl_pll', 'half_pll'] or unit is None):
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
        if not (type.as_dict() if hasattr(type, "as_dict") else type in ['price_list', 'online'] or type is None):
            raise Exception(f'Cannot set field AvailablePricesObjectPricesItemType.type to {repr(type)}')

        self.__type = type

    type = property(__get_type, __set_type)
    """
    The source of this price
    """

    __service_type: Optional[AvailablePricesObjectPricesItemService_Type] = None

    def __get_service_type(self):
        return self.__service_type

    def __set_service_type(self, service_type):
        if not (service_type.as_dict() if hasattr(service_type, "as_dict") else service_type in ['normal', 'parcel_machine'] or service_type is None):
            raise Exception(f'Cannot set field AvailablePricesObjectPricesItemService_Type.service_type to {repr(service_type)}')

        self.__service_type = service_type

    service_type = property(__get_service_type, __set_service_type)
    """
    Service type
    """

    __estimated_collection_date: Optional[str] = None

    def __get_estimated_collection_date(self):
        return self.__estimated_collection_date

    def __set_estimated_collection_date(self, estimated_collection_date):
        if not (isinstance(estimated_collection_date, str) or estimated_collection_date is None):
            raise Exception(f'Cannot set field "estimated_collection_date" (type str) to {repr(estimated_collection_date)}')

        self.__estimated_collection_date = estimated_collection_date

    estimated_collection_date = property(__get_estimated_collection_date, __set_estimated_collection_date)
    """
    Date of collection for shipment
    """

    __estimated_delivery_date: Optional[str] = None

    def __get_estimated_delivery_date(self):
        return self.__estimated_delivery_date

    def __set_estimated_delivery_date(self, estimated_delivery_date):
        if not (isinstance(estimated_delivery_date, str) or estimated_delivery_date is None):
            raise Exception(f'Cannot set field "estimated_delivery_date" (type str) to {repr(estimated_delivery_date)}')

        self.__estimated_delivery_date = estimated_delivery_date

    estimated_delivery_date = property(__get_estimated_delivery_date, __set_estimated_delivery_date)
    """
    Date of delivery for shipment, if present
    """

    __transit_time: Optional[str] = None

    def __get_transit_time(self):
        return self.__transit_time

    def __set_transit_time(self, transit_time):
        if not (isinstance(transit_time, str) or transit_time is None):
            raise Exception(f'Cannot set field "transit_time" (type str) to {repr(transit_time)}')

        self.__transit_time = transit_time

    transit_time = property(__get_transit_time, __set_transit_time)
    """
    Transit time
    """

    # noinspection PyArgumentList
    def __init__(self, carrier=None, id=None, reg_no=None, service=None, service_id=None, price=None, unit=None, type=None, service_type=None, estimated_collection_date=None, estimated_delivery_date=None, transit_time=None):
        self.__set_carrier(carrier)
        self.__set_id(id)
        self.__set_reg_no(reg_no)
        self.__set_service(service)
        self.__set_service_id(service_id)
        self.__set_price(price)
        self.__set_unit(unit)
        self.__set_type(type)
        self.__set_service_type(service_type)
        self.__set_estimated_collection_date(estimated_collection_date)
        self.__set_estimated_delivery_date(estimated_delivery_date)
        self.__set_transit_time(transit_time)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['carrier'] = d.get('carrier')
        v['id'] = d.get('id')
        v['reg_no'] = d.get('reg_no')
        v['service'] = d.get('service')
        v['service_id'] = d.get('service_id')
        v['price'] = d.get('price')
        v['unit'] = AvailablePricesObjectPricesItemUnit.from_dict(d.get('unit'))
        v['type'] = AvailablePricesObjectPricesItemType.from_dict(d.get('type'))
        v['service_type'] = AvailablePricesObjectPricesItemService_Type.from_dict(d.get('service_type'))
        v['estimated_collection_date'] = d.get('estimated_collection_date')
        v['estimated_delivery_date'] = d.get('estimated_delivery_date')
        v['transit_time'] = d.get('transit_time')
        return AvailablePricesObjectPricesItem(**v)

    def as_dict(self):
        res = dict()
        if self.__carrier is not None:
            res['carrier'] = self.__carrier
        if self.__id is not None:
            res['id'] = self.__id
        if self.__reg_no is not None:
            res['reg_no'] = self.__reg_no
        if self.__service is not None:
            res['service'] = self.__service
        if self.__service_id is not None:
            res['service_id'] = self.__service_id
        if self.__price is not None:
            res['price'] = self.__price
        if self.__unit is not None:
            res['unit'] = self.__unit.as_dict()
        if self.__type is not None:
            res['type'] = self.__type.as_dict()
        if self.__service_type is not None:
            res['service_type'] = self.__service_type.as_dict()
        if self.__estimated_collection_date is not None:
            res['estimated_collection_date'] = self.__estimated_collection_date
        if self.__estimated_delivery_date is not None:
            res['estimated_delivery_date'] = self.__estimated_delivery_date
        if self.__transit_time is not None:
            res['transit_time'] = self.__transit_time
        return res


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
        res = dict()
        if self.__prices is not None:
            res['prices'] = [item.as_dict() for item in self.__prices]
        return res


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
        res = dict()
        if self.__status is not None:
            res['status'] = self.__status
        if self.__object is not None:
            res['object'] = self.__object.as_dict()
        return res
