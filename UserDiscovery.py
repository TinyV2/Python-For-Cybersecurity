import os, wmi

w = wmi.WMI()

# Get list of administartor accounts
admins = None
for group in w.Win32():
    if group.Name == "Administrator":
        admins = [a.Name for a in group.associators(wmi_result_class = "Win32_UserAccount")]

# List user acounts on device
for user in w.Win32_UserAccounts():
    print("Username: %s" % user.Name)
    print("Administrator: %s" % (user.Name in admins))
    print("Disabled: %s" % user.Disabled)
    print("Local: %s" % user.LocalAccount)
    print("Password Changeable: %s"%user.PasswordChangeable)
    print("Password Expires: %s" % user.PasswordExpires)
    print("Password Required: %s" % user.PasswordRequired)
    print("\n")

# Print Windows Password Policy
print("Password Policy: ")
print(os.system("net accounts"))