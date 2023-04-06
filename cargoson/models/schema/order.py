from typing import List
from typing import Optional
import enum


# noinspection PyPep8Naming
class OrderDeclaration_AttributesDeclaration_Documents_AttributesItemCategory(enum.Enum):
    """
    Document type  
      
    972: T2LF Dispense Paiement Droits  
    AHC: Analysis and Health Certificate  
    ATA: ATA Carnet  
    ATR: Preference Certificate ATR  
    CHD: CHED-D (Common Health Entry Document for Feed and Food of Non-Animal Origin)  
    CHP: CHED-P (Common Health Entry Document for Products)  
    CIT: CITES Certificate  
    COO: Generic Certificate of Origin  
    DEX: Duty Exemption Certificate  
    EU1: Preference Certificate EUR1  
    EU2: Preferential Declaration of Origin on the Invoice - EUR2  
    EUS: End Use Authorization  
    FMA: Certificate of Origin (Form A)  
    PHY: Phytosanitary Certificate  
    VET: Veterinary Entry Document  
    VEX: VAT Exemption Certificate  
    CRL: Control Document  
    CSD: Consolidated Customs Entry  
    PPY: Proof Of Payment  
    CI2: Export-only Invoice  
    CIV: Customs Invoice Value  
    DOV: Invoice  
    INV: Commercial Invoice  
    PFI: Pro-Forma  
    ALC: Agricultural License  
    HLC: Health Products RegulatoryAuthority (HPRA) Licensing Requirements  
    JLC: Justice License  
    LIC: Specific Export Licenses  
    LNP: License or Permit  
    PLI: Permits & Licenses  
    DLI: Driver's License  
    NID: National Identity Card  
    PAS: Passport  
    CHA: Power of Attorney  
    CPA: Consignee Power of Attorney  
    POA: Power of Attorney (Customer-based)  
    BEX: Branch Letter of Exemption  
    DGD: Dangerous Goods Declaration  
    IPA: Intellectual Property Authorization  
    T2M: T2M Transport Accompanying Document  
    TAD: TAD Transport Accompanying Document T1  
    TCS: Transportation Charges Statement  
    ROD: Receipt on Delivery  
    EXL: DCE Export of Customs Data  
    HWB: House Waybill  
    ELP: Export Licenses and Permits
    """

    CIV = 'CIV'
    DOV = 'DOV'
    INV = 'INV'
    ATR = 'ATR'
    CHD = 'CHD'
    CHP = 'CHP'
    CIT = 'CIT'
    COO = 'COO'
    DEX = 'DEX'
    EU1 = 'EU1'
    EU2 = 'EU2'
    EUS = 'EUS'
    FMA = 'FMA'
    PHY = 'PHY'
    VET = 'VET'
    VEX = 'VEX'
    CRL = 'CRL'
    CSD = 'CSD'
    PPY = 'PPY'
    CI2 = 'CI2'
    VALUE_972 = '972'
    AHC = 'AHC'
    ATA = 'ATA'
    PFI = 'PFI'
    ALC = 'ALC'
    HLC = 'HLC'
    JLC = 'JLC'
    LIC = 'LIC'
    LNP = 'LNP'
    PLI = 'PLI'
    DLI = 'DLI'
    NID = 'NID'
    PAS = 'PAS'
    CHA = 'CHA'
    CPA = 'CPA'
    POA = 'POA'
    BEX = 'BEX'
    DGD = 'DGD'
    IPA = 'IPA'
    T2M = 'T2M'
    TAD = 'TAD'
    TCS = 'TCS'
    ROD = 'ROD'
    EXL = 'EXL'
    HWB = 'HWB'
    ELP = 'ELP'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderDeclaration_AttributesDeclaration_Documents_AttributesItemCategory(value)


# noinspection PyPep8Naming
class OrderDeclaration_AttributesDeclaration_Charges_AttributesItemCategory(enum.Enum):
    """
    Charge type  
      
    ADMIN: Administration fee  
    DELIV: Delivery fee  
    DOCUM: Documentation fee  
    EXPED: Expedite fee  
    EXCHA: Export fee  
    FRCST: Freight cost  
    SSRGE: Fuel surcharge  
    LOGST: Logistic fee  
    SOTHR: Other fee  
    SPKGN: Packaging/packing fee  
    PICUP: Pickup fee  
    HRCRG: Handling fee  
    VATCR: VAT fee  
    INSCH: Insurance cost  
    REVCH: Reverse charge
    """

    ADMIN = 'ADMIN'
    DELIV = 'DELIV'
    DOCUM = 'DOCUM'
    EXPED = 'EXPED'
    EXCHA = 'EXCHA'
    FRCST = 'FRCST'
    SSRGE = 'SSRGE'
    LOGST = 'LOGST'
    SOTHR = 'SOTHR'
    SPKGN = 'SPKGN'
    PICUP = 'PICUP'
    HRCRG = 'HRCRG'
    VATCR = 'VATCR'
    INSCH = 'INSCH'
    REVCH = 'REVCH'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderDeclaration_AttributesDeclaration_Charges_AttributesItemCategory(value)


# noinspection PyPep8Naming
class OrderDeclaration_AttributesDeclaration_Items_AttributesItemUnit_Of_Measure(enum.Enum):
    """
    Unit of measure of stated quanity. (Usually Pieces)   
    BOX: Boxes  
    2GM: Centigram  
    2M: Centimeters  
    2M3: Cubic Centimeters  
    3M3: Cubic Feet  
    M3: Cubic Meters  
    DPR: Dozen Pairs  
    DOZ: Dozen  
    2NO: Each  
    PCS: Pieces  
    GM: Grams  
    GRS: Gross  
    KG: Kilograms  
    L: Liters  
    M: Meters  
    3GM: Milligrams  
    3L: Milliliters  
    X: No Unit Required  
    NO: Number  
    2KG: Ounces  
    PRS: Pairs  
    2L: Gallons  
    3KG: Pounds  
    CM2: Square Centimeters  
    2M2: Square Feet  
    3M2: Square Inches  
    M2: Square Meters  
    4M2: Square Yards  
    3M: Yards
    """

    BOX = 'BOX'
    VALUE_2GM = '2GM'
    VALUE_2M = '2M'
    VALUE_2M3 = '2M3'
    VALUE_3M3 = '3M3'
    M3 = 'M3'
    DPR = 'DPR'
    DOZ = 'DOZ'
    VALUE_2NO = '2NO'
    PCS = 'PCS'
    GM = 'GM'
    GRS = 'GRS'
    KG = 'KG'
    L = 'L'
    M = 'M'
    VALUE_3GM = '3GM'
    VALUE_3L = '3L'
    X = 'X'
    VALUE_FALSE = False
    VALUE_2KG = '2KG'
    PRS = 'PRS'
    VALUE_2L = '2L'
    VALUE_3KG = '3KG'
    CM2 = 'CM2'
    VALUE_2M2 = '2M2'
    VALUE_3M2 = '3M2'
    M2 = 'M2'
    VALUE_4M2 = '4M2'
    VALUE_3M = '3M'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderDeclaration_AttributesDeclaration_Items_AttributesItemUnit_Of_Measure(value)


# noinspection PyPep8Naming
class OrderDeclaration_AttributesDeclaration_Documents_AttributesItem(object):
    """
    Document references related to declaration. These files should be included in the ```documents_attributes```
    """

    __category: Optional[OrderDeclaration_AttributesDeclaration_Documents_AttributesItemCategory] = None

    def __get_category(self):
        return self.__category

    def __set_category(self, category):
        if not (category in ['CIV', 'DOV', 'INV', 'ATR', 'CHD', 'CHP', 'CIT', 'COO', 'DEX', 'EU1', 'EU2', 'EUS', 'FMA', 'PHY', 'VET', 'VEX', 'CRL', 'CSD', 'PPY', 'CI2', '972', 'AHC', 'ATA', 'PFI', 'ALC', 'HLC', 'JLC', 'LIC', 'LNP', 'PLI', 'DLI', 'NID', 'PAS', 'CHA', 'CPA', 'POA', 'BEX', 'DGD', 'IPA', 'T2M', 'TAD', 'TCS', 'ROD', 'EXL', 'HWB', 'ELP'] or category is None):
            raise Exception(f'Cannot set field OrderDeclaration_AttributesDeclaration_Documents_AttributesItemCategory.category to {repr(category)}')

        self.__category = category

    category = property(__get_category, __set_category)
    """
    Document type  
      
    972: T2LF Dispense Paiement Droits  
    AHC: Analysis and Health Certificate  
    ATA: ATA Carnet  
    ATR: Preference Certificate ATR  
    CHD: CHED-D (Common Health Entry Document for Feed and Food of Non-Animal Origin)  
    CHP: CHED-P (Common Health Entry Document for Products)  
    CIT: CITES Certificate  
    COO: Generic Certificate of Origin  
    DEX: Duty Exemption Certificate  
    EU1: Preference Certificate EUR1  
    EU2: Preferential Declaration of Origin on the Invoice - EUR2  
    EUS: End Use Authorization  
    FMA: Certificate of Origin (Form A)  
    PHY: Phytosanitary Certificate  
    VET: Veterinary Entry Document  
    VEX: VAT Exemption Certificate  
    CRL: Control Document  
    CSD: Consolidated Customs Entry  
    PPY: Proof Of Payment  
    CI2: Export-only Invoice  
    CIV: Customs Invoice Value  
    DOV: Invoice  
    INV: Commercial Invoice  
    PFI: Pro-Forma  
    ALC: Agricultural License  
    HLC: Health Products RegulatoryAuthority (HPRA) Licensing Requirements  
    JLC: Justice License  
    LIC: Specific Export Licenses  
    LNP: License or Permit  
    PLI: Permits & Licenses  
    DLI: Driver's License  
    NID: National Identity Card  
    PAS: Passport  
    CHA: Power of Attorney  
    CPA: Consignee Power of Attorney  
    POA: Power of Attorney (Customer-based)  
    BEX: Branch Letter of Exemption  
    DGD: Dangerous Goods Declaration  
    IPA: Intellectual Property Authorization  
    T2M: T2M Transport Accompanying Document  
    TAD: TAD Transport Accompanying Document T1  
    TCS: Transportation Charges Statement  
    ROD: Receipt on Delivery  
    EXL: DCE Export of Customs Data  
    HWB: House Waybill  
    ELP: Export Licenses and Permits
    """

    __document_id: Optional[str] = None

    def __get_document_id(self):
        return self.__document_id

    def __set_document_id(self, document_id):
        if not (isinstance(document_id, str) or document_id is None):
            raise Exception(f'Cannot set field "document_id" (type str) to {repr(document_id)}')

        self.__document_id = document_id

    document_id = property(__get_document_id, __set_document_id)
    """
    Document reference number/ID
    """

    # noinspection PyArgumentList
    def __init__(self, category=None, document_id=None):
        self.__set_category(category)
        self.__set_document_id(document_id)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['category'] = d.get('category')
        v['document_id'] = d.get('document_id')
        return OrderDeclaration_AttributesDeclaration_Documents_AttributesItem(**v)

    def as_dict(self):
        return dict(
            category=self.__category,
            document_id=self.__document_id
        )


