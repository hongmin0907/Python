class Node:
    # 생성자
    def __init__(self, data=None):
        """
        self.__data는 저장할 데이터
        self.__next는 다음 노드를 가르킴
        """
        self.__data=data
        self.__next=None
    
    # self.__data에서 데이터를 가져올 때
    @property
    def data(self):
        return self.__data

    # self.__data에 데이터를 변경할 때
    @data.setter
    def data(self, data):
        self.__data = data

    # self.__next에서 데이터를 가져올 때
    @property
    def next(self):
        return self.__next

    # self.next에 데이터를 변경할 때
    @next.setter
    def next(self, next):
        self.__next = next

class LStack:
    # 생성자
    def __init__(self):
        self.top = None

    # 스택이 비었으면 True, 아니면 False 반환 
    def empty(self):
        if self.top:
            return False
        else:
            return True
    
    # 스택에 데이터를 넣을 때
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top # 새로운 데이터의 다음 데이터는 스택의 맨 처음 데이터 이다
        self.top = new_node # 새로운 데이터를 스택의 맨 앞에 넣는다
    
    # 스택에서 데이터를 빼올 때
    # Python은 garbage collection과 reference counting을 통해 아무도 참조하지 않은 객체는 자동 삭제된다.
    # 그러므로 노드 객체는 따로 삭제하지 않는다
    def pop(self):
        
        # 스택이 비었는지 확인
        if self.empty():
            return None

        cur = self.top # 스택의 맨 앞에 데이터를 가져온다. 
        self.top = self.top.next # 이제 스택의 맨 처음은 가져온 데이터의 다음 데이터이다
        return cur.data # 가져온 노드의 데이터를 반환한다

    # 스택의 맨 첫번째 데이터가 무엇인지 확인할 때
    # 이는 노드를 비어주지 않고 첫번째 노드에 어떤 데이터가 있는지 보여줄 때 사용된다.
    def peek(self):

        # 스택이 비었는지 확인
        if self.empty():
            return None
        return self.top.data

# 이 파일이 main일 때 실행하는 조건문
if __name__=="__main__":

    s = LStack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    while not s.empty():
        print(s.pop(), end=" ") # end=" " 은 데이터를 화면에 출력한 후 띄어쓰기 하는 것
