import snode;

#alpha should be initially set to -1, and beta should never be negative,
#except at the beginning, where it immediately gets set to the maxValue
#maxValue needs to be given and needs to match the maxvalue used to
#construct the tree!
#modes: 0=maximise,1=minimise
def alphaRecurse(node,mode,maxValue,alpha=-1,beta=-1):
    if beta<0:
        beta=maxValue;

    if len(node.children)==0:
        return node.value;

    # maximise mode, find largest value from children
    if not mode:
        mode=1;
        minmax=-1;

    #minimise mode, find smallest value from children
    else:
        mode=0;
        minmax=maxValue;

    for x in node.children:
        childValue=alphaRecurse(x,mode,maxValue,alpha,beta);

        #minimise mode (mode was switched)
        if not mode:
            minmax=min(minmax,childValue);
            beta=min(minmax,beta);

        else:
            minmax=max(minmax,childValue);
            alpha=max(alpha,minmax);

        if beta<=alpha:
            break;

    return minmax;

#give maxValue as the max value given to genTree
# mode: 0=maximise,1=minimise
def minmaxRecurse(node,mode,maxValue):
    if len(node.children)==0:
        return node.value;

    # maximise mode, find largest value from children
    if not mode:
        mode=1;
        minmax=-1;

    #minimise mode, find smallest value from children
    else:
        mode=0;
        minmax=maxValue;

    for x in node.children:
        childValue=minmaxRecurse(x,mode,maxValue);

        #minimise mode (mode was switched)
        if not mode:
            minmax=min(minmax,childValue);

        else:
            minmax=max(minmax,childValue);

    return minmax;

def main():
    root=snode.genTree(3,4,100);

    snode.levelPrint(root);

    print(minmaxRecurse(root,0,100));
    print(alphaRecurse(root,0,100));

def treerecurseTest1():
    newchildren=[];
    bob=snode.snode(value=10);
    newchildren.append(bob.addChilden(2));

    newchildren.append(newchildren[0][0].addChilden(2));
    newchildren.append(newchildren[0][1].addChilden(2));

    newchildren.append(newchildren[1][0].addChilden(2));
    newchildren.append(newchildren[1][1].addChilden(3));

    newchildren[2][0].value=9

    newchildren.append(newchildren[2][1].addChilden(2));

    newchildren[3][0].value=10;
    newchildren[3][0].value=13;
    newchildren[4][0].value=8;
    newchildren[4][2].value=2;
    newchildren[5][0].value=5;
    newchildren[5][1].value=6;

    newchildren.append(newchildren[4][1].addChilden(1));

    newchildren[6][0].value=17;


    snode.levelPrint(bob);

    print(minmaxRecurse(bob,0,20));
    print(alphaRecurse(bob,0,20,-1,20));

if __name__=="__main__":
    main();