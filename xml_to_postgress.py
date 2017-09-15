from Bio import Phylo
#import sys
import psycopg2

def connect():
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='123'")
    cur = conn.cursor()
    conn.commit()
    return(cur,conn)    

def create_table(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS PHYLOXML(BRANCH_NAME VARCHAR(20), BRANCH_LENGTH FLOAT(20), TOTAL_BRANCH_LENGTH FLOAT(20), CONFIDENCE INTEGER, NODE_PATH_LENGTH INTEGER, TERMINALS_NUMBER INT, PARENT_NODE VARCHAR(20))""")
    cur.execute("""TRUNCATE TABLE PHYLOXML""")       
    
def add_values(cur,a,b,c,d,e,f,g):
    cur.execute("INSERT INTO PHYLOXML(BRANCH_NAME,BRANCH_LENGTH,TOTAL_BRANCH_LENGTH,CONFIDENCE,NODE_PATH_LENGTH,TERMINALS_NUMBER,PARENT_NODE) VALUES (%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g))

cur,conn = connect()
create_table(cur)
conn.commit()

tree = Phylo.read("fullexample-1.xml", "phyloxml")
counter = 1
branchName = ''
#output = open('output.txt', 'w')

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

#       output.write(branchName)
       a = branchName    
#       output.write(str(clade.branch_length))
       b = str(clade.branch_length)
#       output.write(str(TotalBranchLength))
       c = str(TotalBranchLength)
       if clade.confidence == None:
#           output.write("0")
           d = "0"
       else :
#           output.write(str(int(clade.confidence)))
           d = str(int(clade.confidence))
           
#       output.write(str(len(node_path)))
       e = str(len(node_path))
#       output.write(str(len(clade.get_terminals())))
       f = str(len(clade.get_terminals()))
       if np == '':
#           output.write("ROOT")
           g = "ROOT"
       else:
#           output.write(str(np))
           g = str(np)

       add_values(cur,a,float(b),float(c),int(d),int(e),int(f),g)
       conn.commit()

    else:
         
       for node_path in tree.get_path(clade):
        TotalBranchLength = TotalBranchLength + node_path.branch_length
       node_path = tree.get_path(clade)
       if len(node_path) > 1:
        np = (node_path[-2])
            
#       output.write(str(clade.name))
       a = str(clade.name)  
#       output.write(str(clade.branch_length))
       b = str(clade.branch_length)  
#       output.write(str(TotalBranchLength))
       c = str(TotalBranchLength)   
#       output.write("0")
       d = "0"
#       output.write(str(len(node_path)))
       e = str(len(node_path))  
#       output.write("1")
       f = "1"
#       output.write(str(np))
       g = str(np)
       add_values(cur,a,float(b),float(c),int(d),int(e),int(f),g)
       conn.commit()

print("Stored given XML data into postgreSQL DB named 'postgres' (which is default database for PostgreSQL) in table named 'PHYLOXML'")

