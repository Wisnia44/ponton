import json
import pingparsing

def ping_time(host):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = 1
    result = transmitter.ping()
    result_dict = ping_parser.parse(result).as_dict()
    return result_dict['rtt_avg']