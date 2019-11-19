class user:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):
        if ( self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호 입니다.")


user1 = user()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

# user1.login(user1, "captain@codeit.kr", "12345")  ### 에러!
user1.login("captain@codeit.kr", "12345")