with open("features_tr_test_1.txt") as xh:
  with open("features_tr_test_2.txt") as yh:
    with open("si_finalfeatures_test.txt", "w") as fl:
      xlines=xh.readlines()
      ylines=yh.readlines()
      for line1, line2 in zip(xlines, ylines):
        fl.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))