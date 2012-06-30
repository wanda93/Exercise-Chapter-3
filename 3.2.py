hours = raw_input ('Enter Hours:')
rate  = raw_input ('Enter Rate:')

try:					#mengecek hasil input
  pay = int (hours) * int (rate)	
  print 'Pay:', (pay)

except:		#menampilkan jika yg di input buka integer
  print 'Error, Please Enter Numeric input:' 
