# # filenames = ['differnt.txt', 'differnt1.txt', 'different2.txt']
# with open("features_si_1.txt") as xh:
#   with open('features_si_2.txt') as yh:
#   	with open('features_si_3.txt') as zh:
#       with open('si_values_attr.txt') as ph:
#         with open('si_finalfeatures.txt','w') as fl:
#           xlines = xh.readlines()
#           ylines = yh.readlines()
#           zlines = zh.readlines()
#           plines = ph.readlines()
#           for line1, line2, line3, line4 in zip(xlines, ylines, zlines, plines):
#             fl.write("{} {} {} {}\n".format(line1.rstrip(), line2.rstrip(), line3.rstrip(), line4.rstrip()))
#   		

with open("features_si_1.txt") as xh:
  with open("features_si_2.txt") as yh:
    with open("si_values_attr.txt") as cl:
      with open("si_finalfeatures.txt", "w") as fl:
        xlines=xh.readlines()
        ylines=yh.readlines()
        clines=cl.readlines()
        for line1, line2, line4 in zip(xlines, ylines, clines):
          fl.write("{} {} {}\n".format(line1.rstrip(), line2.rstrip(), line4.rstrip()))