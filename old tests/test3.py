#test3 height, high density
#vary: height
#fixed: children, value
#measure: time

import mmax;
import snode;
import timeit;

def main():
    maxHeight=5;
    minChildren=8;
    maxChildren=10;
    maxValue=100;
    gentreeProgress=1;

    ofile=open("test3.txt","a");

    for x in range(8,11):
        maxHeight=x;
        print("-- {} --".format(x));
        tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);

        starttime=timeit.default_timer();
        res=mmax.alphaMax(tree,0,maxValue);
        endtime=timeit.default_timer()-starttime;

        del tree;
        ofile.write("{} {}\n".format(x,endtime));

if __name__=="__main__":
    main();