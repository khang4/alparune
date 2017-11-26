import alparecurse;
import snode;
import timeit;

def main():
    tree=snode.genTree(3,7,100,100);

    print(alparecurse.alphaRecurse(tree,0,100));

if __name__=="__main__":
    main();