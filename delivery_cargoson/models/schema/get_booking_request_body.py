from typing import Optional
import enum


# noinspection PyPep8Naming
class GetBookingRequestBodyOptionsInclude_Associations(object):
    """
    Object that holds options for which attribute groups to fetch. By default, these additional attributes are all disabled. Enable only what you need, since every additional step will make the request a bit slower.
    """

    __offer: Optional[bool] = None

    def __get_offer(self):
        return self.__offer

    def __set_offer(self, offer):
        if not (isinstance(offer, bool) or offer is None):
            raise Exception(f'Cannot set field "offer" (type bool) to {repr(offer)}')

        self.__offer = offer

    offer = property(__get_offer, __set_offer)
    """
    Indicates whether you want to receive information about the selected offer (price, service, carrier etc).
    """

    __carrier: Optional[bool] = None

    def __get_carrier(self):
        return self.__carrier

    def __set_carrier(self, carrier):
        if not (isinstance(carrier, bool) or carrier is None):
            raise Exception(f'Cannot set field "carrier" (type bool) to {repr(carrier)}')

        self.__carrier = carrier

    carrier = property(__get_carrier, __set_carrier)
    """
    Indicates whether you want to receive information about the selected carrier.
    """

    __consignor: Optional[bool] = None

    def __get_consignor(self):
        return self.__consignor

    def __set_consignor(self, consignor):
        if not (isinstance(consignor, bool) or consignor is None):
            raise Exception(f'Cannot set field "consignor" (type bool) to {repr(consignor)}')

        self.__consignor = consignor

    consignor = property(__get_consignor, __set_consignor)
    """
    Indicates whether you want to receive information about the consignor (sender).
    """

    __consignee: Optional[bool] = None

    def __get_consignee(self):
        return self.__consignee

    def __set_consignee(self, consignee):
        if not (isinstance(consignee, bool) or consignee is None):
            raise Exception(f'Cannot set field "consignee" (type bool) to {repr(consignee)}')

        self.__consignee = consignee

    consignee = property(__get_consignee, __set_consignee)
    """
    Indicates whether you want to receive information about the consignee (receiver).
    """

    __rows: Optional[bool] = None

    def __get_rows(self):
        return self.__rows

    def __set_rows(self, rows):
        if not (isinstance(rows, bool) or rows is None):
            raise Exception(f'Cannot set field "rows" (type bool) to {repr(rows)}')

        self.__rows = rows

    rows = property(__get_rows, __set_rows)
    """
    Indicates whether you want to receive information about the goods rows.
    """

    __declaration: Optional[bool] = None

    def __get_declaration(self):
        return self.__declaration

    def __set_declaration(self, declaration):
        if not (isinstance(declaration, bool) or declaration is None):
            raise Exception(f'Cannot set field "declaration" (type bool) to {repr(declaration)}')

        self.__declaration = declaration

    declaration = property(__get_declaration, __set_declaration)
    """
    Indicates whether you want to receive information about the declaration.
    """

    # noinspection PyArgumentList
    def __init__(self, offer=None, carrier=None, consignor=None, consignee=None, rows=None, declaration=None):
        self.__set_offer(offer)
        self.__set_carrier(carrier)
        self.__set_consignor(consignor)
        self.__set_consignee(consignee)
        self.__set_rows(rows)
        self.__set_declaration(declaration)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['offer'] = d.get('offer')
        v['carrier'] = d.get('carrier')
        v['consignor'] = d.get('consignor')
        v['consignee'] = d.get('consignee')
        v['rows'] = d.get('rows')
        v['declaration'] = d.get('declaration')
        return GetBookingRequestBodyOptionsInclude_Associations(**v)

    def as_dict(self):
        res = dict()
        if self.__offer is not None:
            res['offer'] = self.__offer
        if self.__carrier is not None:
            res['carrier'] = self.__carrier
        if self.__consignor is not None:
            res['consignor'] = self.__consignor
        if self.__consignee is not None:
            res['consignee'] = self.__consignee
        if self.__rows is not None:
            res['rows'] = self.__rows
        if self.__declaration is not None:
            res['declaration'] = self.__declaration
        return res


