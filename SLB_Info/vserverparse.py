import re

class VserverParse:
    def __init__(self, config):
        self.config = config
        self.result = dict()

    def test(self):
        print(self.config)

    # def getvserver():
    #     vserver=list()
    #     p=re.compile('add lb vserver')
    #     print(self.config)
    #     for i in self.config:
    #         m=p.search(i)
    #         print(m)
    #         if m:
    #             vserver.append(i)
    #     print(vserver)
    #     if vserver:
    #         self.result['vserver']=vserver[4].strip()
    #     return self.result

    # def saveresult(self):
    #     self.getvserver()
    #     return self.result
    