#test5 value
#vary: value
#fixed: height, children
#measure: time

import mmax;
import snode;
import timeit;

def main():
    maxHeight=6;
    minChildren=5;
    maxChildren=5;
    maxValue=100;
    gentreeProgress=1;

    for x in range(2,500):
        with open("test5a.txt","a") as ofile:
            maxValue=x;
            print("-- {} --".format(x));
            tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);

            starttime=timeit.default_timer();
            res=mmax.alphaMax(tree,0,maxValue);
            endtime=timeit.default_timer()-starttime;

            del tree;
            ofile.write("{} {}\n".format(x,endtime));

if __name__=="__main__":
    main();