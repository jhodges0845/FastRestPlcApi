from pycomm3 import LogixDriver

def read_plc(ip_address, tag_name):
    try:
        with LogixDriver(ip_address) as plc:
            return plc.read(tag_name)
    except:
        #log error
        return ""


def write_plc(ip_address, tag_name, tag_value):
    try:

        with LogixDriver(ip_address) as plc:
            result = plc.write(tag_name, tag_value)
            return result

    except:
        # log error
        return ""


def info_plc(ip_address):
    try:
        with LogixDriver(ip_address) as plc:
            return plc.info
    except:
        # Log error
        return ""

def read_all_plc(ip_address):
    try:
        with LogixDriver(ip_address) as plc:
            return plc.tags
    except:
        # Log error#
        return ""