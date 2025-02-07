from socket import *
def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[-]%d/tcp open'% tgtPort)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conScan('216.58.207.238', 80)