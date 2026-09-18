que = [0] * 1000000
front = rear = -1
for i in range(1000000):
    rear += 1
    que[rear] = i
print(rear)

# rear += 1  # enqueue(1)
# que[rear] = 1
# rear += 1  # enq 2
# que[rear] = 2 # enq 3
# rear += 1
# que[rear] = 3

# front += 1
# print(que[front])
# front += 1
# print(que[front])
# front += 1
# print(que[front])

# while front != rear:
#     front += 1
#     print(que[front])

# 밑에 코드(큐생성)랑 다른 점: 넣고 꺼내는 작업만 수행해서 지우는 작업은 수행하지 않음

# ========================================


q = [] # 큐 생성
q.append(1)
q.append(2)
q.append(3)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

for i in range(1000000):
    q.append(i)
print(len(q))
for _ in range(1000000):
    q.pop(0)
print(len(q))
