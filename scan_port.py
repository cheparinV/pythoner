import nmap

nmScan = nmap.PortScanner()
host = raw_input("Please enter host: ")
start = input("Please enter start: ")
end = input("Please enter end: ")

print 'Wait'
for i in xrange(start, end):
    cur_host = host + str(start)
    nmScan.scan(cur_host, '0-1000')
    print nmScan.scaninfo()
    print nmScan[cur_host].all_protocols()
    for port in nmScan[cur_host]['tcp']:
        thisDict = nmScan[cur_host].tcp(port)
        print 'Port ' + str(port) + ': ' + ', v' + thisDict['state']
