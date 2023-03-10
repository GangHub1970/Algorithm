# 전위순회
def preorder(node):
  if node != '.':
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

# 중위순회
def inorder(node):
  if node != '.':
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

# 후위 순회
def postorder(node):
  if node != '.':
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')

graph = {'A': ['B', 'C'],
         'B': ['D', '.'],
         'C': ['E', 'F'],
         'D': ['.', '.'],
         'E': ['.', '.'],
         'F': ['.', 'G'],
         'G': ['.', '.']}

preorder('A')
print()
inorder('A')
print()
postorder('A')