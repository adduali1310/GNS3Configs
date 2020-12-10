from os import path
from ciscoconfparse import CiscoConfParse
import collections
import re

sensitive_commands=["shutdown","ipsec","logging","password","crypto map"]
def sensitive_noninterface_validation(original_file_name,shadow_file_name):
    with open(shadow_file_name, 'r') as file1:
        with open(original_file_name, 'r') as file2:
            difference = set(file1).difference(set(file2)).union(
                set(file2).difference(set(file1)))
    difference.discard('\n')
    differences=list(difference)
    if len(differences)<1:
        print ("No changes to "+original_file_name)
    else:
        for item in sensitive_commands:
            for config in differences:
                if item in config:
                    print("\nSensitive Commands Modified in "+shadow_file_name)
                    print(config)

def interface_all_denied(original_file_name,shadow_file_name,interface_name):
        original_list=[]
        shadow_list=[]
        # useful for rules related to interfaces only.
        parse = CiscoConfParse(original_file_name, syntax='ios')
        for intf_obj in parse.find_objects('^interface'):
            # Check if Interface exists in config
            if interface_name in str(intf_obj):
                for child in intf_obj.children:
                    # Using Regex Capture Group to Extract only the command.
                    capture=re.search(r'\'(.*)\'', str(child)).group(1)
                    original_list.append(capture)

        parse = CiscoConfParse(shadow_file_name, syntax='ios')
        for intf_obj in parse.find_objects('^interface'):
            # Check if Interface exists in config
            if interface_name in str(intf_obj):
                for child in intf_obj.children:
                    capture=re.search(r'\'(.*)\'', str(child)).group(1)
                    shadow_list.append(capture)
        differences=list(set(shadow_list) - set(original_list))
        if len(differences)<1:
            print ("No changes to "+interface_name)
        else:
            for config in differences:
                    print("\nChanges Made to "+interface_name+ " in "+shadow_file_name)
                    print(config)
        # if collections.Counter(original_list) == collections.Counter(shadow_list): 
        #         print ("No changes to "+interface_name)
        # else:
        #     print("Changes made to  "+interface_name)
        #     print("\n"+str(shadow_list)+"\n")
        
def interface_sensitive_denied(original_file_name,shadow_file_name,interface_name):
        original_list=[]
        shadow_list=[]
        # useful for rules related to interfaces only.
        parse = CiscoConfParse(original_file_name, syntax='ios')
        for intf_obj in parse.find_objects('^interface'):
            # Check if Interface exists in config
            if interface_name in str(intf_obj):
                for child in intf_obj.children:
                    capture=re.search(r'\'(.*)\'', str(child)).group(1)
                    original_list.append(capture)

        parse = CiscoConfParse(shadow_file_name, syntax='ios')
        for intf_obj in parse.find_objects('^interface'):
            # Check if Interface exists in config
            if interface_name in str(intf_obj):
                for child in intf_obj.children:
                    capture=re.search(r'\'(.*)\'', str(child)).group(1)
                    shadow_list.append(capture)
        differences=list(set(shadow_list) - set(original_list))
        for item in sensitive_commands:
            for config in differences:
                if item in str(config):
                    print("\nSensitive Commands Modified in "+interface_name+ " in "+shadow_file_name)
                    print(config)
        
        

def main():
    sensitive_noninterface_validation("sample.txt","sample1.txt")

if __name__ == "__main__":
    main()

