import random;

class snode:
    id=0;
    leafs=1;

    # constructor takes parent node, and max randomised
    # value for the node. if value is provided, overwrites
    # randomised value.
    def __init__(self,parent=0,maxValue=-1,value=-1):
        snode.id+=1;
        self.id=snode.id;

        #neither maxvalue or value is given, node has no value
        if maxValue<0 and value<0:
            self.value=-1;
        #if maxvalue is given, randomise
        elif value<0:
            self.value=random.randint(0,maxValue);
        #if value is given, override maxvalue
        else:
            self.value=value;

        self.parent=parent;
        self.children=[];

    def __str__(self):
        return "n"+str(self.id);

    #advanced string print
    #prints out n<node id number> (p:<parent node>,c:<number of children>,v:<value of node>)
    #if node has no children or no value (for non leaf nodes) then it won't print out c or v
    def __repr__(self):
        childrenString="";
        if len(self.children)>0:
            childrenString=",c:{}".format(len(self.children));

        valueString="";
        if self.value>-1:
            valueString=",v:{}".format(self.value);

        return "n{} (p:{}{}{})".format(self.id,str(self.parent),childrenString,valueString);

    # generate children array for this node with maximum
    # amount of children and value, return the list of children
    # just generated
    def genChildren(self,minChildren=0,maxChildren=5,maxValue=100):
        newchildren=[];
        for x in range(random.randint(minChildren,maxChildren)):
            newchildren.append(snode(self,maxValue));
        self.children=newchildren;

        #no longer a leaf node
        if len(newchildren)>0:
            self.value=-1;
            snode.leafs-=1;

        snode.leafs+=len(newchildren);
        return newchildren;

    #add a certain amount of children, if an array of values its
    #provided, sets those children to those values
    def addChilden(self,amount=1,values=[]):
        self.value=-1;
        newChildren=[];
        for x in range(amount):
            newChildren.append(snode(self));

        if len(values)==len(newChildren):
            for i,x in enumerate(values):
                newChildren[i].value=x;

        for x in newChildren:
            self.children.append(x);

        return newChildren;

#generate a tree with given parameters
#maxheight=how high the tree can go
#maxchildren=max range to generate children between
#maxvalue=max random value a leaf node can have
#give it statusPrint=1 to print out stuff (so you dont get bored while its making a tree)
#<level>: <nodes created>/<total nodes for this level>
def genTree(maxHeight,minChildren,maxChildren,maxValue,progressPrint=0):
    root=snode(-1,50);
    nodeslist=[[root]];

    nodeslistLen=len(nodeslist);
    endMode="\r";

    for z in range(maxHeight):
        newNodeslist=[];

        nodeslistLen=len(nodeslist);
        endMode="\r";

        for ix,x in enumerate(nodeslist):
            if progressPrint:
                if ix==nodeslistLen-1:
                    endMode="\n";

                print("{}: {}/{}".format(z+1,ix+1,nodeslistLen),end=endMode,flush=True);

            for y in x:
                newNodeslist.append(y.genChildren(minChildren,maxChildren,maxValue));

        nodeslist=newNodeslist;

    return root;

#prints out a node and its children. labels each level with the initial
#node given as level 1
def levelPrint(node):
    nodes=[[node]];
    newNodes=[];
    i=1;

    while 1:
        print("level {}: ".format(i),end="");
        print(nodes);

        for x in nodes:
            for y in x:
                if len(y.children)>0:
                    newNodes.append(y.children);

        if len(newNodes)==0:
            return;

        nodes=newNodes;
        newNodes=[];
        i+=1;

def main():
    root=genTree(4,3,100);
    levelPrint(root);

if __name__=="__main__":
    main();