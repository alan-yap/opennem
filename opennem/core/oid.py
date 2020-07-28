"""
    Module that generated opennem ids

"""

from opennem.core import base24
from opennem.db.models.opennem import Station


def get_oid(station: Station) -> str:
    _id = station.id

    if not station.id:
        return None

    return base24.dumps(_id)


def get_ocode(station: Station) -> str:
    """

        format: {country}_{network}_{region}_{station}_{id}
    """
    values = [
        station.network.country or "au",
        station.network.code or None,
        station.network_region or None,
        station.code or None,
    ]

    values = [i for i in values if i is not None]

    ocode = "_".join(values)

    return ocode
