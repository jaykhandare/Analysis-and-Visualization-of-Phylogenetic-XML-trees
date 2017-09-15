from Bio import Phylo
import sys

tree = Phylo.read("fullexample-1.xml", "phyloxml")

counter = 1
branchName = ''
output = open('output.txt', 'w')

for clade in tree.find_clades():
    TotalBranchLength = 0.00
    np = ''
    
    if counter == 1:
       counter = counter + 1  
    
    elif clade.name == None:
       branchName = 'B' + str(counter)
       clade.name = branchName
       counter = counter + 1 
       for node_path in tree.get_path(clade):
        TotalBranchLength = TotalBranchLength + node_path.branch_length
       node_path = tree.get_path(clade)
       if len(node_path) > 1:
        np = (node_path[-2])

       output.write(branchName)
       output.write("|")
       output.write(str(clade.branch_length))
       output.write("|")
       output.write(str(TotalBranchLength))
       output.write("|")
       if clade.confidence == None:
           output.write("0")
       else :
           output.write(str(int(clade.confidence)))

       output.write("|")
       output.write(str(len(node_path)))
       output.write("|")
       output.write(str(len(clade.get_terminals())))
       output.write("|")
       if np == '':
           output.write("ROOT")
       else:
           output.write(str(np))
       output.write("\n")
        
    else:
         
       for node_path in tree.get_path(clade):
        TotalBranchLength = TotalBranchLength + node_path.branch_length
       node_path = tree.get_path(clade)
       if len(node_path) > 1:
        np = (node_path[-2])
            
       output.write(str(clade.name))
       output.write("|")
       output.write(str(clade.branch_length))
       output.write("|")
       output.write(str(TotalBranchLength))
       output.write("|")
       output.write("0")
       output.write("|")
       output.write(str(len(node_path)))
       output.write("|")
       output.write("1")
       output.write("|")
       output.write(str(np))
       output.write("\n")