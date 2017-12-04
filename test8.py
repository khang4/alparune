#test 1

import mmax;
import nemax;
import snode;
import psutil;
import os;

def main():
    pr=psutil.Process(os.getpid());
    #changeable variables:
    # maxHeight=5;
    # minNodes=10000;
    # maxNodes=20000;

    minChildren=1;
    maxChildren=5;

    maxValue=100;
    gentreeProgress=1;

    filename="test8d.txt";

    for x in range(0,15):
        with open(filename,"a") as ofile:
            #put things that change here:
            maxHeight=x;
            #--------

            print("-- {} --".format(x));
            tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);
            # tree=snode.genGraphTree(minNodes,maxNodes,minChildren,maxChildren,maxValue,gentreeProgress);

            #DONT CHANGE ANYTHING BELOW HERE!!!!
            # mmax.mmax(tree,0,maxValue);
            # mmax.alphaMax(tree,0,maxValue);
            # nemax.nemax(tree,1,maxValue);
            nemax.nescout(tree,1,maxValue);

            del tree;
            ofile.write("{} {}\n".format(x,pr.memory_full_info().uss));

if __name__=="__main__":
    main();