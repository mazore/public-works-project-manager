from .base import TableAttrBase
from ..dt_helpers import format_time


class Time(TableAttrBase):
    def __init__(self, project):
        text = format_time(project['dt'])
        super().__init__(project, text, 'padding-left: 2px;')
