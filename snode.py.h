class snode
{
  public:
    snode(snode parent,int maxValue);

    snode-array genChildren(int maxChildren,int maxValue);

  private:
    string __str__;
    string __repr__;
};

snode genTree(int maxHeight,int maxChildren,int maxValue);

void levelPrint(snode node);