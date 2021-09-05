import threading
import time
import sys
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import os
import time
import random
import time
import requests


artok = ["1919075128:AAGR3ga5vpv-2A0CF2MPQSQPIVocOvaU2WQ", #right
        "1970484110:AAHgexW8GPu-pQzGDS7-R0_gWa1zu-Zwr8Y", 
        "1859867395:AAGg7CmM4a94OVuh3Sbnn5Lx4w3CURKktCo", 
        "1763276556:AAFg7ggrBP2tydPhg68kZva0W0HbTPET79E" ,
        "1963495959:AAGJHXWheC1LfXXp0_cqXaOiefc7CZgaha4",
         
         "539758075:AAGm1fgY2NnHRSfX1aN9xeb0nQY3BNwrkDA", #honar
         "534358913:AAHM3ygWPvA-WBGux84VhNI4Qvk6mjPajaI",
         "543753995:AAEz9K7TCZ7bnqOrTOQQFvyMJZj4NGUoO-E",
         "463825537:AAGKmXrX3lop7dtSNKs1cn0du-3reS63Kzg",
         "508989186:AAFIuypztaI_svG8nK44mnj6ufbtzvRAJ5A",
         "479615315:AAEQIIcH9iQ7ontmfq4T_Bpaqpl-H5N1CvI",
         "524730204:AAHCp509r1Bxo_5zvmupj1mN2pM2BjClong",
         "526881191:AAH0KomVNQEvsec7RtvaAgd6fxl1cx8vlyo",
         "538947997:AAER1V17VlpB-WcYoXriQdm-de1P4jFHLAU",
         "513612786:AAGnJe7jq2somQBbRXJ1A8aaz7VqnR6loTA",
         "537742361:AAEG40yU72cvFqd8TU24UfVn4ozsHHzpnD8",
         "486768175:AAH2_hUhLBhstemkAZhBpHrglev1o9es08g",
         "450368228:AAHehLntrSeRtC7Wv-BILfVqEfIFy1uwK2w",
         "532113062:AAGJTwTFfP-TpbtKmOYpjcMJgp8yr1Ribdc",
         "458059023:AAGqGJUZmxteDOA8PRUu94ouQBxDgfYAcq0",
         "487250873:AAFjaU4GAO3VTegI4faauBIfOlOMMA7cWgU",
         "509076872:AAFT0vIU6Gj1Wx5Cwq7yuc3EYlcm7x-oQZU",
         "385550106:AAFAP02yw4xYK19ZOJsNUDciVSGYDWWFaVY",
         "474946478:AAHko9lDSqeYV2nMkp7EYZXEUcXn53hdsds",
         "525556349:AAFdH4CygABDkuFfeVfh1CRT9usvW_lrEzc",#honar


         "1908202736:AAGv62QyfnFLlwowkFL-u86fVV4yfx2foac",#iran
         "1903741816:AAGGC55OAVur1yTZIkb5MB5hREpv0uSF1zI",
         "1957087639:AAGzU9PteQO3LyxvGbN48f_KBlr790zsjwM",
         "1935084810:AAG-lA1DuBXnBCBMSqZbZAoBq3ygcEmlK6k",
         "1989210053:AAEHx_afLXA8Sr91vwXqG7yv2xfeMn_okQU",
         "1959028865:AAFB_MEG3wWWFsIIif9rnZpm8RiHZN3yL6k",
         "1988775924:AAGbHs0JxSn5CQZ5CE9vVCNrYGrP0l6PS1I",
         "1983684712:AAGdYRLW9neOUCt-c27Fkbt23REmLE2wvb4",
         "1963519932:AAGJ2a0_NZGReTnMH8UdvGkoE6lsgfGTeyw",
         "1987116834:AAGW3cbBnw9z5JKSuJW3M_p6td1dekBN-5o",
         "1980392065:AAHL36hdDe86kf-g8cHMRCj0yhgd_WIekeU",
         "1965220515:AAGciRNrZ7vPhu3lbF-hZRU_XYFyT-UKKEs",
         "1933873492:AAHq7Mr2ceoNDfjlwy4upS9BoJHDHiBLAsA",
         "1900693776:AAFIHRVavGb-GJhgEkMnNsrP54Se-HBJPxY",
         "1803645260:AAGeyIyFdF_FzwrY5FchtuD4mGrvKr2IAT4",
        ]


def runn(tokenn):
    cont=0
    s=""
    x=0
    url = 'https://api.telegram.org/bot'+tokenn+'/sendMessage?chat_id=1952047235'
    while True:
      cont=cont+1
      private_key =os.urandom(32)
      public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
      addr = keccak_256(public_key).digest()[-20:]
      addr=addr.hex()
      private_key=private_key.hex()
      s=s+str(addr)+"\n"+str(private_key)+"\n"
      if cont>37:
        myobj = {'text':str(s)}
        rs = requests.post(url, data = myobj)
        time.sleep(3)
        cont=0
        s=""
        rs=""
        myobj=""
if __name__ == "__main__":
    i=0
    while i<len(artok):
     x = threading.Thread(target=runn, args=(artok[i],))
     x.start()
     i=i+1
 
