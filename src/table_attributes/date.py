from datetime import datetime
from .base import TableAttrBase
from ..dt_helpers import format_date


class Date(TableAttrBase):
    def __init__(self, project):
        text = format_date(project['dt'])
        if project['dt'] == datetime.min:
            text = project['time']

        super().__init__(project, text, 'padding-left: 2px;')
