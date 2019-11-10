class User:
    def say_hello(some_user):
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))

user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "78978"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "79453"

# static 함수처럼 <클래스이름.메소드> 이런식으로 호출하는데,, 파이썬은 가능?
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)