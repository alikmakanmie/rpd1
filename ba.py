from src.ig import * 
from rich.panel import Panel
from rich import print as prints
def Logo():
  prints(Panel("""                                                 
 _____ _____ _____ _____ _____ _____ _____ _____ 
|     | __  |   __|  _  |_   _|   __|     |   __|
|   --|    -|   __|     | | | |   __|-   -|  |  |
|_____|__|__|_____|__|__| |_| |_____|_____|_____|
                                                 """,title=f"[white][ CODE BY : RIDWAN ][white]",
    width=120,
    padding=(0, 4),
    style="#9F9F9F"
))
def Main():
  Logo() 
  total = int(input("[?] Mau Berapa Akun : "))
  mem = input('[?] Mau Pake A2f? y/t : ')
  #es = input(f'[?] Masukan Bio Untuk Akun : ')
#  print( )
  for _ in range(total):
  	Username()
  #print("[1] AUTO CREATE IG\n[2] CHECK RESULT")
  match int(input("[?] Choice: ")):
    case 1:
      img = input("\n[+] Masukan File Gambar Sesuai Tempat Photonya Cth:/sdcard/img.jpg/png\n[+] Input: ")
      
      print( )
      total = int(input("[*] Masukan Jumlah: "))
      print( )
      for _ in range(total):
        Username()
    case 2:
      print("\n[1] Akun Checkpoint\n[2] Akun Live")
      match int(input("[?] Choice: ")):
        case 1:
          print()
          cp = open('cp.txt','r').read().splitlines()
          jum = len(cp)
          for x in cp:
            print(x)
          print("\n[*] Jumlah Akun Checkpoint: %s"%(jum))
    case __:
      Main()
if __name__=="__main__":
  clear()
  Main()
