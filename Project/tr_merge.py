# filenames = ['differnt.txt', 'differnt1.txt', 'different2.txt']
with open("features_tr_1.txt") as xh:
  with open('features_tr_2.txt') as yh:
  	with open('features_tr_3.txt') as zh:
  		with open("tr_finalfeatures.txt","w") as fl:
  			xlines = xh.readlines()
  			ylines = yh.readlines()
  			zlines = zh.readlines()
  			for line1, line2, line3 in zip(xlines, ylines, zlines):
  				if not line3.strip():
  					fl.write("{} {} {}\n".format(line1.rstrip(), line2.rstrip(), "null"))
  				else:
  					fl.write("{} {} {}\n".format(line1.rstrip(), line2.rstrip(), line3.rstrip()))