#test4 varied high density
#vary: children
#fixed: height, value
#measure: time

import mmax;
import nemax;
import snode;
import timeit;

def main():
    maxHeight=5;
    minChildren=8;
    maxChildren=10;
    maxValue=100;
    gentreeProgress=1;

    for x in range(10,16):
        with open("test4a.txt","a") as ofile:
            minChildren=x;
            maxChildren=minChildren+2;
            print("-- {} --".format(x));
            tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);

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