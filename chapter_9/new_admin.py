from admin import Privileges, Admin

ojenkins = Admin('osei', 'jenkins', 30, 'programmer', 'dallas')
ojenkins.privileges.show_privileges()
