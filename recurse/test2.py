#test2 density, fixed height
#vary: children
#fixed: height, value
#measure: time

import alparecurse;
import snode;
import timeit;

def main():
    maxHeight=5;
    minChildren=1;
    maxChildren=5;
    maxValue=100;
    gentreeProgress=1;

    ofile=open("test2.txt","a");

    for x in range(45,48):
        maxChildren=x;
        print("-- {} --".format(x));
        tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);

        starttime=timeit.default_timer();
        res=alparecurse.alphaRecurse(tree,0,maxValue);
        endtime=timeit.default_timer()-starttime;

        del tree;
        ofile.write("{} {}\n".format(x,endtime));

if __name__=="__main__":
    main();