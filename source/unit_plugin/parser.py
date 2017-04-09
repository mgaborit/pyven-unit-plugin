import os

from pyven.exceptions.parser_exception import ParserException
from pyven.plugins.plugin_api.parser import Parser

from unit_plugin.unit import Unit

class UnitParser(Parser):
    COUNT = 0
    SINGLETON = None
    
    def __init__(self, cwd):
        UnitParser.COUNT += 1
        super(UnitParser, self).__init__(cwd)
    
    def parse(self, node):
        objects = []
        members = self.parse_process(node)
        errors = []
        file = node.find('file').text
        if file == '':
            errors.append('Missing test executable file')
        (path, filename) = os.path.split(file)
        arguments = []
        for argument in node.xpath('arguments/argument'):
            arguments.append(argument.text)
        format = 'cppunit'
        if len(errors) > 0:
            e = ParserException('')
            e.args = tuple(errors)
            raise e
        objects.append(Unit(self.cwd, members[0], path, filename, arguments, format))
        return objects
        
def get(cwd):
    if UnitParser.COUNT <= 0 or UnitParser.SINGLETON is None:
        UnitParser.SINGLETON = UnitParser(cwd)
    UnitParser.SINGLETON.cwd = cwd
    return UnitParser.SINGLETON