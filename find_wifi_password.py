import subprocess

#store profiles in a variable
profiles_data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8',errors='backslashreplace').split('\n')

#covert profile data to list we use [1] becuase the second item is wifi name we use [1:-1] because first and last char is useless. 
profiles = [i.split(':')[1][1:-1] for i in profiles_datadata if 'All User Profile' in i]

#checking adn printing the wifi passwords
for i in profiles:
    #checking passwords
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',i,'key=clear']).decode('utf-8',errors='backslashreplace').split('\n')
    #convertign passwords to list and storing them
    results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
    #printing passwords by using try except method
    try:
        print('{:<30}|{:<}'.format(i,results[0]))
    except IndexError:
        print('{:<30}|{:<}'.format(i,''))

        