# noinspection PyPep8Naming
class GetBookingRequestBodyOptionsLabel_Format(enum.Enum):
    """
    The response includes a link to the goods labels. You can choose the format of those labels with this option. 
    ```a4``` => up to four A6 labels per one A4 page. 
    ```label_printer``` => one label per page in the size of 4x6 inches (10.16 x 15.24 cm, which is close to the A6 format.)
    """

    LABEL_PRINTER = 'label_printer'
    A4 = 'a4'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return GetBookingRequestBodyOptionsLabel_Format(value)


# noinspection PyPep8Naming
class GetBookingRequestBodyOptions(object):
    """
    Object that holds different options for fetching data about the booking
    """

    __label_format: Optional[GetBookingRequestBodyOptionsLabel_Format] = None

    def __get_label_format(self):
        return self.__label_format

    def __set_label_format(self, label_format):
        if not (label_format.as_dict() if hasattr(label_format, "as_dict") else label_format in ['label_printer', 'a4'] or label_format is None):
            raise Exception(f'Cannot set field GetBookingRequestBodyOptionsLabel_Format.label_format to {repr(label_format)}')

        self.__label_format = label_format

    label_format = property(__get_label_format, __set_label_format)
    """
    The response includes a link to the goods labels. You can choose the format of those labels with this option. 
    ```a4``` => up to four A6 labels per one A4 page. 
    ```label_printer``` => one label per page in the size of 4x6 inches (10.16 x 15.24 cm, which is close to the A6 format.)
    """

    __include_associations: Optional[GetBookingRequestBodyOptionsInclude_Associations] = None

    def __get_include_associations(self):
        return self.__include_associations

    def __set_include_associations(self, include_associations):
        if not (isinstance(include_associations, GetBookingRequestBodyOptionsInclude_Associations) or include_associations is None):
            raise Exception(f'Cannot set field GetBookingRequestBodyOptionsInclude_Associations.include_associations to {repr(include_associations)}')

        self.__include_associations = include_associations

    include_associations = property(__get_include_associations, __set_include_associations)
    """
    Object that holds options for which attribute groups to fetch. By default, these additional attributes are all disabled. Enable only what you need, since every additional step will make the request a bit slower.
    """

    # noinspection PyArgumentList
    def __init__(self, label_format=None, include_associations=None):
        self.__set_label_format(label_format)
        self.__set_include_associations(include_associations)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['label_format'] = GetBookingRequestBodyOptionsLabel_Format.from_dict(d.get('label_format'))
        v['include_associations'] = GetBookingRequestBodyOptionsInclude_Associations.from_dict(d.get('include_associations'))
        return GetBookingRequestBodyOptions(**v)

    def as_dict(self):
        res = dict()
        if self.__label_format is not None:
            res['label_format'] = self.__label_format.as_dict()
        if self.__include_associations is not None:
            res['include_associations'] = self.__include_associations.as_dict()
        return res


# noinspection PyPep8Naming
class GetBookingRequestBody(object):
    """
    Request body for defining different options for fetching a booking
    """

    __options: Optional[GetBookingRequestBodyOptions] = None

    def __get_options(self):
        return self.__options

    def __set_options(self, options):
        if not (isinstance(options, GetBookingRequestBodyOptions) or options is None):
            raise Exception(f'Cannot set field GetBookingRequestBodyOptions.options to {repr(options)}')

        self.__options = options

    options = property(__get_options, __set_options)
    """
    Object that holds different options for fetching data about the booking
    """

    # noinspection PyArgumentList
    def __init__(self, options=None):
        self.__set_options(options)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['options'] = GetBookingRequestBodyOptions.from_dict(d.get('options'))
        return GetBookingRequestBody(**v)

    def as_dict(self):
        res = dict()
        if self.__options is not None:
            res['options'] = self.__options.as_dict()
        return res


