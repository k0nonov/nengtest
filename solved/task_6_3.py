access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20", "30", "40"], "0/2": ["only", "11", "21", "31", "41"], "0/4": ["del", "17", "27", "37"]}

for intf, conf in trunk.items():
    print("interface FastEthernet" + intf)
    for command in trunk_template:
        if command.endswith("vlan"):
            if conf[0] == "add":
                for i in range(1,len(conf)):
                    if i == 1:
                        vlans = conf[i]
                    else:
                        vlans = vlans + ', ' + conf[i]
                print(f" {command} add {vlans}")
            elif conf[0] == "only":
                for i in range(1,len(conf)):
                    if i == 1:
                        vlans = conf[i]
                    else:
                        vlans = vlans + ', ' + conf[i]
                print(f" {command} {vlans}")
            elif conf[0] == "del":
                for i in range(1,len(conf)):
                    if i == 1:
                        vlans = conf[i]
                    else:
                        vlans = vlans + ', ' + conf[i]
                print(f" {command} remove {vlans}")

        else:
            print(f" {command}")
