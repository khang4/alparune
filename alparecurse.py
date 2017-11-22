import snode;

def main():
    root=snode.genTree(3,4,100);

    snode.levelPrint(root);

    rtest(root);

def rtest(node):
    if len(node.children)==0:
        print(node);

    for x in node.children:
        rtest(x);

if __name__=="__main__":
    main();