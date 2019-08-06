class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def add(self, data):
        iterator = Node(data)
        iterator.next = self.head.next
        self.head.next = iterator

    
    def delete(self):
        if(self.head.next == None):
            print('연결리스트가 비었습니다.')
            return
        
        self.head.next = self.head.next.next

    def search(self, data):
        if(self.head.next == None):
            print('연결리스트가 비었습니다.')
            return
        iterator = self.head.next
        
        while(iterator != None):
            if iterator.data == data:
                print('값을 찾았습니다.', iterator.data)
                return
            iterator = iterator.next
        
        print('값을 찾지 못했습니다.')
        return

    def print(self):
        if(self.head.next == None):
            print('연결리스트가 비었습니다.')
            return
        iterator = self.head.next
        
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

        
