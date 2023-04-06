from typing import List
from typing import Optional
import enum


# noinspection PyPep8Naming
class PriceRequestShipmentRows_AttributesItemPackage_Type(enum.Enum):
    """
    Type of the package selected from the predefined package types
    """

    EUR = 'EUR'
    CTN = 'CTN'
    FIN = 'FIN'
    HPL = 'HPL'
    QPL = 'QPL'
    LOAD = 'LOAD'
    PLD = 'PLD'
    PXL = 'PXL'
    PLL = 'PLL'
    TBE = 'TBE'
    CLL = 'CLL'
    RLL = 'RLL'
    VALUE_20DC = '20DC'
    VALUE_40DC = '40DC'
    VALUE_40HC = '40HC'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return PriceRequestShipmentRows_AttributesItemPackage_Type(value)


# noinspection PyPep8Naming
class PriceRequestShipmentRows_AttributesItem(object):
    """
    Array of goods rows, with each row consisting of the following 7 (or less) key-value pairs
    """

    __quantity: Optional[int] = None

    def __get_quantity(self):
        return self.__quantity

    def __set_quantity(self, quantity):
        if not (isinstance(quantity, int) or quantity is None):
            raise Exception(f'Cannot set field "quantity" (type int) to {repr(quantity)}')

        self.__quantity = quantity

    quantity = property(__get_quantity, __set_quantity)
    """
    Number of packages
    """

    __package_type: Optional[PriceRequestShipmentRows_AttributesItemPackage_Type] = None

    def __get_package_type(self):
        return self.__package_type

    def __set_package_type(self, package_type):
        if not (package_type in ['EUR', 'CTN', 'FIN', 'HPL', 'QPL', 'LOAD', 'PLD', 'PXL', 'PLL', 'TBE', 'CLL', 'RLL', '20DC', '40DC', '40HC'] or package_type is None):
            raise Exception(f'Cannot set field PriceRequestShipmentRows_AttributesItemPackage_Type.package_type to {repr(package_type)}')

        self.__package_type = package_type

    package_type = property(__get_package_type, __set_package_type)
    """
    Type of the package selected from the predefined package types
    """

    __weight: Optional[int] = None

    def __get_weight(self):
        return self.__weight

    def __set_weight(self, weight):
        if not (isinstance(weight, int) or weight is None):
            raise Exception(f'Cannot set field "weight" (type int) to {repr(weight)}')

        self.__weight = weight

    weight = property(__get_weight, __set_weight)
    """
    Total weight in kilograms of the goods described in the row. If there are 5 EUR pallets, 100kg each, then the weight is 500 kg
    """

    __length: Optional[int] = None

    def __get_length(self):
        return self.__length

    def __set_length(self, length):
        if not (isinstance(length, int) or length is None):
            raise Exception(f'Cannot set field "length" (type int) to {repr(length)}')

        self.__length = length

    length = property(__get_length, __set_length)
    """
    Package length in cm
    """

    __width: Optional[int] = None

    def __get_width(self):
        return self.__width

    def __set_width(self, width):
        if not (isinstance(width, int) or width is None):
            raise Exception(f'Cannot set field "width" (type int) to {repr(width)}')

        self.__width = width

    width = property(__get_width, __set_width)
    """
    Package width in cm
    """

    __height: Optional[int] = None

    def __get_height(self):
        return self.__height

    def __set_height(self, height):
        if not (isinstance(height, int) or height is None):
            raise Exception(f'Cannot set field "height" (type int) to {repr(height)}')

        self.__height = height

    height = property(__get_height, __set_height)
    """
    Package height in cm
    """

    __cbm: Optional[float] = None

    def __get_cbm(self):
        return self.__cbm

    def __set_cbm(self, cbm):
        if not (isinstance(cbm, float) or isinstance(cbm, int) or cbm is None):
            raise Exception(f'Cannot set field "cbm" (type float) to {repr(cbm)}')

        self.__cbm = cbm

    cbm = property(__get_cbm, __set_cbm)
    """
    Row volume in cubic meters
    """

    __ldm: Optional[float] = None

    def __get_ldm(self):
        return self.__ldm

    def __set_ldm(self, ldm):
        if not (isinstance(ldm, float) or isinstance(ldm, int) or ldm is None):
            raise Exception(f'Cannot set field "ldm" (type float) to {repr(ldm)}')

        self.__ldm = ldm

    ldm = property(__get_ldm, __set_ldm)
    """
    Row area in loading metres (ex.: 1 EUR pallet = 0.4 LDM)
    """

    __description: Optional[str] = None

    def __get_description(self):
        return self.__description

    def __set_description(self, description):
        if not (isinstance(description, str) or description is None):
            raise Exception(f'Cannot set field "description" (type str) to {repr(description)}')

        self.__description = description

    description = property(__get_description, __set_description)
    """
    Description of the goods in this row
    """

    # noinspection PyArgumentList
    def __init__(self, quantity=None, package_type=None, weight=None, length=None, width=None, height=None, cbm=None, ldm=None, description=None):
        self.__set_quantity(quantity)
        self.__set_package_type(package_type)
        self.__set_weight(weight)
        self.__set_length(length)
        self.__set_width(width)
        self.__set_height(height)
        self.__set_cbm(cbm)
        self.__set_ldm(ldm)
        self.__set_description(description)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['quantity'] = d.get('quantity')
        v['package_type'] = d.get('package_type')
        v['weight'] = d.get('weight')
        v['length'] = d.get('length')
        v['width'] = d.get('width')
        v['height'] = d.get('height')
        v['cbm'] = d.get('cbm')
        v['ldm'] = d.get('ldm')
        v['description'] = d.get('description')
        return PriceRequestShipmentRows_AttributesItem(**v)

    def as_dict(self):
        return dict(
            quantity=self.__quantity,
            package_type=self.__package_type,
            weight=self.__weight,
            length=self.__length,
            width=self.__width,
            height=self.__height,
            cbm=self.__cbm,
            ldm=self.__ldm,
            description=self.__description
        )


