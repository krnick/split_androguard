from androguard.misc import AnalyzeAPK


a ,d, dx = AnalyzeAPK("14d9f1a92dd984d6040cc41ed06e273e.apk")


print(a.get_permissions)
