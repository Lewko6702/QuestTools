import os, sys, ctypes, urllib.request, time, zipfile
from BonkLib import Logging

ctypes.windll.kernel32.SetConsoleTitleW("Quest Tools")



Logging.StartUp(Tag='Quest Tools')
os.system('cls')

print('Checking for ADB Requirements')
time.sleep(1)

if os.path.isfile('adb.exe'):
    Logging.Success('The ADB Requirements are already downloaded!\n Skipping.')
    time.sleep(2)
else:
    Logging.Warning("The ADB Requirements don't exist!\n Downloading...")
    time.sleep(5)
    url = 'https://cdn.discordapp.com/attachments/795101766425378856/1087570116151091231/Requirements.zip'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        awa = urllib.request.urlopen(req).read()         
        try: 
            with open('Requirements.zip', 'wb') as zipfiles:
                zipfiles.write(awa)         
            with zipfile.ZipFile('Requirements.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.remove('Requirements.zip')
        except Exception as e:
            Logging.Error(e)
            Logging.Info('Failed to unzip Msg Cutie Lewko#4945\n The program will close in 5 seconds.')
            time.sleep(5)
            sys.exit()
    except Exception as e:
        Logging.Error(e)
        Logging.Info('ADB Requirements Failed to download please Msg Cutie Lewko#4945 on Discord!\n The program will close in 5 seconds.')
        time.sleep(5)
        sys.exit()

menu = """
    0: Exit.
    1: APK Install
    2: Enable Wireless
    3: Proximity Sensor On
    4: Proximity Sensor Off
    5: Reboot
    6: Reboot Bootloader
    7: Uninstall App
"""

def apkInstall():
    print('Look at the top of your screen to see if your devices says unauthorised if it just says device that is good.')
    x = input('Paste .apk name here:' )
    os.system(f'adb install -r -t -d -g {x}')
    os.system("pause")
    

def enableWireless():
   os.system('adb tcpip 5555') 
   os.system('pause')
   os.system('clear')

def proxsensorOn():
   os.system('adb shell am broadcast -a com.oculus.vrpowermanager.automation_disable')
   os.system('pause')

def proxsensorOff():
   os.system('adb shell am broadcast -a com.oculus.vrpowermanager.prox_close')
   os.system('pause')

def Reboot():
   os.system('adb reboot')
   os.system('pause')

def rebootBootloader():
   os.system('adb reboot Bootloader')
   os.system('pause')
   

def uninstallApp():
   Logging.Info('example com.facebook.horizon)')
   c = input('Type app to uninstall here: ')
   os.system(f'adb uninstall {c}')
   os.system('pause')
   os.system('cls')

while True:
    try:     
        os.system("cls && adb devices")
        os.system('adb shell getprop ro.product.odm.model')
        print(menu)
        a = int(input('Choose an option: '))
        match a:
            case 0:
                print("Exiting program...")
                sys.exit()
            case 1:
                apkInstall()
            case 2:
                enableWireless()
            case 3:
                proxsensorOn()
            case 4:
                proxsensorOff()
            case 5:
                Reboot()
            case 6:
                rebootBootloader()
            case 7:
                uninstallApp()
            case _:
                print("Invalid option. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")