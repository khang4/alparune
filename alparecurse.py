import snode;

def main():
    # root=snode.genTree(3,4,100);

    # snode.levelPrint(root);

    # print(alpharecurse(root,0,100));

    bob=snode.snode(value=10);
    bob.addChilden(3,[0,1,5]);

    snode.levelPrint(bob);

#give maxValue as the max value given to genTree
# mode: 0=maximise,1=minimise
def alpharecurse(node,mode,maxValue):
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
        childValue=alpharecurse(x,mode,maxValue);

        #minimise mode (mode was switched)
        if not mode:
            minmax=min(minmax,childValue);

        else:
            minmax=max(minmax,childValue);

    return minmax;

if __name__=="__main__":
    main();