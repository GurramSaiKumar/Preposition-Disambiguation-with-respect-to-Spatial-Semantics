with open("differnt.txt") as xh:
  with open("differnt1.txt") as yh:
    with open("different2.txt") as zh:
      with open("lm_values_attr.txt") as cl:
        with open("lm_finalfeatures.txt", "w") as fl:
          xlines=xh.readlines()
          ylines=yh.readlines()
          zlines=zh.readlines()
          clines=cl.readlines()
          for line1, line2, line3, line4 in zip(xlines, ylines, zlines, clines):
            fl.write("{} {} {} {}\n".format(line1.rstrip(), line2.rstrip(), line3.rstrip(), line4.rstrip()))