### Connected component (graph theory)
* 8 May

## Python lib:
* sys
* json
* ast
* networkx
* matplotlib.pyplot
* PyQt4

<img src="/img/graph.png" height="688 " width="681" />

## How to start?
* Download all lib using pip install
* ```
python gui.py

```
* input type edges and connections between them like json:
```
{
  0: [1,2,3],
  1: [],
  2: [1],
  3: [4,5],
  4: [3,5],
  5: [3,4,7],
  6: [8],
  7: [],
  8: [9],
  9: []
}

```


## Algorythm getRoots

```
def getRoots(aNeigh):
    def findRoot(aNode,aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode,aRoot[aNode][1])
    myRoot = {}
    for myNode in aNeigh.keys():
        myRoot[myNode] = (myNode,0)
    for myI in aNeigh:
        for myJ in aNeigh[myI]:
            (myRoot_myI,myDepthMyI) = findRoot(myI,myRoot)
            (myRoot_myJ,myDepthMyJ) = findRoot(myJ,myRoot)
            if myRoot_myI != myRoot_myJ:
                myMin = myRoot_myI
                myMax = myRoot_myJ
                if  myDepthMyI > myDepthMyJ:
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax,max(myRoot[myMin][1]+1,myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0],-1)
    myToRet = {}
    for myI in aNeigh:
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh:
        myToRet[findRoot(myI,myRoot)[0]].append(myI)
    return myToRet

```
