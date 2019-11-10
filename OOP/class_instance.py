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

# 인스턴스 메소드의 특별한 규칙
User.say_hello(user1)   # 클래스에서 메소드를 호출
user1.say_hello()       # 인스턴스의 메소드를 호출, user1의 인스턴스가 say_hello의 파라미터로 자동으로 들어감

# 22, 23번 줄은 서로 같다.

# 에러(파라미터가 1개인데 2개 받았다고 에러남)
#User.say_hello(user1, user1)
#user1.say_hello(user1)
