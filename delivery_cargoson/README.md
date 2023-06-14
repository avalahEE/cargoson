Cargoson Shipping
=================

This module provides Cargoson delivery carrier with additional
options for adding shipping in warehouse transfer phase.


Changelog
=========

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
