"""
1. Write a recursive program to find the squared sum of N natural numbers e.g.
"""
def squared_sum(N):
   
    if N==0:
        return 0
    else:
        return N*N + squared_sum(N-1)

"""
2. Write a program to find a Preorder, Inorder and Postorder traversal of 3-ary Tree.

"""

def traversal_order(graph):
    node_stack=Stack()
    
    keys=list(graph.keys())
    root=keys[0]
    visited={x:0 for x in keys}
    traversal={"Pre":"","Post":"","In":""}
    node_stack.push(root)
    while(not node_stack.isEmpty()):
        # print("traversal :",traversal)
        node=node_stack.peek()
        # node_stack.display()
        # print("node ",node)
        if is_leaf(graph[node]):
            for order in traversal.keys():
                traversal[order]+=str(node)+","
            visited[node]=3
            node_stack.pop()
           
            # print("back tracking")
                
            continue
        visited[node]+=1
        if (visited[node]==1):
            traversal["Pre"]+=str(node)+","            
        if (visited[node]==2):
            traversal["In"]+=str(node)+","
        if (visited[node]==4):
            traversal["Post"]+=str(node)+","            
        #find its remaining children
        child=graph[node]
        # print("child: ",child)
        found_child=has_unvisited_child(child,visited)
        if found_child !=None:
            # print("child found",found_child)
            node_stack.push(found_child)
        else:
            # print("backtracking no child left ")
            node_stack.pop()

    return traversal



"""

4. Write a program to implement the breadth first search(BFS) and depth first search(DFS) in graph.

"""
from Queue import Queue
def BFS(graph):
    sequence=""

    number_of_node=len(graph.keys())
    # print("no nodes ",number_of_node)
    
    graph_queue=Queue(number_of_node)
    keys=list(graph.keys())
    # print("keys: ",keys)
    
    graph_queue.enqueue(keys[0])
    visited={key:0 for key in keys}
    visited[keys[0]]=1
    
    while(not graph_queue.isEmpty()):
        # print("queue ",graph_queue.display())
        node=graph_queue.dequeue()
        # print("node ",node)
        
        sequence+=str(node)
        
        child_nodes=graph[node]
        # print("child:",child_nodes)
    
        for nodes in child_nodes:
            if not visited[nodes]:
                graph_queue.enqueue(nodes)
                visited[nodes]=1
        # print("visited: ",visited)            

    return sequence
from stack import Stack
def DFS(graph):
    node_stack=Stack()
    keys=list(graph.keys())
    root=keys[0]
    # print("root: ",root)
    node_stack.push(root)
    visited={x:0 for x in keys}
    result=""
    while(not node_stack.isEmpty()):    

        # node_stack.display()
        node=node_stack.peek()
        # print("node :",node)
        if not bool(visited[node]):

            # print("node :",node)
            result+=str(node)
            visited[node]=1
        child=graph[node]
        # print("child :",child)
        # print("visited :",visited)
    
        found_child=has_unvisited_child(child,visited)
        if found_child != None:
            # print("child found :",found_child)
            node_stack.push(found_child)
        else:
            # print("backtracking")
            node_stack.pop()    
    return result




    
def has_unvisited_child(child,visited):
    for childs in child:
        if( not bool(visited[childs])):
            return childs
    return None    



def is_leaf(child):
    if len(child)==0:
        return True
    return False

"""

3. Write a program to solve the recurrence relation T(N)=2T(N/2)+N

5. Write a program to identify the Eulerian and Hamiltonian circuits in a given graph.
6. Write a program to identify that the given graph is planar or not.

"""


graph={1:[3,5],3:[1,5,6],5:[1,3,6,4],4:[5,7],6:[3,5,7],7:[6,4]}
graph2={1:[2,3],2:[1,4,5],3:[1,5],4:[5,6],5:[6,3,2],6:[4,5]}
# number_of_nodes=int(input())
graph4={1:[2,3,4],2:[5,6,7],3:[8,9,10],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
print("BFS ",BFS(graph2))
graph3={1:[2,3,4],2:[5,6,7],3:[],4:[],5:[],6:[],7:[]}
print("DFS",DFS(graph2))
print(traversal_order(graph4))


n=int(input("enter upper value of N to calculated squared sum of \"N \"Natural Numbers  :"))
print("squared sum :",squared_sum(n))



