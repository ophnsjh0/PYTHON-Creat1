import telnetlib
import paramiko
import datetime


class HP:
    def __init__(self, switch):
        self.switch = switch
        self.rawdata = list()
        self.cmd = [' term length 0', 'display logbuffer', 'display interface brief', 'display interface | include "Ten|Forty|second input|second output"',
                    'display interface | include "Ten|Forty|errors|collisions|lost carrier"', 'display ip routing-table', 'show system brief', 'display cpu-usage summary', 
                    'display memory summary', 'display environment', 'display power', 'display fan', 'display stp | include "FORWARDING|DISCARDING|role"', 'display ntp status',
                    'exit']

    def get_telnet(self):
        ip = self.switch[0]
        port = self.switch[1]
        uid = self.switch[2]
        password = self.switch[3]
        protocol = self.switch[4]
        vendor = self.switch[5]
        cmd = str()
        for i in self.cmd:
            cmd += i+'\n'
        if vendor != 'cisco' or protocol != 'telnet':
            print('Not suppported switch %s or protocol %s' %
                  (vendor, protocol))
            exit
        data = 'ipaddr: '+ip+'\n'
        try:
            tn = telnetlib.Telnet(ip, port, 20)
            tn.read_until('Username: '.encode('ascii'))
            tn.write(uid.encode('ascii')+b'\n')
            tn.read_until('Password: '.encode('ascii'))
            tn.write(password.encode('ascii')+b'\n')
            tn.write(cmd.encode('ascii')+b'\n')
            data += tn.read_all().decode('ascii')
            tn.close()
        except Exception as ex:
            print('Something is wrong...\n', ex)
            data += 'error'
        f = open('C:/test/{0}.txt'.format(ip), 'w')
        f.write(data)
        f.close()
        self.rawdata = data.split('\n')
        return self.rawdata

    def get_ssh(self):
        ip = self.switch[0]
        ports = self.switch[1]
        uid = self.switch[2]
        passwd = self.switch[3]
        proto = self.switch[4].strip()
        vendor = self.switch[5].strip()
        data = str()
        data += 'ipaddr: '+ip+'\n'
        if proto != 'ssh' or vendor != 'cisco':
            print('Not supported switch %s or vendor %s' % (vendor, proto))
            exit()

        for i in self.cmd:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=ip, port=ports,
                            username=uid, password=passwd)
                stdin, stdout, stderr = ssh.exec_command(i.encode('ascii'))
                data += ((stdout.read()).decode('ascii')).replace('\r\n', '\n')
            except Exception as ex:
                print('Something is wrong...\n', ex)
                data += 'error'
        f = open('C:/test/{0}.txt'.format(ip), 'w')
        f.write(data)
        f.close()
        self.rawdata = data.split('\n')
        return self.rawdata

    def get_tacacs(self):
        ip = self.switch[0]
        ports = self.switch[1]
        uid = self.switch[2]
        passwd = self.switch[3]
        proto = self.switch[4].strip()
        vendor = self.switch[5].strip()
        data = str()
        data += 'ipaddr: '+ip+'\n'
        if proto != 'tacacs' or vendor != 'cisco':
            print('Not supported switch %s or vendor %s' % (vendor, proto))
            exit()

        for i in self.cmd:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=ip, port=ports,
                            username=uid, password=passwd)
                stdin, stdout, stderr = ssh.exec_command(i.encode('cp949', 'ignore'))
                data += ((stdout.read()).decode('cp949', 'ignore')).replace('\r\n', '\n')
            except Exception as ex:
                print('Something is wrong...\n', ex)
                data += 'error'
        f = open('C:/test/{0}.txt'.format(ip), 'w')
        f.write(data)
        f.close()
        self.rawdata = data.split('\n')
        return self.rawdata

