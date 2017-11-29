#test1 height, ranged density
#vary: height
#fixed: children, value
#measure: time

import alparecurse;
import snode;
import timeit;

def main():
    maxHeight=10;
    minChildren=1;
    maxChildren=5;
    maxValue=100;
    gentreeProgress=1;

    ofile=open("test1.txt","w");
    for x in range(12):
        tree=snode.genTree(x,minChildren,maxChildren,maxValue,gentreeProgress);

        starttime=timeit.default_timer();
        res=alparecurse.alphaRecurse(tree,0,maxValue);
        endtime=timeit.default_timer()-starttime;

        ofile.write("{} {}\n".format(x,endtime));

if __name__=="__main__":
    main();