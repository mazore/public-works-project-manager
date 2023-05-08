from .base import TableAttrBase


class Name(TableAttrBase):
    def __init__(self, project):
        super().__init__(project, project['name'], 'padding-left: 5px;')
