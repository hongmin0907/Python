# Node Class 선언
class Node:
    def __init__(self, data=0):
        self.data = data # 데이터
        self.next = None # 다음 노드 값

class LinkedList:
    def __init__(self):
        self.head = Node() # 첫번째 노드를 갖고있는 header
    
    # 연결 리스트에 노드 추가
    def add(self, data):
        iterator = Node(data) # 새로운 노드 만듬 
        iterator.next = self.head.next # 새로운 노드의 다음 노드에 해더가 가지고있는 다음 노드를 넣는다
        self.head.next = iterator # 해더의 다음 노드는 새로운 노드가 된다

    # 연결 리스트의 노드 삭제
    def delete(self):
        # 연결 리스트가 비어있을 때 리턴
        if(self.head.next == None):
            print('연결리스트가 비었습니다.')
            return
        
        # 해더의 다음노드를 해더의 다음다음 노드로 교체한다
        # python의 garbage collection 특성을 이용하여 삭제할 노드는 그냥 참조를 0으로 만들어 준다
        self.head.next = self.head.next.next

    # 연결 리스트의 노드 검색 
    def search(self, data):
        # 연결 리스트가 비어있을 때 리턴
        if(self.head.next == None):
            print('연결리스트가 비었습니다.')
            return
        
        # 반복자는 해더의 다음 노드(연결리스트의 첫번째 노드)를 참조하고
        iterator = self.head.next
        
        # 반복문을 통해 연결리스트 전체를 검색한다.
        # 순회 할 땐 리스트의 맨 마지막 노드의 다음 노드를 가르키는 값은 None 이기 때문에 이걸 이용하여 반복문에 조건을 건다
        while(iterator != None):
            # 만약 찾고자 하는 데이터와 일치하면 값을 출력하고 리턴한다
            if iterator.data == data:
                print('값을 찾았습니다.', iterator.data)
                return
            iterator = iterator.next
        
        # 리스트의 모든 노드를 거쳤는데도 안나오면 값이 없다 출력하고 리턴한다
        print('값을 찾지 못했습니다.')
        return

    # 연결 리스트의 모든 노드의 데이터를 출력한다
    def print(self):
        # 연결 리스트가 비었을 때 리턴
        if(self.head.next == None):
            print('연결리스트가 비었습니다.')
            return
        
        # 반복자는 해더의 다음 노드(연결리스트의 첫번째 노드)를 참조하고
        iterator = self.head.next
        
        # 모든 노드를 순회하며 데이터를 출력한다.
        while(iterator != None):
            print(iterator.data, end=' ')
            iterator = iterator.next
        print()

# 이 파일이 main일 때 실행하는 조건문
if __name__=="__main__":
    linkedlist = LinkedList()
    linkedlist.add(5)
    linkedlist.add(4)
    linkedlist.add(3)
    linkedlist.add(6)
    linkedlist.print()
    linkedlist.delete()
    linkedlist.print()
    linkedlist.search(3)
    linkedlist.search(10)
        
