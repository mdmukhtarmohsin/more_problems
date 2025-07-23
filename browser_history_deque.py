from collections import deque
dq = deque(maxlen=5)


def add_new_page(url):
    if len(dq) == dq.maxlen:
        dq.popleft()
    dq.append(url)


def go_back():
    if len(dq) > 1:
        dq.pop()

def go_forward():
    if len(dq) > 1:
        dq.appendleft(dq.pop())

def get_history():
    return list(dq)

print(get_history())
add_new_page("https://www.google.com")
add_new_page("https://www.youtube.com")
add_new_page("https://www.facebook.com")
add_new_page("https://www.instagram.com")
add_new_page("https://www.twitter.com")
print(get_history())
go_back()
print(get_history())
go_forward()
print(get_history())
