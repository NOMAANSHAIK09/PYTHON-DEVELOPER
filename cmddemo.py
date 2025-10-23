import sys
xInt=int(sys.argv[1])
yInt=int(sys.argv[3])
operator=sys.argv[2]
if(operator == '+'):
     print("addition : ",xInt+yInt)
elif(operator == '-'):
      print("subtitution : ",xInt-yInt)
elif(operator == '*'):
      print("multiplication : ",xInt*yInt)
elif(operator == '/'):
      print("division : ",xInt/yInt)
elif(operator == '**'):
      print("square : ",xInt**yInt)
else:
    print("invalid operastor")
