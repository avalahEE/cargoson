from typing import Optional


# noinspection PyPep8Naming
class EmissionsObjectDistancesSea(object):
    """
    Sea distance
    """

    __ship: Optional[float] = None

    def __get_ship(self):
        return self.__ship

    def __set_ship(self, ship):
        if not (isinstance(ship, float) or isinstance(ship, int) or ship is None):
            raise Exception(f'Cannot set field "ship" (type float) to {repr(ship)}')

        self.__ship = ship

    ship = property(__get_ship, __set_ship)
    """
    Ship distance
    """

    __truck: Optional[float] = None

    def __get_truck(self):
        return self.__truck

    def __set_truck(self, truck):
        if not (isinstance(truck, float) or isinstance(truck, int) or truck is None):
            raise Exception(f'Cannot set field "truck" (type float) to {repr(truck)}')

        self.__truck = truck

    truck = property(__get_truck, __set_truck)
    """
    Truck distance
    """

    # noinspection PyArgumentList
    def __init__(self, ship=None, truck=None):
        self.__set_ship(ship)
        self.__set_truck(truck)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['ship'] = d.get('ship')
        v['truck'] = d.get('truck')
        return EmissionsObjectDistancesSea(**v)

    def as_dict(self):
        return dict(
            ship=self.__ship,
            truck=self.__truck
        )


# noinspection PyPep8Naming
class EmissionsObjectDistancesCoordinates(object):
    """
    an object containing collection and delivery coordinates
    """

    __collection: Optional[list] = None

    def __get_collection(self):
        return self.__collection

    def __set_collection(self, collection):
        if not (isinstance(collection, list) or collection is None):
            raise Exception(f'Cannot set field "collection" (type list) to {repr(collection)}')

        self.__collection = collection

    collection = property(__get_collection, __set_collection)
    """
    Collection coordinates
    """

    __delivery: Optional[list] = None

    def __get_delivery(self):
        return self.__delivery

    def __set_delivery(self, delivery):
        if not (isinstance(delivery, list) or delivery is None):
            raise Exception(f'Cannot set field "delivery" (type list) to {repr(delivery)}')

        self.__delivery = delivery

    delivery = property(__get_delivery, __set_delivery)
    """
    Delivery coordinates
    """

    # noinspection PyArgumentList
    def __init__(self, collection=None, delivery=None):
        self.__set_collection(collection)
        self.__set_delivery(delivery)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['collection'] = d.get('collection')
        v['delivery'] = d.get('delivery')
        return EmissionsObjectDistancesCoordinates(**v)

    def as_dict(self):
        return dict(
            collection=self.__collection,
            delivery=self.__delivery
        )


# noinspection PyPep8Naming
class EmissionsObjectCo2E_Kg(object):
    """
    Expected CO2e emissions for different freight types
    """

    __road: Optional[str] = None

    def __get_road(self):
        return self.__road

    def __set_road(self, road):
        if not (isinstance(road, str) or road is None):
            raise Exception(f'Cannot set field "road" (type str) to {repr(road)}')

        self.__road = road

    road = property(__get_road, __set_road)
    """
    Road CO2e emissions in kg
    """

    __sea: Optional[str] = None

    def __get_sea(self):
        return self.__sea

    def __set_sea(self, sea):
        if not (isinstance(sea, str) or sea is None):
            raise Exception(f'Cannot set field "sea" (type str) to {repr(sea)}')

        self.__sea = sea

    sea = property(__get_sea, __set_sea)
    """
    Sea CO2e emissions in kg
    """

    __air: Optional[str] = None

    def __get_air(self):
        return self.__air

    def __set_air(self, air):
        if not (isinstance(air, str) or air is None):
            raise Exception(f'Cannot set field "air" (type str) to {repr(air)}')

        self.__air = air

    air = property(__get_air, __set_air)
    """
    Air CO2e emissions in kg
    """

    __rail: Optional[str] = None

    def __get_rail(self):
        return self.__rail

    def __set_rail(self, rail):
        if not (isinstance(rail, str) or rail is None):
            raise Exception(f'Cannot set field "rail" (type str) to {repr(rail)}')

        self.__rail = rail

    rail = property(__get_rail, __set_rail)
    """
    Rail CO2e emissions in kg
    """

    # noinspection PyArgumentList
    def __init__(self, road=None, sea=None, air=None, rail=None):
        self.__set_road(road)
        self.__set_sea(sea)
        self.__set_air(air)
        self.__set_rail(rail)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['road'] = d.get('road')
        v['sea'] = d.get('sea')
        v['air'] = d.get('air')
        v['rail'] = d.get('rail')
        return EmissionsObjectCo2E_Kg(**v)

    def as_dict(self):
        return dict(
            road=self.__road,
            sea=self.__sea,
            air=self.__air,
            rail=self.__rail
        )


