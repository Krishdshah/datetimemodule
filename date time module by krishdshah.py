def datetime_module():
  def isleap(y):
    if (y%4==0 and y%100!=0) or y%400==0:
      return True
    else:
      return False

  m={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

  year=int(input('ENTER YEAR: '))
  month=int(input('ENTER MONTH: '))
  while month<1 or month >12:
    month=int(input('ENTER MONTH(btw 1 to 12): '))
  days=int(input('ENTER DAY: '))
  while days<1 or ((days>m[month]) or (days>(m[month]+1) and isleap(year))):
    days=int(input('ENTER DAY(in month\'s range): '))

  maxd=int(input('Enter No. of days to be added:'))

  for i in range(1,maxd+1):
    if month!=12 or days!=31:
      if isleap(year) and month==2:
        if days<m[month]+1:
          days+=1

        else:
          days=1
          month+=1

      else:
        if days<m[month]:
          days+=1
         
        else:
          days=1
          month+=1
          
    else:
      day=1
      month=1
      year+=1
      

  print()
  print(days,'/',month,'/',year)

datetime_module()