# noinspection PyPep8Naming
class OrderDeclaration_AttributesDeclaration_Charges_AttributesItem(object):
    """
    Charges
    """

    __category: Optional[OrderDeclaration_AttributesDeclaration_Charges_AttributesItemCategory] = None

    def __get_category(self):
        return self.__category

    def __set_category(self, category):
        if not (category in ['ADMIN', 'DELIV', 'DOCUM', 'EXPED', 'EXCHA', 'FRCST', 'SSRGE', 'LOGST', 'SOTHR', 'SPKGN', 'PICUP', 'HRCRG', 'VATCR', 'INSCH', 'REVCH'] or category is None):
            raise Exception(f'Cannot set field OrderDeclaration_AttributesDeclaration_Charges_AttributesItemCategory.category to {repr(category)}')

        self.__category = category

    category = property(__get_category, __set_category)
    """
    Charge type  
      
    ADMIN: Administration fee  
    DELIV: Delivery fee  
    DOCUM: Documentation fee  
    EXPED: Expedite fee  
    EXCHA: Export fee  
    FRCST: Freight cost  
    SSRGE: Fuel surcharge  
    LOGST: Logistic fee  
    SOTHR: Other fee  
    SPKGN: Packaging/packing fee  
    PICUP: Pickup fee  
    HRCRG: Handling fee  
    VATCR: VAT fee  
    INSCH: Insurance cost  
    REVCH: Reverse charge
    """

    __value: Optional[float] = None

    def __get_value(self):
        return self.__value

    def __set_value(self, value):
        if not (isinstance(value, float) or isinstance(value, int) or value is None):
            raise Exception(f'Cannot set field "value" (type float) to {repr(value)}')

        self.__value = value

    value = property(__get_value, __set_value)
    """
    Charge value
    """

    # noinspection PyArgumentList
    def __init__(self, category=None, value=None):
        self.__set_category(category)
        self.__set_value(value)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['category'] = d.get('category')
        v['value'] = d.get('value')
        return OrderDeclaration_AttributesDeclaration_Charges_AttributesItem(**v)

    def as_dict(self):
        return dict(
            category=self.__category,
            value=self.__value
        )


# noinspection PyPep8Naming
class OrderDeclaration_AttributesDeclaration_Items_AttributesItem(object):
    """
    Goods to be declared
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
    Number of goods
    """

    __unit_of_measure: Optional[OrderDeclaration_AttributesDeclaration_Items_AttributesItemUnit_Of_Measure] = None

    def __get_unit_of_measure(self):
        return self.__unit_of_measure

    def __set_unit_of_measure(self, unit_of_measure):
        if not (unit_of_measure in ['BOX', '2GM', '2M', '2M3', '3M3', 'M3', 'DPR', 'DOZ', '2NO', 'PCS', 'GM', 'GRS', 'KG', 'L', 'M', '3GM', '3L', 'X', False, '2KG', 'PRS', '2L', '3KG', 'CM2', '2M2', '3M2', 'M2', '4M2', '3M'] or unit_of_measure is None):
            raise Exception(f'Cannot set field OrderDeclaration_AttributesDeclaration_Items_AttributesItemUnit_Of_Measure.unit_of_measure to {repr(unit_of_measure)}')

        self.__unit_of_measure = unit_of_measure

    unit_of_measure = property(__get_unit_of_measure, __set_unit_of_measure)
    """
    Unit of measure of stated quanity. (Usually Pieces)   
    BOX: Boxes  
    2GM: Centigram  
    2M: Centimeters  
    2M3: Cubic Centimeters  
    3M3: Cubic Feet  
    M3: Cubic Meters  
    DPR: Dozen Pairs  
    DOZ: Dozen  
    2NO: Each  
    PCS: Pieces  
    GM: Grams  
    GRS: Gross  
    KG: Kilograms  
    L: Liters  
    M: Meters  
    3GM: Milligrams  
    3L: Milliliters  
    X: No Unit Required  
    NO: Number  
    2KG: Ounces  
    PRS: Pairs  
    2L: Gallons  
    3KG: Pounds  
    CM2: Square Centimeters  
    2M2: Square Feet  
    3M2: Square Inches  
    M2: Square Meters  
    4M2: Square Yards  
    3M: Yards
    """

    __hs_code: Optional[str] = None

    def __get_hs_code(self):
        return self.__hs_code

    def __set_hs_code(self, hs_code):
        if not (isinstance(hs_code, str) or hs_code is None):
            raise Exception(f'Cannot set field "hs_code" (type str) to {repr(hs_code)}')

        self.__hs_code = hs_code

    hs_code = property(__get_hs_code, __set_hs_code)
    """
    TARIC (10 digits), Combined Nomenclature (8 digits) or Harmonised System code (6 digits) for goods
    """

    __origin_country: Optional[str] = None

    def __get_origin_country(self):
        return self.__origin_country

    def __set_origin_country(self, origin_country):
        if not (isinstance(origin_country, str) or origin_country is None):
            raise Exception(f'Cannot set field "origin_country" (type str) to {repr(origin_country)}')

        self.__origin_country = origin_country

    origin_country = property(__get_origin_country, __set_origin_country)
    """
    Country of Origin/Manufacture. ISO 3166-2
    """

    __net_weight: Optional[float] = None

    def __get_net_weight(self):
        return self.__net_weight

    def __set_net_weight(self, net_weight):
        if not (isinstance(net_weight, float) or isinstance(net_weight, int) or net_weight is None):
            raise Exception(f'Cannot set field "net_weight" (type float) to {repr(net_weight)}')

        self.__net_weight = net_weight

    net_weight = property(__get_net_weight, __set_net_weight)
    """
    Net weight of goods (kg) PER ITEM
    """

    __gross_weight: Optional[float] = None

    def __get_gross_weight(self):
        return self.__gross_weight

    def __set_gross_weight(self, gross_weight):
        if not (isinstance(gross_weight, float) or isinstance(gross_weight, int) or gross_weight is None):
            raise Exception(f'Cannot set field "gross_weight" (type float) to {repr(gross_weight)}')

        self.__gross_weight = gross_weight

    gross_weight = property(__get_gross_weight, __set_gross_weight)
    """
    Gross weight of goods (kg) PER ITEM
    """

    __value: Optional[float] = None

    def __get_value(self):
        return self.__value

    def __set_value(self, value):
        if not (isinstance(value, float) or isinstance(value, int) or value is None):
            raise Exception(f'Cannot set field "value" (type float) to {repr(value)}')

        self.__value = value

    value = property(__get_value, __set_value)
    """
    Value of goods PER ITEM
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
    Description of the goods, as descriptive as possible
    """

    # noinspection PyArgumentList
    def __init__(self, quantity=None, unit_of_measure=None, hs_code=None, origin_country=None, net_weight=None, gross_weight=None, value=None, description=None):
        self.__set_quantity(quantity)
        self.__set_unit_of_measure(unit_of_measure)
        self.__set_hs_code(hs_code)
        self.__set_origin_country(origin_country)
        self.__set_net_weight(net_weight)
        self.__set_gross_weight(gross_weight)
        self.__set_value(value)
        self.__set_description(description)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['quantity'] = d.get('quantity')
        v['unit_of_measure'] = d.get('unit_of_measure')
        v['hs_code'] = d.get('hs_code')
        v['origin_country'] = d.get('origin_country')
        v['net_weight'] = d.get('net_weight')
        v['gross_weight'] = d.get('gross_weight')
        v['value'] = d.get('value')
        v['description'] = d.get('description')
        return OrderDeclaration_AttributesDeclaration_Items_AttributesItem(**v)

    def as_dict(self):
        return dict(
            quantity=self.__quantity,
            unit_of_measure=self.__unit_of_measure,
            hs_code=self.__hs_code,
            origin_country=self.__origin_country,
            net_weight=self.__net_weight,
            gross_weight=self.__gross_weight,
            value=self.__value,
            description=self.__description
        )


