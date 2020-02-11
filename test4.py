from datetime import datetime

now = datetime.now()

fds = 7

result = fds - now.day

print ("\n Faltam",result,"dias para acabar a semana!\n")