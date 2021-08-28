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
def runn(tokenn):
    cont=0
    s=""
    x=0
    url = 'https://api.telegram.org/bot'+tokenn+'/sendMessage?chat_id=-1001505422887'
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
    x = threading.Thread(target=runn, args=("1803645260:AAGeyIyFdF_FzwrY5FchtuD4mGrvKr2IAT4",))
    x.start()
    x = threading.Thread(target=runn, args=("1900693776:AAFIHRVavGb-GJhgEkMnNsrP54Se-HBJPxY",))
    x.start()
    x = threading.Thread(target=runn, args=("1933873492:AAHq7Mr2ceoNDfjlwy4upS9BoJHDHiBLAsA",))
    x.start()
    x = threading.Thread(target=runn, args=("1965220515:AAGciRNrZ7vPhu3lbF-hZRU_XYFyT-UKKEs",))
    x.start()
    x = threading.Thread(target=runn, args=("1963519932:AAGJ2a0_NZGReTnMH8UdvGkoE6lsgfGTeyw",))
    x.start()
    x = threading.Thread(target=runn, args=("1821545885:AAEMLKhumxeT301ULjZLADE0vLocRbpWhxo",))
    x.start()
    x = threading.Thread(target=runn, args=("1960665369:AAFgaJP5oUYHzGkTcqTphhjIFeGGFIhFoMA",))
    x.start()
    x = threading.Thread(target=runn, args=("1964390176:AAHvHS6X8IB5N9YF6qwPrvgd8ngVQV96aYY",))
    x.start()
    x = threading.Thread(target=runn, args=("1965873162:AAF9nfTxfC_S1n5b46leTG4WhGGsO-yfecI",))
    x.start()
    x = threading.Thread(target=runn, args=("1980331526:AAEATFMEcnh4we_8RA2UA9isodT1Rb0mRdM",))
    x.start()
    x = threading.Thread(target=runn, args=("1980392065:AAHL36hdDe86kf-g8cHMRCj0yhgd_WIekeU",))
    x.start()
    x = threading.Thread(target=runn, args=("1983684712:AAGdYRLW9neOUCt-c27Fkbt23REmLE2wvb4",))
    x.start()
    x = threading.Thread(target=runn, args=("1987116834:AAGW3cbBnw9z5JKSuJW3M_p6td1dekBN-5o",))
    x.start()
    x = threading.Thread(target=runn, args=("1988775924:AAGbHs0JxSn5CQZ5CE9vVCNrYGrP0l6PS1I",))
    x.start()
    x = threading.Thread(target=runn, args=("1959028865:AAFB_MEG3wWWFsIIif9rnZpm8RiHZN3yL6k",))
    x.start()
    x = threading.Thread(target=runn, args=("539758075:AAGm1fgY2NnHRSfX1aN9xeb0nQY3BNwrkDA",))
    x.start()
    x = threading.Thread(target=runn, args=("534358913:AAHM3ygWPvA-WBGux84VhNI4Qvk6mjPajaI",))
    x.start()
    x = threading.Thread(target=runn, args=("543753995:AAEz9K7TCZ7bnqOrTOQQFvyMJZj4NGUoO-E",))
    x.start()
    x = threading.Thread(target=runn, args=("463825537:AAGKmXrX3lop7dtSNKs1cn0du-3reS63Kzg",))
    x.start()
    x = threading.Thread(target=runn, args=("508989186:AAFIuypztaI_svG8nK44mnj6ufbtzvRAJ5A",))
    x.start()
    x = threading.Thread(target=runn, args=("479615315:AAEQIIcH9iQ7ontmfq4T_Bpaqpl-H5N1CvI",))
    x.start()


