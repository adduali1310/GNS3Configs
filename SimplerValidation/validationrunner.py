from os import path
import comparison
from validation2 import interface_all_denied,interface_sensitive_denied,sensitive_noninterface_validation


with open("rules1.txt", "r+") as rules_file:
    lines = rules_file.readlines()
    for i,line in enumerate(lines):
        if "interface" not in line and "All Commands Denied" in line:
            device=line.split("->")[0]
            comparison.compare(device+".cfg",device+"_shadow.cfg")
        elif "interface" in line and "All Commands Denied" in line:
            device=line.split("->")[0]
            interface=line.split("[")[1].split(":")[0]
            interface_all_denied(device+".cfg",device+"_shadow.cfg",interface)
        elif "interface" in line and "Sensitive Commands Denied"  in line:
            device=line.split("->")[0]
            interface=line.split("[")[1].split(":")[0]
            interface_sensitive_denied(device+".cfg",device+"_shadow.cfg",interface)
        elif "interface" not in line and "Sensitive Commands Denied"  in line:
            device=line.split("->")[0]
            sensitive_noninterface_validation(device+".cfg",device+"_shadow.cfg")



            
        #         #Adding selected rule to selected router line
        #         # Remove Line and add the new config if already exists
        #         lines[i] = lines[i].strip() +" "+config
        #         count=count+1
        #         #print(count)
        # rules_file.seek(0)
        # for line in lines:
        #     rules_file.write(line)
        # # If config not present,add it
        # if count!=1:
        #     #print("Here"+str(count))
        #     rules_file.write("\n"+val +"Router-"+" "+config)

# def interface_config():
#     val = ""
#     while val!="No":
#         val=input("Please Select the device/Configuration File for specifying interface rules.Enter No to exit\n")
#         if val=="No":
#             break
#         interface=input("Please Select the interface to add rules. Ex- interface Ethernet0/0")
#         config=input("Please select config to disallow:\n"+
#         "cdp\n"+"shutdown\n"+"duplex\n"+"speed\n"+"bandwidth\n"
#         )
#         count=0
#         with open("rules.txt", "r+") as rules_file:
#             lines = rules_file.readlines()
#             for i,line in enumerate(lines):
#                 if line.startswith(val +"InterfacesRules-"):
#                     #Adding selected rule to router-interface line
#                     # Remove Line and add the new config if already exists
#                     lines[i] = lines[i].strip("]") +","+interface+":"+config+"]\n"
#                     count=count+1
#                     #print(count)
#             rules_file.seek(0)
#             for line in lines:
#                 rules_file.write(line)
#             if count!=1:
#                 #print("Here"+str(count))
#                 rules_file.write("\n"+val +"InterfacesRules-"+"["+interface+":"+config+"]")


# def take_input():
#     val = input("Please Select your choice:\n"+     
#         "1: Router\n"+
#         "2: Switch\n"+
#         "3: Firewall\n"+
#         "4: Router-Interface\n"+
#         "5: Switch-Interface\n"+
#         "6: Firewall_interface\n"
#      ) 
#     return val

# def main():


# if __name__ == "__main__":
#     main()