# noinspection PyPep8Naming
class OrderDeclaration_AttributesInvoice_Reference(enum.Enum):
    """
    Invoice reference.  
    ACL - Parent Shipment ID for BBX  
    CID - Customer Identifier  
    CN - Contract Number  
    CU - Consignor reference number  
    ITN - US Export declaration reference ID  
    MRN - Movement Reference number  
    UCN - Unique reference of a consignment (UCRN)  
    OID - Order Number  
    PON - Purchase Order Number  
    RMA - RMA Number  
    AAM - AWB Ref #  
    ABT - Goods Declaration number  
    ADA - Buyer Reference number  
    AES - AES Post Clearance  
    AFD - 1496 Item number  
    ANT - Consignee Reference number  
    BKN - Booking Number  
    BOL - Bill of Lading Number  
    CDN - Customs Declaration number  
    COD - Cash On Delivery  
    DSC - Weltpaket Reference  
    FF - Freight forwarder's reference number  
    FN - Freight bill number  
    FTR - Post Clearance Exemption US  
    HWB - Shipment Identifiers  
    IBC - Inbound center reference number  
    IPP - Insurance Policy Provider  
    LLR - Load list reference  
    MAB - Master Airwaybill Number  
    MWB - MAWB Reference number  
    OBC - Outbound center reference number  
    PD - Vendor Reference Number  
    PRN - Pickup request number  
    RTL - Return Leg waybill number  
    SID - Shipment ID 15 Digit CODA  
    SS - Seller Reference number  
    SWN - Original Waybill number (Return)
    """

    ACL = 'ACL'
    CID = 'CID'
    CN = 'CN'
    CU = 'CU'
    ITN = 'ITN'
    MRN = 'MRN'
    UCN = 'UCN'
    OID = 'OID'
    PON = 'PON'
    RMA = 'RMA'
    AAM = 'AAM'
    ABT = 'ABT'
    ADA = 'ADA'
    AES = 'AES'
    AFD = 'AFD'
    ANT = 'ANT'
    BKN = 'BKN'
    BOL = 'BOL'
    CDN = 'CDN'
    COD = 'COD'
    DSC = 'DSC'
    FF = 'FF'
    FN = 'FN'
    FTR = 'FTR'
    HWB = 'HWB'
    IBC = 'IBC'
    IPP = 'IPP'
    LLR = 'LLR'
    MAB = 'MAB'
    MWB = 'MWB'
    OBC = 'OBC'
    PD = 'PD'
    PRN = 'PRN'
    RTL = 'RTL'
    SID = 'SID'
    SS = 'SS'
    SWN = 'SWN'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderDeclaration_AttributesInvoice_Reference(value)


# noinspection PyPep8Naming
class OrderOptionsLabel_Format(enum.Enum):
    """
    The response includes a link to the goods labels. The link will be empty until the shipment is booked in Cargoson. You can choose the format of those labels with this option. 
    **a4** => up to four A6 labels per one A4 page. 
    **label_printer** => one label per page in the size of 4x6 inches (10.16 x 15.24 cm, which is close to the A6 format.)
    """

    LABEL_PRINTER = 'label_printer'
    A4 = 'a4'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderOptionsLabel_Format(value)


# noinspection PyPep8Naming
class OrderRows_AttributesItemAdr_Rows_AttributesItem(object):
    """
    Array of dangerous goods rows that are included in this goods row, with each row consisting of the following 5 (or less) key-value pairs
    """

    __adr_un: Optional[str] = None

    def __get_adr_un(self):
        return self.__adr_un

    def __set_adr_un(self, adr_un):
        if not (isinstance(adr_un, str) or adr_un is None):
            raise Exception(f'Cannot set field "adr_un" (type str) to {repr(adr_un)}')

        self.__adr_un = adr_un

    adr_un = property(__get_adr_un, __set_adr_un)
    """
    Four-digit UN number that identifies hazardous materials, and articles
    """

    __adr_group: Optional[str] = None

    def __get_adr_group(self):
        return self.__adr_group

    def __set_adr_group(self, adr_group):
        if not (isinstance(adr_group, str) or adr_group is None):
            raise Exception(f'Cannot set field "adr_group" (type str) to {repr(adr_group)}')

        self.__adr_group = adr_group

    adr_group = property(__get_adr_group, __set_adr_group)
    """
    I - high danger, II - medium danger, III - low danger
    """

    __adr_class: Optional[str] = None

    def __get_adr_class(self):
        return self.__adr_class

    def __set_adr_class(self, adr_class):
        if not (isinstance(adr_class, str) or adr_class is None):
            raise Exception(f'Cannot set field "adr_class" (type str) to {repr(adr_class)}')

        self.__adr_class = adr_class

    adr_class = property(__get_adr_class, __set_adr_class)
    """
    1 - Explosives, 2 - Gases, 3 - Flammable liquids, 4 - Flammable solids
    """

    __adr_neq: Optional[str] = None

    def __get_adr_neq(self):
        return self.__adr_neq

    def __set_adr_neq(self, adr_neq):
        if not (isinstance(adr_neq, str) or adr_neq is None):
            raise Exception(f'Cannot set field "adr_neq" (type str) to {repr(adr_neq)}')

        self.__adr_neq = adr_neq

    adr_neq = property(__get_adr_neq, __set_adr_neq)
    """
    The weight or volume of the dangerous goods contained in a package excluding the weight or volume of any packaging material; or the weight of an unpackaged article of dangerous goods
    """

    __adr_description: Optional[str] = None

    def __get_adr_description(self):
        return self.__adr_description

    def __set_adr_description(self, adr_description):
        if not (isinstance(adr_description, str) or adr_description is None):
            raise Exception(f'Cannot set field "adr_description" (type str) to {repr(adr_description)}')

        self.__adr_description = adr_description

    adr_description = property(__get_adr_description, __set_adr_description)
    """
    Description of the dangerous goods
    """

    # noinspection PyArgumentList
    def __init__(self, adr_un=None, adr_group=None, adr_class=None, adr_neq=None, adr_description=None):
        self.__set_adr_un(adr_un)
        self.__set_adr_group(adr_group)
        self.__set_adr_class(adr_class)
        self.__set_adr_neq(adr_neq)
        self.__set_adr_description(adr_description)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['adr_un'] = d.get('adr_un')
        v['adr_group'] = d.get('adr_group')
        v['adr_class'] = d.get('adr_class')
        v['adr_neq'] = d.get('adr_neq')
        v['adr_description'] = d.get('adr_description')
        return OrderRows_AttributesItemAdr_Rows_AttributesItem(**v)

    def as_dict(self):
        return dict(
            adr_un=self.__adr_un,
            adr_group=self.__adr_group,
            adr_class=self.__adr_class,
            adr_neq=self.__adr_neq,
            adr_description=self.__adr_description
        )


# noinspection PyPep8Naming
class OrderRows_AttributesItemPackage_Type(enum.Enum):
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
        return OrderRows_AttributesItemPackage_Type(value)


# noinspection PyPep8Naming
class OrderDocuments_AttributesItemCategory(enum.Enum):
    """
    Type of the document selected from the predefined document types
    """

    GOODS_INVOICE = 'goods_invoice'
    PACKAGE_LIST = 'package_list'
    CMR = 'cmr'
    WAYBILL = 'waybill'
    BOL = 'bol'
    TRANSPORTATION_INVOICE = 'transportation_invoice'
    POD = 'pod'
    LABELS = 'labels'
    OTHER = 'other'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderDocuments_AttributesItemCategory(value)


