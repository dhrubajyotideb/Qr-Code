import qrcode
user_input=input("Enter Your Number/URL/UPI Id:")
print("you entered:",user_input)
userqr= qrcode.make(user_input)
userqr.save("userqr.png") 