# noinspection PyPep8Naming
class EmissionsObjectDistances(object):
    """
    an object containing shipment coordinates and distances
    """

    __coordinates: Optional[EmissionsObjectDistancesCoordinates] = None

    def __get_coordinates(self):
        return self.__coordinates

    def __set_coordinates(self, coordinates):
        if not (isinstance(coordinates, EmissionsObjectDistancesCoordinates) or coordinates is None):
            raise Exception(f'Cannot set field EmissionsObjectDistancesCoordinates.coordinates to {repr(coordinates)}')

        self.__coordinates = coordinates

    coordinates = property(__get_coordinates, __set_coordinates)
    """
    an object containing collection and delivery coordinates
    """

    __road: Optional[float] = None

    def __get_road(self):
        return self.__road

    def __set_road(self, road):
        if not (isinstance(road, float) or isinstance(road, int) or road is None):
            raise Exception(f'Cannot set field "road" (type float) to {repr(road)}')

        self.__road = road

    road = property(__get_road, __set_road)
    """
    Road distance
    """

    __sea: Optional[EmissionsObjectDistancesSea] = None

    def __get_sea(self):
        return self.__sea

    def __set_sea(self, sea):
        if not (isinstance(sea, EmissionsObjectDistancesSea) or sea is None):
            raise Exception(f'Cannot set field EmissionsObjectDistancesSea.sea to {repr(sea)}')

        self.__sea = sea

    sea = property(__get_sea, __set_sea)
    """
    Sea distance
    """

    __gcd: Optional[float] = None

    def __get_gcd(self):
        return self.__gcd

    def __set_gcd(self, gcd):
        if not (isinstance(gcd, float) or isinstance(gcd, int) or gcd is None):
            raise Exception(f'Cannot set field "gcd" (type float) to {repr(gcd)}')

        self.__gcd = gcd

    gcd = property(__get_gcd, __set_gcd)
    """
    Great Circle distance
    """

    # noinspection PyArgumentList
    def __init__(self, coordinates=None, road=None, sea=None, gcd=None):
        self.__set_coordinates(coordinates)
        self.__set_road(road)
        self.__set_sea(sea)
        self.__set_gcd(gcd)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['coordinates'] = EmissionsObjectDistancesCoordinates.from_dict(d.get('coordinates'))
        v['road'] = d.get('road')
        v['sea'] = EmissionsObjectDistancesSea.from_dict(d.get('sea'))
        v['gcd'] = d.get('gcd')
        return EmissionsObjectDistances(**v)

    def as_dict(self):
        return dict(
            coordinates=self.__coordinates.as_dict() if self.__coordinates is not None else None,
            road=self.__road,
            sea=self.__sea.as_dict() if self.__sea is not None else None,
            gcd=self.__gcd
        )


# noinspection PyPep8Naming
class EmissionsObject(object):
    """
    an object containing shipment coordinates and co2e emissions
    """

    __distances: Optional[EmissionsObjectDistances] = None

    def __get_distances(self):
        return self.__distances

    def __set_distances(self, distances):
        if not (isinstance(distances, EmissionsObjectDistances) or distances is None):
            raise Exception(f'Cannot set field EmissionsObjectDistances.distances to {repr(distances)}')

        self.__distances = distances

    distances = property(__get_distances, __set_distances)
    """
    an object containing shipment coordinates and distances
    """

    __co2e_kg: Optional[EmissionsObjectCo2E_Kg] = None

    def __get_co2e_kg(self):
        return self.__co2e_kg

    def __set_co2e_kg(self, co2e_kg):
        if not (isinstance(co2e_kg, EmissionsObjectCo2E_Kg) or co2e_kg is None):
            raise Exception(f'Cannot set field EmissionsObjectCo2E_Kg.co2e_kg to {repr(co2e_kg)}')

        self.__co2e_kg = co2e_kg

    co2e_kg = property(__get_co2e_kg, __set_co2e_kg)
    """
    Expected CO2e emissions for different freight types
    """

    # noinspection PyArgumentList
    def __init__(self, distances=None, co2e_kg=None):
        self.__set_distances(distances)
        self.__set_co2e_kg(co2e_kg)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['distances'] = EmissionsObjectDistances.from_dict(d.get('distances'))
        v['co2e_kg'] = EmissionsObjectCo2E_Kg.from_dict(d.get('co2e_kg'))
        return EmissionsObject(**v)

    def as_dict(self):
        return dict(
            distances=self.__distances.as_dict() if self.__distances is not None else None,
            co2e_kg=self.__co2e_kg.as_dict() if self.__co2e_kg is not None else None
        )


# noinspection PyPep8Naming
class Emissions(object):

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

    __object: Optional[EmissionsObject] = None

    def __get_object(self):
        return self.__object

    def __set_object(self, object):
        if not (isinstance(object, EmissionsObject) or object is None):
            raise Exception(f'Cannot set field EmissionsObject.object to {repr(object)}')

        self.__object = object

    object = property(__get_object, __set_object)
    """
    an object containing shipment coordinates and co2e emissions
    """

    # noinspection PyArgumentList
    def __init__(self, status=None, object=None):
        self.__set_status(status)
        self.__set_object(object)

    @staticmethod
    def from_dict(d):
        v = dict()
        v['status'] = d.get('status')
        v['object'] = EmissionsObject.from_dict(d.get('object'))
        return Emissions(**v)

    def as_dict(self):
        return dict(
            status=self.__status,
            object=self.__object.as_dict() if self.__object is not None else None
        )