# noinspection PyPep8Naming
class OrderDeclaration_Attributes(object):
    """
    If the shipment requires a customs declaration, these fields should be filled
    """

    __invoice_reference: Optional[OrderDeclaration_AttributesInvoice_Reference] = None

    def __get_invoice_reference(self):
        return self.__invoice_reference

    def __set_invoice_reference(self, invoice_reference):
        if not (invoice_reference in ['ACL', 'CID', 'CN', 'CU', 'ITN', 'MRN', 'UCN', 'OID', 'PON', 'RMA', 'AAM', 'ABT', 'ADA', 'AES', 'AFD', 'ANT', 'BKN', 'BOL', 'CDN', 'COD', 'DSC', 'FF', 'FN', 'FTR', 'HWB', 'IBC', 'IPP', 'LLR', 'MAB', 'MWB', 'OBC', 'PD', 'PRN', 'RTL', 'SID', 'SS', 'SWN'] or invoice_reference is None):
            raise Exception(f'Cannot set field OrderDeclaration_AttributesInvoice_Reference.invoice_reference to {repr(invoice_reference)}')

        self.__invoice_reference = invoice_reference

    invoice_reference = property(__get_invoice_reference, __set_invoice_reference)
    """
    Invoice reference.  
    ACL - Parent Shipment ID for BBX  
    CID - Customer Identifier  
    CN - Contract Number  
    CU - Consignor reference number  
    ITN - US Export declaration reference ID  
    MRN - Movement Reference number  
    UCN - Unique reference of a consignment (UCRN)  
    OID - Order Number  
    PON - Purchase Order Number  
    RMA - RMA Number  
    AAM - AWB Ref #  
    ABT - Goods Declaration number  
    ADA - Buyer Reference number  
    AES - AES Post Clearance  
    AFD - 1496 Item number  
    ANT - Consignee Reference number  
    BKN - Booking Number  
    BOL - Bill of Lading Number  
    CDN - Customs Declaration number  
    COD - Cash On Delivery  
    DSC - Weltpaket Reference  
    FF - Freight forwarder's reference number  
    FN - Freight bill number  
    FTR - Post Clearance Exemption US  
    HWB - Shipment Identifiers  
    IBC - Inbound center reference number  
    IPP - Insurance Policy Provider  
    LLR - Load list reference  
    MAB - Master Airwaybill Number  
    MWB - MAWB Reference number  
    OBC - Outbound center reference number  
    PD - Vendor Reference Number  
    PRN - Pickup request number  
    RTL - Return Leg waybill number  
    SID - Shipment ID 15 Digit CODA  
    SS - Seller Reference number  
    SWN - Original Waybill number (Return)
    """

    __invoice_reference_text: Optional[str] = None

    def __get_invoice_reference_text(self):
        return self.__invoice_reference_text

    def __set_invoice_reference_text(self, invoice_reference_text):
        if not (isinstance(invoice_reference_text, str) or invoice_reference_text is None):
            raise Exception(f'Cannot set field "invoice_reference_text" (type str) to {repr(invoice_reference_text)}')

        self.__invoice_reference_text = invoice_reference_text

    invoice_reference_text = property(__get_invoice_reference_text, __set_invoice_reference_text)
    """
    Invoice reference number
    """

    __currency: Optional[str] = None

    def __get_currency(self):
        return self.__currency

    def __set_currency(self, currency):
        if not (isinstance(currency, str) or currency is None):
            raise Exception(f'Cannot set field "currency" (type str) to {repr(currency)}')

        self.__currency = currency

    currency = property(__get_currency, __set_currency)
    """
    Currency for all values in declaration. ISO 4217
    """

    __remark: Optional[str] = None

    def __get_remark(self):
        return self.__remark

    def __set_remark(self, remark):
        if not (isinstance(remark, str) or remark is None):
            raise Exception(f'Cannot set field "remark" (type str) to {repr(remark)}')

        self.__remark = remark

    remark = property(__get_remark, __set_remark)
    """
    Remarks for declaration
    """

    __declaration_text: Optional[str] = None

    def __get_declaration_text(self):
        return self.__declaration_text

    def __set_declaration_text(self, declaration_text):
        if not (isinstance(declaration_text, str) or declaration_text is None):
            raise Exception(f'Cannot set field "declaration_text" (type str) to {repr(declaration_text)}')

        self.__declaration_text = declaration_text

    declaration_text = property(__get_declaration_text, __set_declaration_text)
    """
    Field to explicity state that the information declared is correct
    """

    __declaration_items_attributes: Optional[List["OrderDeclaration_AttributesDeclaration_Items_AttributesItem"]] = []

    def __get_declaration_items_attributes(self):
        return self.__declaration_items_attributes

    def __set_declaration_items_attributes(self, declaration_items_attributes):
        if not (isinstance(declaration_items_attributes, list) or declaration_items_attributes is None):
            raise Exception(f'Cannot set field List["OrderDeclaration_AttributesDeclaration_Items_AttributesItem"].declaration_items_attributes to {repr(declaration_items_attributes)}')

        self.__declaration_items_attributes = declaration_items_attributes

    declaration_items_attributes = property(__get_declaration_items_attributes, __set_declaration_items_attributes)
    """
    Goods to be declared
    """

    __declaration_charges_attributes: Optional[List["OrderDeclaration_AttributesDeclaration_Charges_AttributesItem"]] = []

    def __get_declaration_charges_attributes(self):
        return self.__declaration_charges_attributes

    def __set_declaration_charges_attributes(self, declaration_charges_attributes):
        if not (isinstance(declaration_charges_attributes, list) or declaration_charges_attributes is None):
            raise Exception(f'Cannot set field List["OrderDeclaration_AttributesDeclaration_Charges_AttributesItem"].declaration_charges_attributes to {repr(declaration_charges_attributes)}')

        self.__declaration_charges_attributes = declaration_charges_attributes

    declaration_charges_attributes = property(__get_declaration_charges_attributes, __set_declaration_charges_attributes)
    """
    Charges
    """

    __declaration_documents_attributes: Optional[List["OrderDeclaration_AttributesDeclaration_Documents_AttributesItem"]] = []

    def __get_declaration_documents_attributes(self):
        return self.__declaration_documents_attributes

    def __set_declaration_documents_attributes(self, declaration_documents_attributes):
        if not (isinstance(declaration_documents_attributes, list) or declaration_documents_attributes is None):
            raise Exception(f'Cannot set field List["OrderDeclaration_AttributesDeclaration_Documents_AttributesItem"].declaration_documents_attributes to {repr(declaration_documents_attributes)}')

        self.__declaration_documents_attributes = declaration_documents_attributes

    declaration_documents_attributes = property(__get_declaration_documents_attributes, __set_declaration_documents_attributes)
    """
    Document references related to declaration. These files should be included in the ```documents_attributes```
    """

    # noinspection PyArgumentList
    def __init__(self, declaration_items_attributes, invoice_reference=None, invoice_reference_text=None, currency=None, remark=None, declaration_text=None, declaration_charges_attributes=None, declaration_documents_attributes=None):
        self.__set_invoice_reference(invoice_reference)
        self.__set_invoice_reference_text(invoice_reference_text)
        self.__set_currency(currency)
        self.__set_remark(remark)
        self.__set_declaration_text(declaration_text)
        self.__set_declaration_items_attributes(declaration_items_attributes)
        self.__set_declaration_charges_attributes(declaration_charges_attributes)
        self.__set_declaration_documents_attributes(declaration_documents_attributes)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['invoice_reference'] = d.get('invoice_reference')
        v['invoice_reference_text'] = d.get('invoice_reference_text')
        v['currency'] = d.get('currency')
        v['remark'] = d.get('remark')
        v['declaration_text'] = d.get('declaration_text')
        v['declaration_items_attributes'] = [OrderDeclaration_AttributesDeclaration_Items_AttributesItem.from_dict(item) for item in d.get('declaration_items_attributes')]
        v['declaration_charges_attributes'] = [OrderDeclaration_AttributesDeclaration_Charges_AttributesItem.from_dict(item) for item in d.get('declaration_charges_attributes')]
        v['declaration_documents_attributes'] = [OrderDeclaration_AttributesDeclaration_Documents_AttributesItem.from_dict(item) for item in d.get('declaration_documents_attributes')]
        return OrderDeclaration_Attributes(**v)

    def as_dict(self):
        return dict(
            invoice_reference=self.__invoice_reference,
            invoice_reference_text=self.__invoice_reference_text,
            currency=self.__currency,
            remark=self.__remark,
            declaration_text=self.__declaration_text,
            declaration_items_attributes=[item.as_dict() for item in self.__declaration_items_attributes] if self.__declaration_items_attributes is not None else None,
            declaration_charges_attributes=[item.as_dict() for item in self.__declaration_charges_attributes] if self.__declaration_charges_attributes is not None else None,
            declaration_documents_attributes=[item.as_dict() for item in self.__declaration_documents_attributes] if self.__declaration_documents_attributes is not None else None
        )


