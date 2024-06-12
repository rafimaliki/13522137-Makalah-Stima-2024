from algorithms.KMP import KMP
from algorithms.BM import BM
from algorithms.WordCounter import WordCounter
from filereader.filereader import FileReader
import time

if __name__ == "__main__":
    
    # string = "bismillah lulus matkul stima dengan indeks A"
    # pattern = "lulus"
    
    print("\nSelamat datang di program 'Word Significancy Calculator!'")
    
    print("\nOpsi:\n  1. KMP\n  2. BM\n")
    method_opt = input("Pilihan: ")

    while method_opt != "1" and method_opt != "2":
        print("Input tidak valid.")
        method_opt = input("Pilihan: ")
    
    pdf_file = FileReader.read_pdf()
    WordCounter.countUniqueWords(pdf_file, method_opt)
    
    while True:
        
        print("\nOpsi:\n  1. Ganti file PDF\n  2. Ganti Algoritma\n  3. Keluar\n")
        opt = input("Pilihan: ")
            
        if opt == "1": # Ganti file PDF
            
            print("\nOpsi:\n  1. KMP\n  2. BM\n")
            method_opt = input("Pilihan: ")

            while method_opt != "1" and method_opt != "2":
                print("Input tidak valid.")
                method_opt = input("Pilihan: ")
                
            pdf_file = FileReader.read_pdf()
            WordCounter.countUniqueWords(pdf_file, method_opt)
        
        elif opt == "2":
                
            print("\nOpsi:\n  1. KMP\n  2. BM\n")
            method_opt = input("Pilihan: ")

            while method_opt != "1" and method_opt != "2":
                print("Input tidak valid.")
                method_opt = input("Pilihan: ")
                
            WordCounter.countUniqueWords(pdf_file, method_opt)

        elif opt == "3": # Keluar
            print("Terima kasih telah menggunakan program ini!")
            break
        
        else: # Input tidak valid
            print("Input tidak valid.")
            
        
    
    
