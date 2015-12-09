__author__ = 'LG'

import ConfigParser
import os


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class GetConfigs():
    cf = ConfigParser.ConfigParser()
    #read config
    cf.read(PATH("setting.conf"))

    def get_configs_by_sec(self,secName):
        kvs = self.cf.items(secName)
        return kvs


'''
    # return all section
    # secs = cf.sections()
    # print 'sections:', secs
    opts = self.cf.options(secName)
    print 'driver1.options:', opts

    kvs = cf.items("driver1")
    print 'driver1.items:', kvs

    #read by type
    str_val = cf.get("driver1", "appActivity")
    int_val = cf.getint("driver1", "udid")

    print "Striug value:", str_val
    print "Int value:", int_val



    #write config
    #update value
    cf.set("sec_b", "b_key3", "new-$r")
    #set a new value
    cf.set("sec_b", "b_newkey", "new-value")
    #create a new section
    cf.add_section('a_new_section')
    cf.set('a_new_section', 'new_key', 'new_value')

    #write back to configure file
    cf.write(open("test.conf", "w"))
    '''

if __name__ == '__main__':
    GetConfigs().get_configs_by_sec('driver1')