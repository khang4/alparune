#test 5

import mmax;
import nemax;
import snode;
import timeit;

def main():
    #changeable variables:
    maxHeight=6;
    # minNodes=10000;
    # maxNodes=20000;

    minChildren=6;
    maxChildren=6;

    # maxValue=100;
    gentreeProgress=1;

    filename="test5.txt";

    for x in range(2,500):
        with open(filename,"a") as ofile:
            #put things that change here:
            maxValue=x;
            #--------

            print("-- {} --".format(x));
            tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);
            # tree=snode.genGraphTree(minNodes,maxNodes,minChildren,maxChildren,maxValue,gentreeProgress);

            #DONT CHANGE ANYTHING BELOW HERE!!!!
            times=[0,0,0,0];

            times[0]=timeit.default_timer();
            mmax.mmax(tree,0,maxValue);
            times[0]=timeit.default_timer()-times[0];

            times[1]=timeit.default_timer();
            mmax.alphaMax(tree,0,maxValue);
            times[1]=timeit.default_timer()-times[1];

            times[2]=timeit.default_timer();
            nemax.nemax(tree,1,maxValue);
            times[2]=timeit.default_timer()-times[2];

            times[3]=timeit.default_timer();
            nemax.nescout(tree,1,maxValue);
            times[3]=timeit.default_timer()-times[3];

            del tree;
            ofile.write("{} {} {} {} {}\n".format(x,times[0],times[1],times[2],times[3]));

if __name__=="__main__":
    main();