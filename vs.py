from datetime import datetime
from sys import argv
from getpass import getpass
from f5.bigip import ManagementRoot
from f5.utils.responses.handlers import Stats
import time
import json 

script,user,device = argv

password      = getpass()
mgmt          = ManagementRoot(device, user, password,token = True)
system_info   = mgmt.tm.sys.global_settings.load()
system_status = mgmt.tm.sys.failover.load()
hardware_info = mgmt.tm.sys.hardware.load()

collection_vs = mgmt.tm.ltm.virtuals.get_collection()

     
def Get_virtual_servers():
        print("\n")
        print('| {:50} | {:40} | {:10} | {:20} | {:130}'.format("virtual server","dst-Address","Enable?","Availability-State","Details"))
        print("-"*200)

        print()
          
        for vs in collection_vs:
                
                vs_stats = Stats(vs.stats.load()) ## utils de F5.
                state = vs_stats.stat.status_availabilityState['description']
                more_info =  vs_stats.stat.status_statusReason['description']
                print ('| {:50} | {:40} | {:10} | {:20} | {:130}'.format(vs.name,vs.destination,str(vs.enabled if hasattr(vs,"enabled") else False), state, more_info))


t0 = time.time()
print("+-------------------------------------------------+")
print("| {:47} |".format("Hostname: "+ system_info.hostname))
print("| {:47} |".format("Version: "+ mgmt.tmos_version))  
print("| {:47} |".format("Model: " + hardware_info.entries['https://localhost/mgmt/tm/sys/hardware/platform']['nestedStats']['entries']['https://localhost/mgmt/tm/sys/hardware/platform/0']['nestedStats']['entries']['marketingName']['description']))
print("| {:47} |".format("Serial-Number: "+ hardware_info.entries['https://localhost/mgmt/tm/sys/hardware/system-info']['nestedStats']['entries']['https://localhost/mgmt/tm/sys/hardware/system-info/0']['nestedStats']['entries']['bigipChassisSerialNum']['description']))
print("+-------------------------------------------------+")
print("\nHA-Status: "+ system_status.apiRawValues['apiAnonymous']+"\n")
print("Fecha:"+ datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
       

Get_virtual_servers()
f_time = time.time() - t0
print ("\ntiempo transcurrido: {}".format(f_time))

