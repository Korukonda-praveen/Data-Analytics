# task
class SmartHomeSecurity:
    'smart home security system data'
    def __init__(self,device_name,_version,__master_code):
        self.device=device_name #public
        self._version=_version #protected
        self.__master_code=__master_code #private

    def get_version(self):
        return self._version
    def set_version(self,new_version):
        if len(new_version)>=2:
            self._version=new_version
            return self._version
        else:
            return 'make sure you enter a valid version'

    def get_master_code(self):
        return self.__master_code
    def set_master_code(self,new_code):
        if len(new_code)==4:
            self.__master_code=new_code
            return self.__master_code
        else:
            return 'make sure you enter 4 digit code'
    def details(self):
        print(f'device name:{self.device}')
        print(f'firmware version:{self._version()}')
        print(f'master code:{self.__master_code}')
sec=SmartHomeSecurity('Front-Door-Lock','v2',4321)
print('Device:',sec.device)

print('get version:',sec.get_version())
print('set version:',sec.set_version('v4'))

print('get master code:',sec.get_master_code())
print('set new master code:',sec.set_master_code('0560'))