# noinspection PyPep8Naming
class OrderOptions(object):

    __label_format: Optional[OrderOptionsLabel_Format] = None

    def __get_label_format(self):
        return self.__label_format

    def __set_label_format(self, label_format):
        if not (label_format in ['label_printer', 'a4'] or label_format is None):
            raise Exception(f'Cannot set field OrderOptionsLabel_Format.label_format to {repr(label_format)}')

        self.__label_format = label_format

    label_format = property(__get_label_format, __set_label_format)
    """
    The response includes a link to the goods labels. The link will be empty until the shipment is booked in Cargoson. You can choose the format of those labels with this option. 
    **a4** => up to four A6 labels per one A4 page. 
    **label_printer** => one label per page in the size of 4x6 inches (10.16 x 15.24 cm, which is close to the A6 format.)
    """

    __direct_booking_service_id: Optional[int] = None

    def __get_direct_booking_service_id(self):
        return self.__direct_booking_service_id

    def __set_direct_booking_service_id(self, direct_booking_service_id):
        if not (isinstance(direct_booking_service_id, int) or direct_booking_service_id is None):
            raise Exception(f'Cannot set field "direct_booking_service_id" (type int) to {repr(direct_booking_service_id)}')

        self.__direct_booking_service_id = direct_booking_service_id

    direct_booking_service_id = property(__get_direct_booking_service_id, __set_direct_booking_service_id)
    """
    If you wish to submit the booking immediately, you can enter the ID of the desired carrier's service. You can request the service IDs from Cargoson support.
    """

    __create_incomplete_shipment: Optional[bool] = None

    def __get_create_incomplete_shipment(self):
        return self.__create_incomplete_shipment

    def __set_create_incomplete_shipment(self, create_incomplete_shipment):
        if not (isinstance(create_incomplete_shipment, bool) or create_incomplete_shipment is None):
            raise Exception(f'Cannot set field "create_incomplete_shipment" (type bool) to {repr(create_incomplete_shipment)}')

        self.__create_incomplete_shipment = create_incomplete_shipment

    create_incomplete_shipment = property(__get_create_incomplete_shipment, __set_create_incomplete_shipment)
    """
    Indicates if you want the shipment to be saved for later editing even if booking itself fails
    """

    __automated_booking: Optional[bool] = None

    def __get_automated_booking(self):
        return self.__automated_booking

    def __set_automated_booking(self, automated_booking):
        if not (isinstance(automated_booking, bool) or automated_booking is None):
            raise Exception(f'Cannot set field "automated_booking" (type bool) to {repr(automated_booking)}')

        self.__automated_booking = automated_booking

    automated_booking = property(__get_automated_booking, __set_automated_booking)
    """
    Indicates if you want the shipment to be automatically booked based on rules defined in Cargoson by the user
    """

    __save_collection_address: Optional[bool] = None

    def __get_save_collection_address(self):
        return self.__save_collection_address

    def __set_save_collection_address(self, save_collection_address):
        if not (isinstance(save_collection_address, bool) or save_collection_address is None):
            raise Exception(f'Cannot set field "save_collection_address" (type bool) to {repr(save_collection_address)}')

        self.__save_collection_address = save_collection_address

    save_collection_address = property(__get_save_collection_address, __set_save_collection_address)
    """
    Indicates if you want to save the collection address in Cargoson's address book for later use
    """

    __save_delivery_address: Optional[bool] = None

    def __get_save_delivery_address(self):
        return self.__save_delivery_address

    def __set_save_delivery_address(self, save_delivery_address):
        if not (isinstance(save_delivery_address, bool) or save_delivery_address is None):
            raise Exception(f'Cannot set field "save_delivery_address" (type bool) to {repr(save_delivery_address)}')

        self.__save_delivery_address = save_delivery_address

    save_delivery_address = property(__get_save_delivery_address, __set_save_delivery_address)
    """
    Indicates if you want to save the delivery address in Cargoson's address book for later use
    """

    __parcel_machine_reference: Optional[str] = None

    def __get_parcel_machine_reference(self):
        return self.__parcel_machine_reference

    def __set_parcel_machine_reference(self, parcel_machine_reference):
        if not (isinstance(parcel_machine_reference, str) or parcel_machine_reference is None):
            raise Exception(f'Cannot set field "parcel_machine_reference" (type str) to {repr(parcel_machine_reference)}')

        self.__parcel_machine_reference = parcel_machine_reference

    parcel_machine_reference = property(__get_parcel_machine_reference, __set_parcel_machine_reference)
    """
    If ```direct_booking_service_id``` was defined, and the service id is for a parcel machine service, you can define the desired parcel machine here. If the service is a parcel machine service but this element is not defined, the closest parcel machine to the delivery address will be selected. You can request the desired parcel machine references from Cargoson support. Do not use if the ```direct_booking_service_id``` was not used or is not a parcel machine service ID:
    """

    # noinspection PyArgumentList
    def __init__(self, label_format=None, direct_booking_service_id=None, create_incomplete_shipment=None, automated_booking=None, save_collection_address=None, save_delivery_address=None, parcel_machine_reference=None):
        self.__set_label_format(label_format)
        self.__set_direct_booking_service_id(direct_booking_service_id)
        self.__set_create_incomplete_shipment(create_incomplete_shipment)
        self.__set_automated_booking(automated_booking)
        self.__set_save_collection_address(save_collection_address)
        self.__set_save_delivery_address(save_delivery_address)
        self.__set_parcel_machine_reference(parcel_machine_reference)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['label_format'] = d.get('label_format')
        v['direct_booking_service_id'] = d.get('direct_booking_service_id')
        v['create_incomplete_shipment'] = d.get('create_incomplete_shipment')
        v['automated_booking'] = d.get('automated_booking')
        v['save_collection_address'] = d.get('save_collection_address')
        v['save_delivery_address'] = d.get('save_delivery_address')
        v['parcel_machine_reference'] = d.get('parcel_machine_reference')
        return OrderOptions(**v)

    def as_dict(self):
        return dict(
            label_format=self.__label_format,
            direct_booking_service_id=self.__direct_booking_service_id,
            create_incomplete_shipment=self.__create_incomplete_shipment,
            automated_booking=self.__automated_booking,
            save_collection_address=self.__save_collection_address,
            save_delivery_address=self.__save_delivery_address,
            parcel_machine_reference=self.__parcel_machine_reference
        )


# noinspection PyPep8Naming
class OrderOffer(object):

    __total_price: Optional[float] = None

    def __get_total_price(self):
        return self.__total_price

    def __set_total_price(self, total_price):
        if not (isinstance(total_price, float) or isinstance(total_price, int) or total_price is None):
            raise Exception(f'Cannot set field "total_price" (type float) to {repr(total_price)}')

        self.__total_price = total_price

    total_price = property(__get_total_price, __set_total_price)
    """
    Price for the shipment that has been previously agreed upon with carrier
    """

    __currency: Optional[str] = None

    def __get_currency(self):
        return self.__currency

    def __set_currency(self, currency):
        if not (isinstance(currency, str) or currency is None):
            raise Exception(f'Cannot set field "currency" (type str) to {repr(currency)}')

        self.__currency = currency

    currency = property(__get_currency, __set_currency)
    """
    Currency of agreed price. Defaults to user's company's currency if not provided
    """

    # noinspection PyArgumentList
    def __init__(self, total_price, currency=None):
        self.__set_total_price(total_price)
        self.__set_currency(currency)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['total_price'] = d.get('total_price')
        v['currency'] = d.get('currency')
        return OrderOffer(**v)

    def as_dict(self):
        return dict(
            total_price=self.__total_price,
            currency=self.__currency
        )


