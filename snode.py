import random;

class snode:
    id=0;

    # constructor takes parent node, and max randomised
    # value for the node
    def __init__(self,parent=0,maxValue=100):
        snode.id+=1;
        self.id=snode.id;
        self.value=random.randint(0,maxValue);
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
    def genChildren(self,maxChildren,maxValue=100):
        newchildren=[];
        for x in range(random.randint(0,maxChildren)):
            newchildren.append(snode(self,maxValue));
        self.children=newchildren;

        if len(newchildren)>0:
            self.value=-1;

        return newchildren;

# generate a tree with given parameters
def genTree(maxHeight,maxChildren,maxValue):
    root=snode(-1,50);
    nodeslist=[[root]];

    for x in range(maxHeight):
        newNodeslist=[];
        for x in nodeslist:
            for y in x:
                newNodeslist.append(y.genChildren(maxChildren,maxValue));

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