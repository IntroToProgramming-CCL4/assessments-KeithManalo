# i used the % operator to get the remainder and int on pmany to get whole numbers
money = 50
usb = 6
pleft = money%usb
pmany = int(money/usb)
print('with £',money,'\nyou can buy',pmany,'usb\nyour change is £', pleft)
