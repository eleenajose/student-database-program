condition=True
while(condition):
        student_info=input("enter student information in the following format(name age contact_number e-mail_id):")
        print("enter information:"+student_info)
        condition_check=input("enter (yes or no) if you want to:")    
        if condition_check=="yes":
            condition = True
        if condition_check=="no":
            condition = False
