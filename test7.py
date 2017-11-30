#test 7

import mmax;
import nemax;
import snode;
import timeit;

def main():
    #changeable variables:
    # maxHeight=6;
    minNodes=50000;
    maxNodes=50000;

    minChildren=10;
    maxChildren=10;

    # maxValue=100;
    gentreeProgress=1;

    filename="test7.txt";

    for x in range(500,501):
        with open(filename,"a") as ofile:
            #put things that change here:
            maxValue=x;
            #--------

            print("-- {} --".format(x));
            # tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);
            tree=snode.genGraphTree(minNodes,maxNodes,minChildren,maxChildren,maxValue,gentreeProgress);

            #DONT CHANGE ANYTHING BELOW HERE!!!!
            mmax.alphaMax(tree,0,maxValue);
            nemax.nescout(tree,1,maxValue);

            del tree;
            ofile.write("{} {} {}\n".format(x,mmax.alphaBreak,nemax.nescoutBreak));
            mmax.alphaBreak=0;
            nemax.nescoutBreak=0;

if __name__=="__main__":
    main();