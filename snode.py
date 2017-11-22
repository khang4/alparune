import random;

class snode:
    # constructor takes parent node, and max randomised
    # value for the node
    def __init__(self,parent=0,maxValue=100):
        self.value=random.randint(0,maxValue);
        self.parent=parent;
        self.children=[];

    def __str__(self):
        return "n"+str(self.value);

    #advanced str representation: {node value} ({parent value},{number of children})
    def __repr__(self):
        return "n{} ({},{})".format(self.value,str(self.parent),len(self.children));

    # generate children array for this node with maximum
    # amount of children and value, return the list of children
    # just generated
    def genChildren(self,maxChildren,maxValue=100):
        newchildren=[];
        for x in range(random.randint(0,maxChildren)):
            newchildren.append(snode(self,maxValue));
        self.children=newchildren;
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