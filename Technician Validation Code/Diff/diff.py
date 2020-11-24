with open('shadow_network.cfg', 'r') as file1:
    with open('original.cfg', 'r') as file2:
        difference = set(file1).difference(set(file2)).union(
            set(file2).difference(set(file1)))

difference.discard('\n')

print("The Changes made to Shadow Network different from Original Network are copied to differences.txt file")

with open('differences.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)