# noinspection PyPep8Naming
class PriceRequestShipment(object):
    """
    the shipment for which the prices are requested
    """

    __collection_date: Optional[str] = None

    def __get_collection_date(self):
        return self.__collection_date

    def __set_collection_date(self, collection_date):
        if not (isinstance(collection_date, str) or collection_date is None):
            raise Exception(f'Cannot set field "collection_date" (type str) to {repr(collection_date)}')

        self.__collection_date = collection_date

    collection_date = property(__get_collection_date, __set_collection_date)
    """
    Date when goods are ready for collection. Can be today or in the future
    """

    __collection_postcode: Optional[str] = None

    def __get_collection_postcode(self):
        return self.__collection_postcode

    def __set_collection_postcode(self, collection_postcode):
        if not (isinstance(collection_postcode, str) or collection_postcode is None):
            raise Exception(f'Cannot set field "collection_postcode" (type str) to {repr(collection_postcode)}')

        self.__collection_postcode = collection_postcode

    collection_postcode = property(__get_collection_postcode, __set_collection_postcode)
    """
    ZIP or postal code. May contain both numbers and letters. Should not include the country code.
    """

    __collection_country: Optional[str] = None

    def __get_collection_country(self):
        return self.__collection_country

    def __set_collection_country(self, collection_country):
        if not (isinstance(collection_country, str) or collection_country is None):
            raise Exception(f'Cannot set field "collection_country" (type str) to {repr(collection_country)}')

        self.__collection_country = collection_country

    collection_country = property(__get_collection_country, __set_collection_country)
    """
    Two-letter country code (ISO 3166-1 alpha-2)
    """

    __delivery_postcode: Optional[str] = None

    def __get_delivery_postcode(self):
        return self.__delivery_postcode

    def __set_delivery_postcode(self, delivery_postcode):
        if not (isinstance(delivery_postcode, str) or delivery_postcode is None):
            raise Exception(f'Cannot set field "delivery_postcode" (type str) to {repr(delivery_postcode)}')

        self.__delivery_postcode = delivery_postcode

    delivery_postcode = property(__get_delivery_postcode, __set_delivery_postcode)
    """
    ZIP or postal code. May contain both numbers and letters. Should not include the country code.
    """

    __delivery_country: Optional[str] = None

    def __get_delivery_country(self):
        return self.__delivery_country

    def __set_delivery_country(self, delivery_country):
        if not (isinstance(delivery_country, str) or delivery_country is None):
            raise Exception(f'Cannot set field "delivery_country" (type str) to {repr(delivery_country)}')

        self.__delivery_country = delivery_country

    delivery_country = property(__get_delivery_country, __set_delivery_country)
    """
    Two-letter country code (ISO 3166-1 alpha-2)
    """

    __frigo: Optional[bool] = None

    def __get_frigo(self):
        return self.__frigo

    def __set_frigo(self, frigo):
        if not (isinstance(frigo, bool) or frigo is None):
            raise Exception(f'Cannot set field "frigo" (type bool) to {repr(frigo)}')

        self.__frigo = frigo

    frigo = property(__get_frigo, __set_frigo)
    """
    Indicates whether the goods are temperature sensitive
    """

    __adr: Optional[bool] = None

    def __get_adr(self):
        return self.__adr

    def __set_adr(self, adr):
        if not (isinstance(adr, bool) or adr is None):
            raise Exception(f'Cannot set field "adr" (type bool) to {repr(adr)}')

        self.__adr = adr

    adr = property(__get_adr, __set_adr)
    """
    Indicates whether the shipment is hazardous (ADR). The shipment is hazardous if any of its goods contain hazardous goods
    """

    __collection_prenotification: Optional[bool] = None

    def __get_collection_prenotification(self):
        return self.__collection_prenotification

    def __set_collection_prenotification(self, collection_prenotification):
        if not (isinstance(collection_prenotification, bool) or collection_prenotification is None):
            raise Exception(f'Cannot set field "collection_prenotification" (type bool) to {repr(collection_prenotification)}')

        self.__collection_prenotification = collection_prenotification

    collection_prenotification = property(__get_collection_prenotification, __set_collection_prenotification)
    """
    Indicates whether the driver should call the collection contact before loading
    """

    __collection_with_tail_lift: Optional[bool] = None

    def __get_collection_with_tail_lift(self):
        return self.__collection_with_tail_lift

    def __set_collection_with_tail_lift(self, collection_with_tail_lift):
        if not (isinstance(collection_with_tail_lift, bool) or collection_with_tail_lift is None):
            raise Exception(f'Cannot set field "collection_with_tail_lift" (type bool) to {repr(collection_with_tail_lift)}')

        self.__collection_with_tail_lift = collection_with_tail_lift

    collection_with_tail_lift = property(__get_collection_with_tail_lift, __set_collection_with_tail_lift)
    """
    Indicates whether the collection should be performed with a tail-lift truck
    """

    __delivery_prenotification: Optional[bool] = None

    def __get_delivery_prenotification(self):
        return self.__delivery_prenotification

    def __set_delivery_prenotification(self, delivery_prenotification):
        if not (isinstance(delivery_prenotification, bool) or delivery_prenotification is None):
            raise Exception(f'Cannot set field "delivery_prenotification" (type bool) to {repr(delivery_prenotification)}')

        self.__delivery_prenotification = delivery_prenotification

    delivery_prenotification = property(__get_delivery_prenotification, __set_delivery_prenotification)
    """
    Indicates whether the driver should call the delivery contact before loading
    """

    __delivery_with_tail_lift: Optional[bool] = None

    def __get_delivery_with_tail_lift(self):
        return self.__delivery_with_tail_lift

    def __set_delivery_with_tail_lift(self, delivery_with_tail_lift):
        if not (isinstance(delivery_with_tail_lift, bool) or delivery_with_tail_lift is None):
            raise Exception(f'Cannot set field "delivery_with_tail_lift" (type bool) to {repr(delivery_with_tail_lift)}')

        self.__delivery_with_tail_lift = delivery_with_tail_lift

    delivery_with_tail_lift = property(__get_delivery_with_tail_lift, __set_delivery_with_tail_lift)
    """
    Indicates whether the delivery should be performed with a tail-lift truck
    """

    __delivery_return_document: Optional[bool] = None

    def __get_delivery_return_document(self):
        return self.__delivery_return_document

    def __set_delivery_return_document(self, delivery_return_document):
        if not (isinstance(delivery_return_document, bool) or delivery_return_document is None):
            raise Exception(f'Cannot set field "delivery_return_document" (type bool) to {repr(delivery_return_document)}')

        self.__delivery_return_document = delivery_return_document

    delivery_return_document = property(__get_delivery_return_document, __set_delivery_return_document)
    """
    Indicates whether the customer expects signed documents to be returned
    """

    __delivery_to_private_person: Optional[bool] = None

    def __get_delivery_to_private_person(self):
        return self.__delivery_to_private_person

    def __set_delivery_to_private_person(self, delivery_to_private_person):
        if not (isinstance(delivery_to_private_person, bool) or delivery_to_private_person is None):
            raise Exception(f'Cannot set field "delivery_to_private_person" (type bool) to {repr(delivery_to_private_person)}')

        self.__delivery_to_private_person = delivery_to_private_person

    delivery_to_private_person = property(__get_delivery_to_private_person, __set_delivery_to_private_person)
    """
    Indicates whether the goods will be delivered to a private person instead of a company
    """

    __rows_attributes: Optional[List["PriceRequestShipmentRows_AttributesItem"]] = []

    def __get_rows_attributes(self):
        return self.__rows_attributes

    def __set_rows_attributes(self, rows_attributes):
        if not (isinstance(rows_attributes, list) or rows_attributes is None):
            raise Exception(f'Cannot set field List["PriceRequestShipmentRows_AttributesItem"].rows_attributes to {repr(rows_attributes)}')

        self.__rows_attributes = rows_attributes

    rows_attributes = property(__get_rows_attributes, __set_rows_attributes)
    """
    Array of goods rows, with each row consisting of the following 7 (or less) key-value pairs
    """

    # noinspection PyArgumentList
    def __init__(self, collection_date, collection_postcode, collection_country, delivery_postcode, delivery_country, frigo=None, adr=None, collection_prenotification=None, collection_with_tail_lift=None, delivery_prenotification=None, delivery_with_tail_lift=None, delivery_return_document=None, delivery_to_private_person=None, rows_attributes=None):
        self.__set_collection_date(collection_date)
        self.__set_collection_postcode(collection_postcode)
        self.__set_collection_country(collection_country)
        self.__set_delivery_postcode(delivery_postcode)
        self.__set_delivery_country(delivery_country)
        self.__set_frigo(frigo)
        self.__set_adr(adr)
        self.__set_collection_prenotification(collection_prenotification)
        self.__set_collection_with_tail_lift(collection_with_tail_lift)
        self.__set_delivery_prenotification(delivery_prenotification)
        self.__set_delivery_with_tail_lift(delivery_with_tail_lift)
        self.__set_delivery_return_document(delivery_return_document)
        self.__set_delivery_to_private_person(delivery_to_private_person)
        self.__set_rows_attributes(rows_attributes)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['collection_date'] = d.get('collection_date')
        v['collection_postcode'] = d.get('collection_postcode')
        v['collection_country'] = d.get('collection_country')
        v['delivery_postcode'] = d.get('delivery_postcode')
        v['delivery_country'] = d.get('delivery_country')
        v['frigo'] = d.get('frigo')
        v['adr'] = d.get('adr')
        v['collection_prenotification'] = d.get('collection_prenotification')
        v['collection_with_tail_lift'] = d.get('collection_with_tail_lift')
        v['delivery_prenotification'] = d.get('delivery_prenotification')
        v['delivery_with_tail_lift'] = d.get('delivery_with_tail_lift')
        v['delivery_return_document'] = d.get('delivery_return_document')
        v['delivery_to_private_person'] = d.get('delivery_to_private_person')
        v['rows_attributes'] = [PriceRequestShipmentRows_AttributesItem.from_dict(item) for item in d.get('rows_attributes')]
        return PriceRequestShipment(**v)

    def as_dict(self):
        return dict(
            collection_date=self.__collection_date,
            collection_postcode=self.__collection_postcode,
            collection_country=self.__collection_country,
            delivery_postcode=self.__delivery_postcode,
            delivery_country=self.__delivery_country,
            frigo=self.__frigo,
            adr=self.__adr,
            collection_prenotification=self.__collection_prenotification,
            collection_with_tail_lift=self.__collection_with_tail_lift,
            delivery_prenotification=self.__delivery_prenotification,
            delivery_with_tail_lift=self.__delivery_with_tail_lift,
            delivery_return_document=self.__delivery_return_document,
            delivery_to_private_person=self.__delivery_to_private_person,
            rows_attributes=[item.as_dict() for item in self.__rows_attributes] if self.__rows_attributes is not None else None
        )


