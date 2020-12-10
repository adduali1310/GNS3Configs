def compare(shadow_file,original_file):
    with open(shadow_file, 'r') as file1:
        with open(original_file, 'r') as file2:
            difference = set(file1).difference(set(file2)).union(
                set(file2).difference(set(file1)))

    difference.discard('\n')

    with open(original_file.split(".cfg")[0]+'differences.txt', 'w') as file_out:
        if(len(difference))>1:
            print("The following changes have been detected in shadow network of "+original_file)
            for line in difference:
                print(line)
                file_out.write(line)
