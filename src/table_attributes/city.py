from .base import TableAttrBase
from ..city_data import CITY_ID_NAME_MAP


class City(TableAttrBase):
    def __init__(self, project):
        super().__init__(
            project,
            CITY_ID_NAME_MAP.get(project['city_id'], 'Error: Unknown City'),
            'padding-left: 5px;'
        )
