hours = raw_input ('Enter Hours:')
rate  = raw_input ('Enter Rate:')

jam = float(hours)
byr = float(rate)

if jam < 40:		#kondisi 1 jika jam<40 kalikan saja
   print jam * byr

else :			#kondisi 2 jika jam>40 maka kalikan 3/2
   nrml = 40 * byr
   ext = jam - 40
   bnus = (byr*3/2) * ext
   total = nrml + bnus	
   print ('pay :'), float(total)
