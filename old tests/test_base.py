import mmax;
import snode;
import timeit;

def main():
    maxHeight=10;
    minChildren=1;
    maxChildren=5;
    maxValue=100;
    gentreeProgress=1;
    tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue,gentreeProgress);

    # snode.levelPrint(tree);
    print("nodes generated: ",snode.snode.id);
    print("leaf nodes: ",snode.snode.leafs);

    starttime=timeit.default_timer();
    res=mmax.alphaMax(tree,0,maxValue);
    endtime=timeit.default_timer()-starttime;

    print("result: ",res);
    print("time: ",endtime);

if __name__=="__main__":
    main();