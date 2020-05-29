class Pliki:
     
    _filename = __file__.split("\\")[-1]

    def __init__(self, file_name=_filename, phrase='', shift_num=0):
        self.file_name = str(file_name)
        self.phrase = str(phrase)
        self.shift_num = int(shift_num)

    def get_filename(self):
        return self.file_name

    def list_dir(self):
        import os
        arr = os.listdir()
        print(arr) 
    
    def check_file(self):
        try: 
            open(self.file_name, 'r')
            print(f'plik zostal znaleziony')
            return True
            
        except FileNotFoundError:
            print('nie znaleziono pliku')
            return False

    def show_content(self):
        f1 = open(self.file_name, "r")
        wczytane = f1.read()
        print(wczytane)
        
    def create_file(self):
        return open(self.file_name,"wb")
    

    def copy_file(self):
        """
        funkcja kopiuje plik o nazwie przekazywanej przez paramter funkcji
        :param file_name: pelna nazwa pliku.
        """
        try:
            base = open(self.file_name, "rb")             # funkcja open na bazowy plik do odczytu       
            cop = open("kopia " + self.file_name, "wb")   # funkcja open w celu stworzenia kopii do zapisu
            while True:                
                b = base.read(1)                          # wczytujemy z pliku bazowego
                if not b: break      
                cop.write(b)                              # zapis do kopii
            cop.close(); base.close()                     # zamykniecie obu plikow           
            print("Kopiowanie zakończone pomyślnie")      # output (jezeli sie udalo)   
        except FileNotFoundError:
            print('plik nie zostal znaleziony')           # output jezeli nie udalo sie znalezc nazwy pliku 


    def encrypt_msg(self, file_name, shift_num):
        pass
        """
        funkcja kopiuje plik o nazwie przekazywanej przez paramter funkcji
        :param file_name: pelna nazwa pliku.
        :param shift_num: definiuje przesunięcie 

        napisz funkcje która szyfruje wskazany przez użytkownika plik tekstowy (jezeli istnieje) 
        w oparciu o szyfr Cezara (przesuwanie liter w alfabecie o podaną wartość).     
        """


if __name__ == "__main__":

    
    pierwszy_plik = Pliki('9. Modules.py')
    pierwszy_plik.list_dir()
    pierwszy_plik.get_filename()
    pierwszy_plik.check_file()
    
    print(pierwszy_plik.get_filename())
    l = pierwszy_plik
    print(l)   # Output <__main__.Pliki object at 0x...>
    
    pierwszy_plik.show_content()      # podgladamy plik

    # napisz funkcje encrypt_msg
    # stworz wiecej obiektow 
    
