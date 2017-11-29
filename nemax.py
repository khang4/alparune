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

def nescout(node,mode,maxValue,alpha=None,beta=None):
    if alpha==None or beta==None:
        alpha=-maxValue;
        beta=maxValue;

    if len(node.children)==0:
        return mode*node.value;

    firstChild=1;
    for x in node.children:
        if firstChild:
            firstChild=0;
            alpha=max(alpha,-nescout(x,-mode,maxValue,-beta,-alpha));

        else:
            childValue=-nescout(x,-mode,maxValue,-(alpha+1),-alpha);
            if alpha<childValue and childValue<beta:
                childValue=-nescout(x,-mode,maxValue,-beta,-childValue);
            alpha=max(alpha,childValue);

        if alpha>=beta:
            break;

    return alpha;

def main():
    # root=snode.genTree(3,1,5,100,1);
    root=snode.genGraphTree(45000,45000,5,10,100,0);

    # snode.levelPrint(root);

    print(alparecurse.minmaxRecurse(root,0,100));
    print(alparecurse.alphaRecurse(root,0,100));
    print(nemax(root,1,100));
    print(nescout(root,1,100));

if __name__=="__main__":
    main();