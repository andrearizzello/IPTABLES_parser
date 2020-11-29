import json

if __name__ == '__main__':
    requestList = []
    for line in open('/var/log/ufw.log', 'r'):
        request = {}
        source_index = line.find('SRC=')
        if source_index != -1:
            source = line[source_index + 4:].split(' ', 1)[0]
            request['source'] = source
        protocol_index = line.find('PROTO=')
        if protocol_index != -1:
            protocol = line[protocol_index + 6:].split(' ', 1)[0]
            request['protocol'] = protocol
        destination_port_index = line.find('DPT=')
        if destination_port_index != -1:
            destination_port = int(line[destination_port_index + 4:].split(' ', 1)[0])
            request['dest_port'] = destination_port
        requestList.append(request)
    print(json.dumps(requestList))
