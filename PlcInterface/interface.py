from pycomm3 import LogixDriver

def read_plc(ip_address, tag_name):
    try:
        with LogixDriver(ip_address) as plc:
            return plc.read(tag_name)
    except:
        #log error
        return ""


def write_plc(ip_address, tag_name, data_type, tag_value):
    try:
        with LogixDriver(ip_address) as plc:
            # Validate value is same as tag data_type

            result = plc.write(tag_name, tag_value)
            return result
    except:
        # log error
        return ""