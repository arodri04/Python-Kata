def ip_to_int32(ip):
    list = ip.split(".")
    result = int(list[0]) << 24
    print(result)
    result += int(list[1]) << 16
    print(result)
    result += int(list[2]) << 8
    print(result)
    result += int(list[3])
    return result
