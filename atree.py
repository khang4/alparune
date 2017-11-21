import random;

class snode:
    def __init__(self,maxValue=100):
        self.value=random.randint(0,maxValue);
        self.children=[];

    def __repr__(self):
        return "n"+str(self.value);

    # generate children array for this node with maximum
    # amount of children and value
    def genChildren(self,maxChildren,maxValue):
        newchildren=[];
        for x in range(random.randint(0,maxChildren)):
            newchildren.append(snode(maxValue));
        self.children=newchildren;
        return newchildren;

def main():
    root=snode(50);
    nodeslist=[[root]];

    for x in range(3):
        newNodeslist=[];
        for x in nodeslist:
            for y in x:
                newNodeslist.append(y.genChildren(5,50));

        nodeslist=newNodeslist;

    print(newNodeslist);

if __name__=="__main__":
    main();