from typing import Optional


# noinspection PyPep8Naming
class ParcelMachines(object):
    """
    A parcel machine object detailing information about the parcel machine, such as its name, location, references and info about its carrier
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
    The numeric ID of this parcel machine
    """

    __reference: Optional[str] = None

    def __get_reference(self):
        return self.__reference

    def __set_reference(self, reference):
        if not (isinstance(reference, str) or reference is None):
            raise Exception(f'Cannot set field "reference" (type str) to {repr(reference)}')

        self.__reference = reference

    reference = property(__get_reference, __set_reference)
    """
    The reference of this parcel machine (as referenced to by the carrier)
    """

    __name: Optional[str] = None

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        if not (isinstance(name, str) or name is None):
            raise Exception(f'Cannot set field "name" (type str) to {repr(name)}')

        self.__name = name

    name = property(__get_name, __set_name)
    """
    The name of this parcel machine
    """

    __carrier_name: Optional[str] = None

    def __get_carrier_name(self):
        return self.__carrier_name

    def __set_carrier_name(self, carrier_name):
        if not (isinstance(carrier_name, str) or carrier_name is None):
            raise Exception(f'Cannot set field "carrier_name" (type str) to {repr(carrier_name)}')

        self.__carrier_name = carrier_name

    carrier_name = property(__get_carrier_name, __set_carrier_name)
    """
    The name of the carrier of this parcel machine
    """

    __carrier_id: Optional[int] = None

    def __get_carrier_id(self):
        return self.__carrier_id

    def __set_carrier_id(self, carrier_id):
        if not (isinstance(carrier_id, int) or carrier_id is None):
            raise Exception(f'Cannot set field "carrier_id" (type int) to {repr(carrier_id)}')

        self.__carrier_id = carrier_id

    carrier_id = property(__get_carrier_id, __set_carrier_id)
    """
    The numeric ID of the carrier of this parcel machine
    """

    __carrier_reg_no: Optional[str] = None

    def __get_carrier_reg_no(self):
        return self.__carrier_reg_no

    def __set_carrier_reg_no(self, carrier_reg_no):
        if not (isinstance(carrier_reg_no, str) or carrier_reg_no is None):
            raise Exception(f'Cannot set field "carrier_reg_no" (type str) to {repr(carrier_reg_no)}')

        self.__carrier_reg_no = carrier_reg_no

    carrier_reg_no = property(__get_carrier_reg_no, __set_carrier_reg_no)
    """
    The business registration number of the carrier of this parcel machine
    """

    __address_row_1: Optional[str] = None

    def __get_address_row_1(self):
        return self.__address_row_1

    def __set_address_row_1(self, address_row_1):
        if not (isinstance(address_row_1, str) or address_row_1 is None):
            raise Exception(f'Cannot set field "address_row_1" (type str) to {repr(address_row_1)}')

        self.__address_row_1 = address_row_1

    address_row_1 = property(__get_address_row_1, __set_address_row_1)
    """
    The street address of this parcel machine
    """

    __city: Optional[str] = None

    def __get_city(self):
        return self.__city

    def __set_city(self, city):
        if not (isinstance(city, str) or city is None):
            raise Exception(f'Cannot set field "city" (type str) to {repr(city)}')

        self.__city = city

    city = property(__get_city, __set_city)
    """
    The name of the city of this parcel machine
    """

    __postcode: Optional[str] = None

    def __get_postcode(self):
        return self.__postcode

    def __set_postcode(self, postcode):
        if not (isinstance(postcode, str) or postcode is None):
            raise Exception(f'Cannot set field "postcode" (type str) to {repr(postcode)}')

        self.__postcode = postcode

    postcode = property(__get_postcode, __set_postcode)
    """
    The postcode of this parcel machine
    """

    __country: Optional[str] = None

    def __get_country(self):
        return self.__country

    def __set_country(self, country):
        if not (isinstance(country, str) or country is None):
            raise Exception(f'Cannot set field "country" (type str) to {repr(country)}')

        self.__country = country

    country = property(__get_country, __set_country)
    """
    The two-letter country code (ISO 3166-1 alpha-2) of this parcel machine
    """

    # noinspection PyArgumentList
    def __init__(self, id=None, reference=None, name=None, carrier_name=None, carrier_id=None, carrier_reg_no=None, address_row_1=None, city=None, postcode=None, country=None):
        self.__set_id(id)
        self.__set_reference(reference)
        self.__set_name(name)
        self.__set_carrier_name(carrier_name)
        self.__set_carrier_id(carrier_id)
        self.__set_carrier_reg_no(carrier_reg_no)
        self.__set_address_row_1(address_row_1)
        self.__set_city(city)
        self.__set_postcode(postcode)
        self.__set_country(country)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['id'] = d.get('id')
        v['reference'] = d.get('reference')
        v['name'] = d.get('name')
        v['carrier_name'] = d.get('carrier_name')
        v['carrier_id'] = d.get('carrier_id')
        v['carrier_reg_no'] = d.get('carrier_reg_no')
        v['address_row_1'] = d.get('address_row_1')
        v['city'] = d.get('city')
        v['postcode'] = d.get('postcode')
        v['country'] = d.get('country')
        return ParcelMachines(**v)

    def as_dict(self):
        res = dict()
        if self.__id is not None:
            res['id'] = self.__id
        if self.__reference is not None:
            res['reference'] = self.__reference
        if self.__name is not None:
            res['name'] = self.__name
        if self.__carrier_name is not None:
            res['carrier_name'] = self.__carrier_name
        if self.__carrier_id is not None:
            res['carrier_id'] = self.__carrier_id
        if self.__carrier_reg_no is not None:
            res['carrier_reg_no'] = self.__carrier_reg_no
        if self.__address_row_1 is not None:
            res['address_row_1'] = self.__address_row_1
        if self.__city is not None:
            res['city'] = self.__city
        if self.__postcode is not None:
            res['postcode'] = self.__postcode
        if self.__country is not None:
            res['country'] = self.__country
        return res


