from enum import Enum
import errors

PacketType = Enum('PacketType', 'eth cooked tun')

class NetworkType(Enum):
    ipv4        = 0x0800
    arp         = 0x0806
    wake_on_lan = 0x0842
    vlan        = 0x8100
    ipv6        = 0x86dd

def make_packet(data, type):
    return {
        PacketType.eth    : lambda(data): EthPacket(data),
        PacketType.cooked : lambda(data): CookedPacket(data),
        PacketType.tun    : lambda(data): TunPacket(data)
    }.get(type, lambda(data): expr_raise(Error, "Unknown packet type"))(data)

class Packet:
    def __init__(self, data):
        self.data = data

    def print_packet():
        pass

    def __getattr__(self, attr):
        raise AttributeError

class EthPacket(Packet):
    def __init__(self, data):
        super(ChildB, self).__init__(data)
        self.layout = {
            mac_dest : 2
        }

class CookedPacket(Packet):
    def __init__(self, data):
        super(ChildB, self).__init__(data)

class TunPacket(Packet):
    def __init__(self, data):
        super(ChildB, self).__init__(data)
