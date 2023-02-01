
# vs.py

Script que muestra el estado de los virtual servers para BIG-IP via iControl REST.
Por defecto devolvera el Modelo,version,serial number y status de todos los virtual servers configurados en el equipo.



uso
```
vs.py <admin_user> <Device_ip> 

```

Output
```
+-------------------------------------------------+
| Hostname: bigip.lab                             |
| Version: 15.1.3                                 |
| Model: BIG-IP Virtual Edition                   |
| Serial-Number: 564d6fee-6a4f-5851-8455eeeeeeee  |
+-------------------------------------------------+

HA-Status: Failover active for 251d 06:36:24


Fecha:01/02/2023 10:49:29


| virtual server                        | dst-Address                        | Enable?    | Availability-State   | Details
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| VS_Asterisk                           | /Common/192.168.11.59:5060         | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| VS_Asterisk_2                         | /Common/192.28.11.56:5060          | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| mgmt_A                                | /Common/192.89.210.4:443           | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| APM_s                                 | /Common/122.40.210.4:22            | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| captive_portal_swg                    | /Common/192.109.210.5:443          | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| captive_portal_swg_redirect           | /Common/192.101.210.5:80           | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| site_dmz                              | /Common/10.2.230.0:0               | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| site_lan1                             | /Common/10.5.231.0:0               | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| site_lan2                             | /Common/10.220.3.16:0              | True       | unknown              | The children pool member(s) either don't have service checking enabled,
| forwarding_con_in                     | /Common/0.0.0.0:0                  | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| forwarding_fundacion_in               | /Common/0.0.0.0:0                  | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| forwarding_interred_in                | /Common/0.0.0.0:0                  | True       | unknown              | The children pool member(s) either don't have service checking enabled, 
| ftps                                  | /Common/192.168.215.5:0            | True       | available            | The virtual server is available

```
