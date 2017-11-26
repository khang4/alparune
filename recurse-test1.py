import alparecurse;
import snode;
import timeit;

def main():
    maxHeight=8;
    minChildren=4;
    maxChildren=8;
    maxValue=100;
    tree=snode.genTree(maxHeight,minChildren,maxChildren,maxValue);

    # snode.levelPrint(tree);
    print("nodes generated: ",snode.snode.id);
    print("leaf nodes: ",snode.snode.leafs);

    starttime=timeit.default_timer();
    res=alparecurse.alphaRecurse(tree,0,maxValue);
    endtime=timeit.default_timer()-starttime;

    print("result: ",res);
    print("time: ",endtime);

if __name__=="__main__":
    main();