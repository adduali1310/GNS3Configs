from os import path
from ciscoconfparse import CiscoConfParse

with open('rules.txt', 'r') as rule_file:
    for line in rule_file:
        # Removing extra spaces in files
        line = line.rstrip("\n")
        current_line = line.split(' ', 1)

        # Getting the Device Name
        device = current_line[0]+".cfg"
        if path.exists(device):
            list_of_nonintf_rules=[]
            list_of_intf_rules=[]
            # Getting Rule list and excluding [] brackets
            temp = current_line[1].split('[',2)
            list_of_nonintf_rules.append('['.join(temp[:2])[1:-1])
            
            # Append interfaces rules to list if they exist
            try:
              list_of_intf_rules.append(temp[2][:-1])  
            except IndexError:
                pass

            
            with open(device, 'r') as config_file:
                # useful for rules related to interfaces only.
                parse = CiscoConfParse(device, syntax='ios')
                for item in list_of_intf_rules:
                    for intf_obj in parse.find_objects('^interface'):
                        # Check if Interface exists in config
                        if item.split(':')[0] in str(intf_obj):
                            # Check individual config for given interface
                            # Another way to try can be parse.find_objects_w_child
                            if item.split(':')[1].split('-')[0] in str(intf_obj.children) and item.split(':')[1].split('-')[1]=="Not Allowed":
                                print("Rule is",item)
                                print("Config in shadow network is different")
                                print(str(intf_obj)+" : "+ str(intf_obj.children)+"\n")

                for config in config_file:
                    config=config.rstrip("\n")
                    for item in list_of_nonintf_rules:
                        if item.split(':')[0] in config and item.split(':')[1]=="Not Allowed":
                            print("Rule is",item)
                            print("Config in shadow network is different")
                            print(config,"\n")
            
        
