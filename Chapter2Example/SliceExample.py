string = 'abcdefghijklmnopqrstuvwxyz'
print(string[0], string[25]+'\n') #문자열은 배열이다
##Slice 는 a:b로 사용한다면 a에서 b에 해당하는 인덱스까지 문자열을 자르는 것이다. a 와 b를 생략할 경우 각각 처음부터, 끝까지 의 의미를 가지게 된다.
print('slice example 1 : ' + string[2:5])
slice1 = string[:] # string[:] = string[0:]
print('length of the string : ' + str(len(string)))
