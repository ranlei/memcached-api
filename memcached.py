import socket
import sys
import re


class MemCached(object):

    def __init__(self, addr="localhost", port=12000):
        self.addr = addr
        self.port = port
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("socket connect error.")
            sys.exit()
        try:
            self.remote_ip = socket.gethostbyname(self.addr)
        except socket.gaierror:
            print("hostname is wrong.")
            sys.exit()
        self.s.connect((self.remote_ip, self.port))

    def __del__(self):
        self.s.close()

    def checkkey(fn):
        def check(self, *argv):
            obj = MemCached(self.addr, self.port)
            # first argument is key in tuple
            result = obj.get(argv[0])
            if result:
                print("key is existed.")
                return False
            else:
                return fn(self, *argv)
        return check

    @checkkey
    def set(self, key, data, flags=0, exptime=0):
        byte_num = len(str(data))
        message = "set "+key+" "+str(flags)+" "+str(exptime)+" "+str(byte_num)\
            + " "+"[noreply]\r\n"+data+"\r\n"
        try:
            self.s.sendall(message)
        except socket.error:
            return False
            sys.exit()
        return True

    def get(self, key):
        message = "get "+str(key)+"\r\n"
        try:
            self.s.sendall(message)
        except socket.error:
            return False
            sys.exit()
        reply = self.s.recv(4096)
        li = re.split("\r\n", reply)
        try:
            if li[-3]:
                return li[-3]
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    mem = MemCached()
    mem.set("names", "rale")
    mem_get = MemCached()
    print(mem_get.get("names"))
