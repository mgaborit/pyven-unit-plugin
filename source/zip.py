import zipfile, os
import unit_plugin.constants

def zip_pvn():
    if not os.path.isdir(os.path.join(os.environ.get('PVN_HOME'), 'plugins')):
        os.makedirs(os.path.join(os.environ.get('PVN_HOME'), 'plugins'))
    zf = zipfile.ZipFile(os.path.join(os.environ.get('PVN_HOME'), 'plugins', 'unit-plugin_' + unit_plugin.constants.VERSION + '.zip'), mode='w')
    
    zf.write('__init__.py')
    
    zf.write('unit_plugin/__init__.py')
    zf.write('unit_plugin/constants.py')
    zf.write('unit_plugin/parser.py')
    zf.write('unit_plugin/unit.py')
    
if __name__ == '__main__':
    zip_pvn()
