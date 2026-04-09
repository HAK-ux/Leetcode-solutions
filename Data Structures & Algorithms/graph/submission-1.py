class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False
        
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        
        def dfs(node):
            if node == dst:
                return True
            if node in visit:
                return False
  
            visit.add(node)

            for neighbor in self.adjList.get(node, []):
                if dfs(neighbor):
                    return True

            return False
            
        return dfs(src)

