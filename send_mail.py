 import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("dhirajsharma884417@gmail.com","Dhiraj@3103") 
message = "this is trial message"
s.sendmail("dhirajsharma884417@gmail.com", "firsttalk26@gmail.com", message) 
s.quit()
