import dpkt

with open('error_reporting.pcap', 'rb') as f:
    packets = []
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        payload = dpkt.ethernet.Ethernet(buf).data.data.data.data
        packets.append(payload)

with open('answer.jpg', 'w+b') as of:
    of.write(b''.join(packets[1:]))