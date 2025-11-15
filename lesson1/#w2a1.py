#w2a1
print('hello world!')

#w2a2
a=input('Hãy nhập tên bạn:')
print('xin chào ',a)

#w2a3
a,b=map(int,input('nhập 2 số nguyên a,b:').split())
print('tổng hai số là:',a+b)
print('hiệu hai số là:',a-b)
print('tích hai số là:',a*b)
print('a chia b được phần nguyên là:',a//b)
print('a chia b dư:',a%b)
print('a chia b được:',(round(a/b,2)))




#w2a4
a1,b1,c1,a2,b2,a3=map(float,input('Nhập điểm 6 môn theo thứ tự:').split())
m=((a1+b2+c1)+(a2+b2)*2+(a3)*3)/10
print('điểm trung bình là:','%.1f'%m)

#w2a5
a,b=map(int,input('Nhập 2 số nguyên a,b').split())
print("a^b=",a**b)

#w2a6
ma=(input('nhập một chữ cái bất kì từ a đến z:'))
print('mã unicode của từ đó là:',ord(ma))
print('in hoa mã unicode: ',ma.upper())

#w2a7
print( ((13 ** 2) * 3) + 5)
print( 13**2*3 + 5)

#w2a8
nhietdo=int(input('nhập nhiệt độ C:'))
print('nhiệt độ theo thang F là:',round(nhietdo*9/5+32,2))

#w2a9
gia=int(input('nhập giá chiếc đồng hồ:'))
print('tổng tiền mà đạt phải trả là:',round(gia*1.4+10,2),'usd')


#w2a10
a,b,c=input('nhập tên 3 người:').split()
print('hi', c,b,a)

#w2a11
x,y=map(int,(input('nhập vào giờ và phút:').split()))
print('chuyển sang giây:',(x*3600)+(y*60))

#w2a12
a=int(input('nhập độ dài cạnh khối rubik:'))
print('số miếng dán cần dùng để phủ kín rubik là:',(a**2)*6)

#w2a13
a,b=map(input,('nhập vào 2 số nguyên a,b:').split())
print('hàng đơn vị khi a nhân b là:'(a*b)%10)

#w2a14
a=100
b=200
a,b=b,a
print(a,b)

#w2a15
n = int(input("Nhập một số nguyên dương n: "))
if n > 0:
    sosao = 3 * n * (n - 1) + 1
    print("Số sao thứ", n, "là:", sosao)
else:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")



#w2a16
print("Spring\nSummer\nAutumn\nWinter")

#w2a17
print('  *')
print(' ***')
print('*****')

#w2a18
print('### # #  ### ### ')
print(' #  #  #  #   # ')
print(' #  #   # #   # ')
print(' #  #  #  #   # ')
print(' #  # #   #   # ')

#w2a19
print("Monday")
print("Tuesday")
print("Wednesday")
print("Thursday")
print("Friday")
print("Saturday")
print("Sunday")

#w2a20
import calendar

for month in calendar.month_name[1:]:
    print(month)

#w2a21
print(("Hello, world\n" * 10).strip())










