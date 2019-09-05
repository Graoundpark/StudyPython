    
def func(a):
    print("입력숫자 : ", a)

if __name__ == "__main__": # 코드를 직접 수행할 때만 인식하고, 임포트해서 사용하면 수행하지 않음
    print("모듈을 직접 실행")
    func(3)
    func(4)
else: # 임포트 할 경우에만 수행
    print("Import네~")
