Cargoson Shipping
=================

This module provides Cargoson delivery carrier with additional
options for adding shipping in warehouse transfer phase.


Changelog
=========

- 1.1.2
    - [ADD] Added manual weight adjustment option for wizards.
- 1.1.1
    - [FIX] Fixed cargoson weight by converting it to kilograms when sending API request.
- 1.1.0
    ### Added
    - Fields to Cargosoni wizard and `cargoson.shipping.options` models:
    - ADR UN: text field (four-digit UN number for hazardous materials/articles).
    - ADR Group: selection field (I - high danger, II - medium danger, III - low danger).
    - ADR Class: selection field (1 - Explosives, 2 - Gases, 3 - Flammable liquids, 4 - Flammable solids).
    - ADR NEQ: text field (weight/volume of dangerous goods in package excluding packaging material; or weight of unpackaged article of dangerous goods).
    - ADR Description: text field (description of the dangerous goods).
    - ADR fields are now visible when ADR option is activated.
    ### Updated
    - The `_cargoson_send_shipping` method in the `delivery.carrier` model has been updated to include ADR data with the booking. The `OrderRows_AttributesItem` object now has an `adr_rows_attributes` attribute (a list of `OrderRows_AttributesItemAdr_Rows_AttributesItem` instances).
- 1.0.9
    - Two new fields `estimated_collection_date` and `estimated_delivery_date` in Cargoson AvailablePrices schema.
    - Displayed these new fields in wizards where the `get rates` function is called.
    - Stored these new fields in the `cargoson.shipping.options`.
- 1.0.8
    - Added a new method `_cargoson_get_self_service_url(self, path)` to the `ProviderCargoson` class, that creates a URL by  removing `/api` from the base URL and adding the provided path.
    - Enhanced the `_cargoson_send_shipping` method to log the CMR document link, the Waybill document link, and the Customs declaration document link in the `stock.picking` object.
    - Also added a DGD document link to the log if the ADR option in shipping options is true.
    - All log messages are now translatable and Estonian translations have been added for the new messages.
- 1.0.7
    - Changed "update cargoson data" button location.
- 1.0.6
    - Added no carrier options, so shipments can be completed without having to specify carrier.
- 1.0.5
    - Added height, depth, width fields for wizards.
- 1.0.4
    - Added manual Cargoson data update button on stock picking form.
- 1.0.3
    - Disallow "Get prices" for orders that have shipping weight of zero
- 1.0.2
    - Pallet name translations
- 1.0.1
    - Add proper packaging and pallet names
- 1.0.0
    - Initial version
