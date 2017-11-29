import snode;
import alparecurse;

#to start, give it:
#node=root node
#mode=1 for maximise, -1 for minimise
#maxValue=maximum value possible, give it same value given to genTree
#alpha and beta bootstraps itself
def nemax(node,mode,maxValue,alpha=None,beta=None):
    if alpha==None or beta==None:
        alpha=-maxValue;
        beta=maxValue;

    if len(node.children)==0:
        return mode*node.value;

    childMax=-maxValue;
    for x in node.children:
        childMax=max(childMax,-nemax(x,-mode,maxValue,-beta,-alpha));
        alpha=max(alpha,childMax);
        if alpha>=beta:
            break;

    return childMax;

def main():
    root=snode.genTree(3,1,5,100,1);

    snode.levelPrint(root);

    print(alparecurse.minmaxRecurse(root,0,100));
    print(alparecurse.alphaRecurse(root,0,100));
    print(nemax(root,1,100));

if __name__=="__main__":
    main();