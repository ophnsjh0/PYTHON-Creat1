import re
import math

class citrixParse:
    def __init__(self, rawdata):
        self.rawdata=rawdata
        self.result=dict()
        

    def getip(self):
        ip=list()
        p=re.compile('^ipaddr')
        for i in self.rawdata:
            m=p.search(i)
            if m:               
                i=' '.join(i.split())                
                ip=i.split(':')
                print(i)
        if ip:
            self.result['ip']=ip[1].strip()
        else:
            self.result['ip']='unknown'
        return self.result

    def getmodel(self):
        model=list()
        p=re.compile('Platform:')
        for i in self.rawdata:
            m=p.search(i)
            if m:               
                i=' '.join(i.split())
                model=i.split(' ')              
        if model:
            self.result['model']=model[1].strip()
        else:
            self.result['model']='unknown'
        return self.result

    def gethostname(self):
        hosts=list()
        p=re.compile('Hostname:')
        for i in self.rawdata:
            m=p.search(i)
            if m:
                i=' '.join(i.split())
                hosts=i.split(' ')
        if hosts:
            self.result['hostname']=hosts[1].strip()
        else:
            self.result['hostname']='unknown'
        return self.result

    def getcpu(self):
        cpu=list()
        p=re.compile('Packet CPU usage')
        for i in self.rawdata:
            m=p.search(i)
            if m:                
                i=' '.join(i.split())            
                cpu=i.split(' ')             
        if cpu:
            self.result['cpu util']=cpu[-1].strip()+'%'
        else:
            self.result['cpu util']='unknown'
        return self.result

    def getmem(self):
        mem=list()
        p=re.compile('InUse Memory')
        for i in self.rawdata:
            m=p.search(i)
            if m:                
                i=' '.join(i.split())               
                mem=i.split(' ')               
        if mem:
            self.result['mem util']=mem[-1].strip()+'%'
        else:
            self.result['mem util']='unknown'
        return self.result

    def gettemp(self):
        temp=list()
        p=re.compile('Internal Temperature')
        for i in self.rawdata:
            m=p.search(i)
            if m:
                i=' '.join(i.split())
                temp=i.split(' ')
        if temp:
            self.result['temperature']=temp[-1]
        else:
            self.result['temperature']='unknown'
        return self.result

    def getfan(self):
        fan=list()
        p=re.compile('System Fan Speed')
        for i in self.rawdata:
            m=p.search(i)           
            if m:
                i=' '.join(i.split())
                fan=i
        if fan:
            self.result['fan']=fan[-1]
        else:
            self.result['fan']='unknown'
        return self.result

    def getpower(self):
        ps=list()
        p=re.compile('Power supply 1')
        for i in self.rawdata:
            m=p.search(i)
            if m:
                i=' '.join(i.split())
                ps=i.split(' ')
        if ps:
            self.result['power']=ps[-1].strip()
        else:
            self.result['power']='unknown'
        return self.result

    def saveresult(self):
        self.getip()
        self.getmodel()
        self.gethostname()
        self.getcpu()
        self.getmem()
        self.gettemp()
        self.getfan()
        self.getpower()
        return self.result





