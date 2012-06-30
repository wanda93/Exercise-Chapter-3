enter = raw_input ('Enter Score:')	#meminta input dari user

score = float(enter)

if score >= 1.0:		#bagian dari pengecekan	
        print 'Bad Score'

elif score >= 0.9:
        print 'A'	

elif score >= 0.8:
	print 'B'

elif score >= 0.7:
        print 'C'

elif score >= 0.6:
        print 'D'

elif score < 0.6:
	print 'E'

elif score > 10:		#jika yg diinput>10 tampilkan error
	print 'Error'
