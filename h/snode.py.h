class snode
{
    static int id; //running id count for nodes, can be used as total number of nodes
    static int leafs; //number of leaf nodes

  public:
    snode(snode parent,int maxValue,int value);

    int id;
    int value;
    snode parent;
    snode-array children;

    snode-array genChildren(int maxChildren,int maxValue);
    snode-array addChildren(int amount,int-array values);

  private:
    string __str__;
    string __repr__;
};

//progressprint is optional, defaults to 0
snode genTree(int maxHeight,int minChildren,int maxChildren,int maxValue,(int progressPrint));

void levelPrint(snode node);