# noinspection PyPep8Naming
class OrderRows_AttributesItem(object):
    """
    Array of goods rows, with each row consisting of the following 7 (or less) key-value pairs and an array of ADR rows (not required)
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

    __package_type: Optional[OrderRows_AttributesItemPackage_Type] = None

    def __get_package_type(self):
        return self.__package_type

    def __set_package_type(self, package_type):
        if not (package_type in ['EUR', 'CTN', 'FIN', 'HPL', 'QPL', 'LOAD', 'PLD', 'PXL', 'PLL', 'TBE', 'CLL', 'RLL', '20DC', '40DC', '40HC'] or package_type is None):
            raise Exception(f'Cannot set field OrderRows_AttributesItemPackage_Type.package_type to {repr(package_type)}')

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
    Row area in loading meters (ex.: 1 EUR pallet = 0.4 LDM)
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

    __adr_rows_attributes: Optional[List["OrderRows_AttributesItemAdr_Rows_AttributesItem"]] = []

    def __get_adr_rows_attributes(self):
        return self.__adr_rows_attributes

    def __set_adr_rows_attributes(self, adr_rows_attributes):
        if not (isinstance(adr_rows_attributes, list) or adr_rows_attributes is None):
            raise Exception(f'Cannot set field List["OrderRows_AttributesItemAdr_Rows_AttributesItem"].adr_rows_attributes to {repr(adr_rows_attributes)}')

        self.__adr_rows_attributes = adr_rows_attributes

    adr_rows_attributes = property(__get_adr_rows_attributes, __set_adr_rows_attributes)
    """
    Array of dangerous goods rows that are included in this goods row, with each row consisting of the following 5 (or less) key-value pairs
    """

    # noinspection PyArgumentList
    def __init__(self, quantity=None, package_type=None, weight=None, length=None, width=None, height=None, cbm=None, ldm=None, description=None, adr_rows_attributes=None):
        self.__set_quantity(quantity)
        self.__set_package_type(package_type)
        self.__set_weight(weight)
        self.__set_length(length)
        self.__set_width(width)
        self.__set_height(height)
        self.__set_cbm(cbm)
        self.__set_ldm(ldm)
        self.__set_description(description)
        self.__set_adr_rows_attributes(adr_rows_attributes)

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
        v['adr_rows_attributes'] = [OrderRows_AttributesItemAdr_Rows_AttributesItem.from_dict(item) for item in d.get('adr_rows_attributes')]
        return OrderRows_AttributesItem(**v)

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
            description=self.__description,
            adr_rows_attributes=[item.as_dict() for item in self.__adr_rows_attributes] if self.__adr_rows_attributes is not None else None
        )


# noinspection PyPep8Naming
class OrderDocuments_AttributesItem(object):
    """
    Array of files that will be attached to the shipment
    """

    __category: Optional[OrderDocuments_AttributesItemCategory] = None

    def __get_category(self):
        return self.__category

    def __set_category(self, category):
        if not (category in ['goods_invoice', 'package_list', 'cmr', 'waybill', 'bol', 'transportation_invoice', 'pod', 'labels', 'other'] or category is None):
            raise Exception(f'Cannot set field OrderDocuments_AttributesItemCategory.category to {repr(category)}')

        self.__category = category

    category = property(__get_category, __set_category)
    """
    Type of the document selected from the predefined document types
    """

    __filename: Optional[str] = None

    def __get_filename(self):
        return self.__filename

    def __set_filename(self, filename):
        if not (isinstance(filename, str) or filename is None):
            raise Exception(f'Cannot set field "filename" (type str) to {repr(filename)}')

        self.__filename = filename

    filename = property(__get_filename, __set_filename)
    """
    File name with extension
    """

    __annex: Optional[str] = None

    def __get_annex(self):
        return self.__annex

    def __set_annex(self, annex):
        if not (isinstance(annex, str) or annex is None):
            raise Exception(f'Cannot set field "annex" (type str) to {repr(annex)}')

        self.__annex = annex

    annex = property(__get_annex, __set_annex)
    """
    File content in Base64 encoded string
    """

    # noinspection PyArgumentList
    def __init__(self, category=None, filename=None, annex=None):
        self.__set_category(category)
        self.__set_filename(filename)
        self.__set_annex(annex)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['category'] = d.get('category')
        v['filename'] = d.get('filename')
        v['annex'] = d.get('annex')
        return OrderDocuments_AttributesItem(**v)

    def as_dict(self):
        return dict(
            category=self.__category,
            filename=self.__filename,
            annex=self.__annex
        )


# noinspection PyPep8Naming
class OrderIncoterm_Code(enum.Enum):
    """
    International Commercial Terms are a series of pre-defined commercial terms published by the International Chamber of Commerce (ICC) relating to international commercial law
    """

    EXW = 'EXW'
    FCA = 'FCA'
    CPT = 'CPT'
    CIP = 'CIP'
    DAT = 'DAT'
    DPU = 'DPU'
    DAP = 'DAP'
    DDP = 'DDP'
    FAS = 'FAS'
    FOB = 'FOB'
    CFR = 'CFR'
    CIF = 'CIF'

    def as_dict(self):
        return self.value

    @staticmethod
    def from_dict(value):
        return OrderIncoterm_Code(value)


# noinspection PyPep8Naming
class Order(object):

    __customer_reference: Optional[str] = None

    def __get_customer_reference(self):
        return self.__customer_reference

    def __set_customer_reference(self, customer_reference):
        if not (isinstance(customer_reference, str) or customer_reference is None):
            raise Exception(f'Cannot set field "customer_reference" (type str) to {repr(customer_reference)}')

        self.__customer_reference = customer_reference

    customer_reference = property(__get_customer_reference, __set_customer_reference)
    """
    Internal shipment reference
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

    __collection_time_from: Optional[str] = None

    def __get_collection_time_from(self):
        return self.__collection_time_from

    def __set_collection_time_from(self, collection_time_from):
        if not (isinstance(collection_time_from, str) or collection_time_from is None):
            raise Exception(f'Cannot set field "collection_time_from" (type str) to {repr(collection_time_from)}')

        self.__collection_time_from = collection_time_from

    collection_time_from = property(__get_collection_time_from, __set_collection_time_from)
    """
    Must be before collection time to. Cannot be less than current local time if collection date is set to today
    """

    __collection_time_to: Optional[str] = None

    def __get_collection_time_to(self):
        return self.__collection_time_to

    def __set_collection_time_to(self, collection_time_to):
        if not (isinstance(collection_time_to, str) or collection_time_to is None):
            raise Exception(f'Cannot set field "collection_time_to" (type str) to {repr(collection_time_to)}')

        self.__collection_time_to = collection_time_to

    collection_time_to = property(__get_collection_time_to, __set_collection_time_to)
    """
    Must be after collection time from
    """

    __delivery_date: Optional[str] = None

    def __get_delivery_date(self):
        return self.__delivery_date

    def __set_delivery_date(self, delivery_date):
        if not (isinstance(delivery_date, str) or delivery_date is None):
            raise Exception(f'Cannot set field "delivery_date" (type str) to {repr(delivery_date)}')

        self.__delivery_date = delivery_date

    delivery_date = property(__get_delivery_date, __set_delivery_date)
    """
    Desired delivery date. Must be equal to the collection date or later
    """

    __delivery_time_from: Optional[str] = None

    def __get_delivery_time_from(self):
        return self.__delivery_time_from

    def __set_delivery_time_from(self, delivery_time_from):
        if not (isinstance(delivery_time_from, str) or delivery_time_from is None):
            raise Exception(f'Cannot set field "delivery_time_from" (type str) to {repr(delivery_time_from)}')

        self.__delivery_time_from = delivery_time_from

    delivery_time_from = property(__get_delivery_time_from, __set_delivery_time_from)
    """
    Must be before delivery time to. If collection and delivery dates match then must be after collection time to
    """

    __delivery_time_to: Optional[str] = None

    def __get_delivery_time_to(self):
        return self.__delivery_time_to

    def __set_delivery_time_to(self, delivery_time_to):
        if not (isinstance(delivery_time_to, str) or delivery_time_to is None):
            raise Exception(f'Cannot set field "delivery_time_to" (type str) to {repr(delivery_time_to)}')

        self.__delivery_time_to = delivery_time_to

    delivery_time_to = property(__get_delivery_time_to, __set_delivery_time_to)
    """
    Must be after delivery time from
    """

    __collection_company_name: Optional[str] = None

    def __get_collection_company_name(self):
        return self.__collection_company_name

    def __set_collection_company_name(self, collection_company_name):
        if not (isinstance(collection_company_name, str) or collection_company_name is None):
            raise Exception(f'Cannot set field "collection_company_name" (type str) to {repr(collection_company_name)}')

        self.__collection_company_name = collection_company_name

    collection_company_name = property(__get_collection_company_name, __set_collection_company_name)
    """
    The name of the company the goods are collected from
    """

    __collection_address_row_1: Optional[str] = None

    def __get_collection_address_row_1(self):
        return self.__collection_address_row_1

    def __set_collection_address_row_1(self, collection_address_row_1):
        if not (isinstance(collection_address_row_1, str) or collection_address_row_1 is None):
            raise Exception(f'Cannot set field "collection_address_row_1" (type str) to {repr(collection_address_row_1)}')

        self.__collection_address_row_1 = collection_address_row_1

    collection_address_row_1 = property(__get_collection_address_row_1, __set_collection_address_row_1)
    """
    Street, house number
    """

    __collection_address_row_2: Optional[str] = None

    def __get_collection_address_row_2(self):
        return self.__collection_address_row_2

    def __set_collection_address_row_2(self, collection_address_row_2):
        if not (isinstance(collection_address_row_2, str) or collection_address_row_2 is None):
            raise Exception(f'Cannot set field "collection_address_row_2" (type str) to {repr(collection_address_row_2)}')

        self.__collection_address_row_2 = collection_address_row_2

    collection_address_row_2 = property(__get_collection_address_row_2, __set_collection_address_row_2)
    """
    County, building, unit
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

    __collection_city: Optional[str] = None

    def __get_collection_city(self):
        return self.__collection_city

    def __set_collection_city(self, collection_city):
        if not (isinstance(collection_city, str) or collection_city is None):
            raise Exception(f'Cannot set field "collection_city" (type str) to {repr(collection_city)}')

        self.__collection_city = collection_city

    collection_city = property(__get_collection_city, __set_collection_city)
    """
    City, district, suburb, town or village
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

    __collection_contact_name: Optional[str] = None

    def __get_collection_contact_name(self):
        return self.__collection_contact_name

    def __set_collection_contact_name(self, collection_contact_name):
        if not (isinstance(collection_contact_name, str) or collection_contact_name is None):
            raise Exception(f'Cannot set field "collection_contact_name" (type str) to {repr(collection_contact_name)}')

        self.__collection_contact_name = collection_contact_name

    collection_contact_name = property(__get_collection_contact_name, __set_collection_contact_name)
    """
    The name of the person that the driver can contact
    """

    __collection_contact_phone: Optional[str] = None

    def __get_collection_contact_phone(self):
        return self.__collection_contact_phone

    def __set_collection_contact_phone(self, collection_contact_phone):
        if not (isinstance(collection_contact_phone, str) or collection_contact_phone is None):
            raise Exception(f'Cannot set field "collection_contact_phone" (type str) to {repr(collection_contact_phone)}')

        self.__collection_contact_phone = collection_contact_phone

    collection_contact_phone = property(__get_collection_contact_phone, __set_collection_contact_phone)
    """
    The phone number of the person that the driver can contact
    """

    __collection_contact_email: Optional[str] = None

    def __get_collection_contact_email(self):
        return self.__collection_contact_email

    def __set_collection_contact_email(self, collection_contact_email):
        if not (isinstance(collection_contact_email, str) or collection_contact_email is None):
            raise Exception(f'Cannot set field "collection_contact_email" (type str) to {repr(collection_contact_email)}')

        self.__collection_contact_email = collection_contact_email

    collection_contact_email = property(__get_collection_contact_email, __set_collection_contact_email)
    """
    The email of the person that the carrier can contact
    """

    __collection_comment: Optional[str] = None

    def __get_collection_comment(self):
        return self.__collection_comment

    def __set_collection_comment(self, collection_comment):
        if not (isinstance(collection_comment, str) or collection_comment is None):
            raise Exception(f'Cannot set field "collection_comment" (type str) to {repr(collection_comment)}')

        self.__collection_comment = collection_comment

    collection_comment = property(__get_collection_comment, __set_collection_comment)
    """
    Additional collection related information. (e.g., "Code to enter the gate is 1234")
    """

    __delivery_company_name: Optional[str] = None

    def __get_delivery_company_name(self):
        return self.__delivery_company_name

    def __set_delivery_company_name(self, delivery_company_name):
        if not (isinstance(delivery_company_name, str) or delivery_company_name is None):
            raise Exception(f'Cannot set field "delivery_company_name" (type str) to {repr(delivery_company_name)}')

        self.__delivery_company_name = delivery_company_name

    delivery_company_name = property(__get_delivery_company_name, __set_delivery_company_name)
    """
    The name of the company the goods are delivered to
    """

    __delivery_address_row_1: Optional[str] = None

    def __get_delivery_address_row_1(self):
        return self.__delivery_address_row_1

    def __set_delivery_address_row_1(self, delivery_address_row_1):
        if not (isinstance(delivery_address_row_1, str) or delivery_address_row_1 is None):
            raise Exception(f'Cannot set field "delivery_address_row_1" (type str) to {repr(delivery_address_row_1)}')

        self.__delivery_address_row_1 = delivery_address_row_1

    delivery_address_row_1 = property(__get_delivery_address_row_1, __set_delivery_address_row_1)
    """
    Street, house number
    """

    __delivery_address_row_2: Optional[str] = None

    def __get_delivery_address_row_2(self):
        return self.__delivery_address_row_2

    def __set_delivery_address_row_2(self, delivery_address_row_2):
        if not (isinstance(delivery_address_row_2, str) or delivery_address_row_2 is None):
            raise Exception(f'Cannot set field "delivery_address_row_2" (type str) to {repr(delivery_address_row_2)}')

        self.__delivery_address_row_2 = delivery_address_row_2

    delivery_address_row_2 = property(__get_delivery_address_row_2, __set_delivery_address_row_2)
    """
    County, building, unit
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

    __delivery_city: Optional[str] = None

    def __get_delivery_city(self):
        return self.__delivery_city

    def __set_delivery_city(self, delivery_city):
        if not (isinstance(delivery_city, str) or delivery_city is None):
            raise Exception(f'Cannot set field "delivery_city" (type str) to {repr(delivery_city)}')

        self.__delivery_city = delivery_city

    delivery_city = property(__get_delivery_city, __set_delivery_city)
    """
    City, district, suburb, town or village
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

    __delivery_contact_name: Optional[str] = None

    def __get_delivery_contact_name(self):
        return self.__delivery_contact_name

    def __set_delivery_contact_name(self, delivery_contact_name):
        if not (isinstance(delivery_contact_name, str) or delivery_contact_name is None):
            raise Exception(f'Cannot set field "delivery_contact_name" (type str) to {repr(delivery_contact_name)}')

        self.__delivery_contact_name = delivery_contact_name

    delivery_contact_name = property(__get_delivery_contact_name, __set_delivery_contact_name)
    """
    The name of the person that the driver can contact
    """

    __delivery_contact_phone: Optional[str] = None

    def __get_delivery_contact_phone(self):
        return self.__delivery_contact_phone

    def __set_delivery_contact_phone(self, delivery_contact_phone):
        if not (isinstance(delivery_contact_phone, str) or delivery_contact_phone is None):
            raise Exception(f'Cannot set field "delivery_contact_phone" (type str) to {repr(delivery_contact_phone)}')

        self.__delivery_contact_phone = delivery_contact_phone

    delivery_contact_phone = property(__get_delivery_contact_phone, __set_delivery_contact_phone)
    """
    The phone number of the person that the driver can contact
    """

    __delivery_contact_email: Optional[str] = None

    def __get_delivery_contact_email(self):
        return self.__delivery_contact_email

    def __set_delivery_contact_email(self, delivery_contact_email):
        if not (isinstance(delivery_contact_email, str) or delivery_contact_email is None):
            raise Exception(f'Cannot set field "delivery_contact_email" (type str) to {repr(delivery_contact_email)}')

        self.__delivery_contact_email = delivery_contact_email

    delivery_contact_email = property(__get_delivery_contact_email, __set_delivery_contact_email)
    """
    The email of the person that the carrier can contact
    """

    __delivery_comment: Optional[str] = None

    def __get_delivery_comment(self):
        return self.__delivery_comment

    def __set_delivery_comment(self, delivery_comment):
        if not (isinstance(delivery_comment, str) or delivery_comment is None):
            raise Exception(f'Cannot set field "delivery_comment" (type str) to {repr(delivery_comment)}')

        self.__delivery_comment = delivery_comment

    delivery_comment = property(__get_delivery_comment, __set_delivery_comment)
    """
    Additional delivery related information. (e.g., "Code to enter the gate is 1234")
    """

    __goods_value: Optional[float] = None

    def __get_goods_value(self):
        return self.__goods_value

    def __set_goods_value(self, goods_value):
        if not (isinstance(goods_value, float) or isinstance(goods_value, int) or goods_value is None):
            raise Exception(f'Cannot set field "goods_value" (type float) to {repr(goods_value)}')

        self.__goods_value = goods_value

    goods_value = property(__get_goods_value, __set_goods_value)
    """
    The monetary value of the goods
    """

    __goods_value_currency: Optional[str] = None

    def __get_goods_value_currency(self):
        return self.__goods_value_currency

    def __set_goods_value_currency(self, goods_value_currency):
        if not (isinstance(goods_value_currency, str) or goods_value_currency is None):
            raise Exception(f'Cannot set field "goods_value_currency" (type str) to {repr(goods_value_currency)}')

        self.__goods_value_currency = goods_value_currency

    goods_value_currency = property(__get_goods_value_currency, __set_goods_value_currency)
    """
    Three-letter currency code (ISO 4217)
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

    __temp_min: Optional[int] = None

    def __get_temp_min(self):
        return self.__temp_min

    def __set_temp_min(self, temp_min):
        if not (isinstance(temp_min, int) or temp_min is None):
            raise Exception(f'Cannot set field "temp_min" (type int) to {repr(temp_min)}')

        self.__temp_min = temp_min

    temp_min = property(__get_temp_min, __set_temp_min)
    """
    Minimum temperature limit
    """

    __temp_max: Optional[int] = None

    def __get_temp_max(self):
        return self.__temp_max

    def __set_temp_max(self, temp_max):
        if not (isinstance(temp_max, int) or temp_max is None):
            raise Exception(f'Cannot set field "temp_max" (type int) to {repr(temp_max)}')

        self.__temp_max = temp_max

    temp_max = property(__get_temp_max, __set_temp_max)
    """
    Maximum temperature limit
    """

    __incoterm_code: Optional[OrderIncoterm_Code] = None

    def __get_incoterm_code(self):
        return self.__incoterm_code

    def __set_incoterm_code(self, incoterm_code):
        if not (incoterm_code in ['EXW', 'FCA', 'CPT', 'CIP', 'DAT', 'DPU', 'DAP', 'DDP', 'FAS', 'FOB', 'CFR', 'CIF'] or incoterm_code is None):
            raise Exception(f'Cannot set field OrderIncoterm_Code.incoterm_code to {repr(incoterm_code)}')

        self.__incoterm_code = incoterm_code

    incoterm_code = property(__get_incoterm_code, __set_incoterm_code)
    """
    International Commercial Terms are a series of pre-defined commercial terms published by the International Chamber of Commerce (ICC) relating to international commercial law
    """

    __incoterm_city: Optional[str] = None

    def __get_incoterm_city(self):
        return self.__incoterm_city

    def __set_incoterm_city(self, incoterm_city):
        if not (isinstance(incoterm_city, str) or incoterm_city is None):
            raise Exception(f'Cannot set field "incoterm_city" (type str) to {repr(incoterm_city)}')

        self.__incoterm_city = incoterm_city

    incoterm_city = property(__get_incoterm_city, __set_incoterm_city)
    """
    Incoterm city
    """

    __customer_remark: Optional[str] = None

    def __get_customer_remark(self):
        return self.__customer_remark

    def __set_customer_remark(self, customer_remark):
        if not (isinstance(customer_remark, str) or customer_remark is None):
            raise Exception(f'Cannot set field "customer_remark" (type str) to {repr(customer_remark)}')

        self.__customer_remark = customer_remark

    customer_remark = property(__get_customer_remark, __set_customer_remark)
    """
    Important additional information for the carrier
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

    __documents_attributes: Optional[List["OrderDocuments_AttributesItem"]] = []

    def __get_documents_attributes(self):
        return self.__documents_attributes

    def __set_documents_attributes(self, documents_attributes):
        if not (isinstance(documents_attributes, list) or documents_attributes is None):
            raise Exception(f'Cannot set field List["OrderDocuments_AttributesItem"].documents_attributes to {repr(documents_attributes)}')

        self.__documents_attributes = documents_attributes

    documents_attributes = property(__get_documents_attributes, __set_documents_attributes)
    """
    Array of files that will be attached to the shipment
    """

    __rows_attributes: Optional[List["OrderRows_AttributesItem"]] = []

    def __get_rows_attributes(self):
        return self.__rows_attributes

    def __set_rows_attributes(self, rows_attributes):
        if not (isinstance(rows_attributes, list) or rows_attributes is None):
            raise Exception(f'Cannot set field List["OrderRows_AttributesItem"].rows_attributes to {repr(rows_attributes)}')

        self.__rows_attributes = rows_attributes

    rows_attributes = property(__get_rows_attributes, __set_rows_attributes)
    """
    Array of goods rows, with each row consisting of the following 7 (or less) key-value pairs and an array of ADR rows (not required)
    """

    __offer: Optional[OrderOffer] = None

    def __get_offer(self):
        return self.__offer

    def __set_offer(self, offer):
        if not (isinstance(offer, OrderOffer) or offer is None):
            raise Exception(f'Cannot set field OrderOffer.offer to {repr(offer)}')

        self.__offer = offer

    offer = property(__get_offer, __set_offer)

    __options: Optional[OrderOptions] = None

    def __get_options(self):
        return self.__options

    def __set_options(self, options):
        if not (isinstance(options, OrderOptions) or options is None):
            raise Exception(f'Cannot set field OrderOptions.options to {repr(options)}')

        self.__options = options

    options = property(__get_options, __set_options)

    __declaration_attributes: Optional[OrderDeclaration_Attributes] = None

    def __get_declaration_attributes(self):
        return self.__declaration_attributes

    def __set_declaration_attributes(self, declaration_attributes):
        if not (isinstance(declaration_attributes, OrderDeclaration_Attributes) or declaration_attributes is None):
            raise Exception(f'Cannot set field OrderDeclaration_Attributes.declaration_attributes to {repr(declaration_attributes)}')

        self.__declaration_attributes = declaration_attributes

    declaration_attributes = property(__get_declaration_attributes, __set_declaration_attributes)
    """
    If the shipment requires a customs declaration, these fields should be filled
    """

    # noinspection PyArgumentList
    def __init__(self, collection_date, collection_postcode, collection_country, delivery_postcode, delivery_country, rows_attributes, customer_reference=None, collection_time_from=None, collection_time_to=None, delivery_date=None, delivery_time_from=None, delivery_time_to=None, collection_company_name=None, collection_address_row_1=None, collection_address_row_2=None, collection_city=None, collection_contact_name=None, collection_contact_phone=None, collection_contact_email=None, collection_comment=None, delivery_company_name=None, delivery_address_row_1=None, delivery_address_row_2=None, delivery_city=None, delivery_contact_name=None, delivery_contact_phone=None, delivery_contact_email=None, delivery_comment=None, goods_value=None, goods_value_currency=None, frigo=None, temp_min=None, temp_max=None, incoterm_code=None, incoterm_city=None, customer_remark=None, collection_with_tail_lift=None, collection_prenotification=None, delivery_with_tail_lift=None, delivery_prenotification=None, delivery_return_document=None, delivery_to_private_person=None, documents_attributes=None, offer=None, options=None, declaration_attributes=None):
        self.__set_customer_reference(customer_reference)
        self.__set_collection_date(collection_date)
        self.__set_collection_time_from(collection_time_from)
        self.__set_collection_time_to(collection_time_to)
        self.__set_delivery_date(delivery_date)
        self.__set_delivery_time_from(delivery_time_from)
        self.__set_delivery_time_to(delivery_time_to)
        self.__set_collection_company_name(collection_company_name)
        self.__set_collection_address_row_1(collection_address_row_1)
        self.__set_collection_address_row_2(collection_address_row_2)
        self.__set_collection_postcode(collection_postcode)
        self.__set_collection_city(collection_city)
        self.__set_collection_country(collection_country)
        self.__set_collection_contact_name(collection_contact_name)
        self.__set_collection_contact_phone(collection_contact_phone)
        self.__set_collection_contact_email(collection_contact_email)
        self.__set_collection_comment(collection_comment)
        self.__set_delivery_company_name(delivery_company_name)
        self.__set_delivery_address_row_1(delivery_address_row_1)
        self.__set_delivery_address_row_2(delivery_address_row_2)
        self.__set_delivery_postcode(delivery_postcode)
        self.__set_delivery_city(delivery_city)
        self.__set_delivery_country(delivery_country)
        self.__set_delivery_contact_name(delivery_contact_name)
        self.__set_delivery_contact_phone(delivery_contact_phone)
        self.__set_delivery_contact_email(delivery_contact_email)
        self.__set_delivery_comment(delivery_comment)
        self.__set_goods_value(goods_value)
        self.__set_goods_value_currency(goods_value_currency)
        self.__set_frigo(frigo)
        self.__set_temp_min(temp_min)
        self.__set_temp_max(temp_max)
        self.__set_incoterm_code(incoterm_code)
        self.__set_incoterm_city(incoterm_city)
        self.__set_customer_remark(customer_remark)
        self.__set_collection_with_tail_lift(collection_with_tail_lift)
        self.__set_collection_prenotification(collection_prenotification)
        self.__set_delivery_with_tail_lift(delivery_with_tail_lift)
        self.__set_delivery_prenotification(delivery_prenotification)
        self.__set_delivery_return_document(delivery_return_document)
        self.__set_delivery_to_private_person(delivery_to_private_person)
        self.__set_documents_attributes(documents_attributes)
        self.__set_rows_attributes(rows_attributes)
        self.__set_offer(offer)
        self.__set_options(options)
        self.__set_declaration_attributes(declaration_attributes)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['customer_reference'] = d.get('customer_reference')
        v['collection_date'] = d.get('collection_date')
        v['collection_time_from'] = d.get('collection_time_from')
        v['collection_time_to'] = d.get('collection_time_to')
        v['delivery_date'] = d.get('delivery_date')
        v['delivery_time_from'] = d.get('delivery_time_from')
        v['delivery_time_to'] = d.get('delivery_time_to')
        v['collection_company_name'] = d.get('collection_company_name')
        v['collection_address_row_1'] = d.get('collection_address_row_1')
        v['collection_address_row_2'] = d.get('collection_address_row_2')
        v['collection_postcode'] = d.get('collection_postcode')
        v['collection_city'] = d.get('collection_city')
        v['collection_country'] = d.get('collection_country')
        v['collection_contact_name'] = d.get('collection_contact_name')
        v['collection_contact_phone'] = d.get('collection_contact_phone')
        v['collection_contact_email'] = d.get('collection_contact_email')
        v['collection_comment'] = d.get('collection_comment')
        v['delivery_company_name'] = d.get('delivery_company_name')
        v['delivery_address_row_1'] = d.get('delivery_address_row_1')
        v['delivery_address_row_2'] = d.get('delivery_address_row_2')
        v['delivery_postcode'] = d.get('delivery_postcode')
        v['delivery_city'] = d.get('delivery_city')
        v['delivery_country'] = d.get('delivery_country')
        v['delivery_contact_name'] = d.get('delivery_contact_name')
        v['delivery_contact_phone'] = d.get('delivery_contact_phone')
        v['delivery_contact_email'] = d.get('delivery_contact_email')
        v['delivery_comment'] = d.get('delivery_comment')
        v['goods_value'] = d.get('goods_value')
        v['goods_value_currency'] = d.get('goods_value_currency')
        v['frigo'] = d.get('frigo')
        v['temp_min'] = d.get('temp_min')
        v['temp_max'] = d.get('temp_max')
        v['incoterm_code'] = d.get('incoterm_code')
        v['incoterm_city'] = d.get('incoterm_city')
        v['customer_remark'] = d.get('customer_remark')
        v['collection_with_tail_lift'] = d.get('collection_with_tail_lift')
        v['collection_prenotification'] = d.get('collection_prenotification')
        v['delivery_with_tail_lift'] = d.get('delivery_with_tail_lift')
        v['delivery_prenotification'] = d.get('delivery_prenotification')
        v['delivery_return_document'] = d.get('delivery_return_document')
        v['delivery_to_private_person'] = d.get('delivery_to_private_person')
        v['documents_attributes'] = [OrderDocuments_AttributesItem.from_dict(item) for item in d.get('documents_attributes')]
        v['rows_attributes'] = [OrderRows_AttributesItem.from_dict(item) for item in d.get('rows_attributes')]
        v['offer'] = OrderOffer.from_dict(d.get('offer'))
        v['options'] = OrderOptions.from_dict(d.get('options'))
        v['declaration_attributes'] = OrderDeclaration_Attributes.from_dict(d.get('declaration_attributes'))
        return Order(**v)

    def as_dict(self):
        return dict(
            customer_reference=self.__customer_reference,
            collection_date=self.__collection_date,
            collection_time_from=self.__collection_time_from,
            collection_time_to=self.__collection_time_to,
            delivery_date=self.__delivery_date,
            delivery_time_from=self.__delivery_time_from,
            delivery_time_to=self.__delivery_time_to,
            collection_company_name=self.__collection_company_name,
            collection_address_row_1=self.__collection_address_row_1,
            collection_address_row_2=self.__collection_address_row_2,
            collection_postcode=self.__collection_postcode,
            collection_city=self.__collection_city,
            collection_country=self.__collection_country,
            collection_contact_name=self.__collection_contact_name,
            collection_contact_phone=self.__collection_contact_phone,
            collection_contact_email=self.__collection_contact_email,
            collection_comment=self.__collection_comment,
            delivery_company_name=self.__delivery_company_name,
            delivery_address_row_1=self.__delivery_address_row_1,
            delivery_address_row_2=self.__delivery_address_row_2,
            delivery_postcode=self.__delivery_postcode,
            delivery_city=self.__delivery_city,
            delivery_country=self.__delivery_country,
            delivery_contact_name=self.__delivery_contact_name,
            delivery_contact_phone=self.__delivery_contact_phone,
            delivery_contact_email=self.__delivery_contact_email,
            delivery_comment=self.__delivery_comment,
            goods_value=self.__goods_value,
            goods_value_currency=self.__goods_value_currency,
            frigo=self.__frigo,
            temp_min=self.__temp_min,
            temp_max=self.__temp_max,
            incoterm_code=self.__incoterm_code,
            incoterm_city=self.__incoterm_city,
            customer_remark=self.__customer_remark,
            collection_with_tail_lift=self.__collection_with_tail_lift,
            collection_prenotification=self.__collection_prenotification,
            delivery_with_tail_lift=self.__delivery_with_tail_lift,
            delivery_prenotification=self.__delivery_prenotification,
            delivery_return_document=self.__delivery_return_document,
            delivery_to_private_person=self.__delivery_to_private_person,
            documents_attributes=[item.as_dict() for item in self.__documents_attributes] if self.__documents_attributes is not None else None,
            rows_attributes=[item.as_dict() for item in self.__rows_attributes] if self.__rows_attributes is not None else None,
            offer=self.__offer.as_dict() if self.__offer is not None else None,
            options=self.__options.as_dict() if self.__options is not None else None,
            declaration_attributes=self.__declaration_attributes.as_dict() if self.__declaration_attributes is not None else None
        )


