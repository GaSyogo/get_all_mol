'''
get_all_mol.py written by HE
20210115
note:this is a python script to merge MULTIPLE mol files(each with ONE molecule) into ONE sdf file
the source mol files was a list of mol files like:
000.mol
...
268.mol

Command line arguments include
 - the max num of XXX.mol
 - one filename for the output sdf file
'''


import sys
import pandas as pd

def getString(inFile):
	ans = str()
	ll = "somestring"
	while ll != "" and ll.find("$$$$") == -1:
		ll = inFile.readline()
		ans += ll
	return ans

# Traverse n files
def traverse(n):
	ans = str()
	for i in range(n):
		k = str(i)
		notStand_k = k.zfill(3)#notStand_k is a string like "012"
		inf = (str(notStand_k+".mol"))
		with open(inf) as f:
			oldString = getString(f)
			#print(oldString)
			sdfString = str(str(i) + oldString[3:])
			#for j in range(len(sdfString)):
			#	print("sdfString[{}]:".format(j),sdfString[j])
			ans += sdfString
	return ans



def main(argv):
	n = argv[1]
	n = int(n)+1 # remind that we have (max num+1) files
	outname = argv[2]
	ans = traverse(n)
	with open(str(outname+'.sdf'),'w') as f:
		f.write(ans)
	#ans = getString(inFile):


main(sys.argv)