from tkinter import *
from tkinter import messagebox
#from tkinter.filedialog import askdirectory

def executeFilter():
    operadora = entryOperadora.get()
    for i in listboxTec.curselection():
        tecnologia = listboxTec.get(i)
        
    oldFile = open("/home/andrey/Desktop/Teste/drive_test.txt", "r")
    newFile0 = open("/home/andrey/Desktop/Teste/file_earth_80.txt", "w")
    newFile1 = open("/home/andrey/Desktop/Teste/file_earth_85.txt", "w")
    newFile2 = open("/home/andrey/Desktop/Teste/file_earth_90.txt", "w")
    newFile3 = open("/home/andrey/Desktop/Teste/file_earth_95.txt", "w")
    newFile4 = open("/home/andrey/Desktop/Teste/file_earth_100.txt", "w")
    newFile5 = open("/home/andrey/Desktop/Teste/file_earth_102.txt", "w")
    newFile6 = open("/home/andrey/Desktop/Teste/file_earth_105.txt", "w")
    newFile7 = open("/home/andrey/Desktop/Teste/file_earth_110.txt", "w")
    newFile8 = open("/home/andrey/Desktop/Teste/file_earth_NS.txt", "w")

    for line in oldFile:
        data = line.split()

        if(data[0] == "Timestamp"):
            line = line.replace("Filemark", "Color")
            newFile0.write(line)
            newFile1.write(line)
            newFile2.write(line)
            newFile3.write(line)
            newFile5.write(line)
            newFile5.write(line)
            newFile6.write(line)
            newFile7.write(line)
            newFile8.write(line)
        elif data[3] == operadora and data[4] == tecnologia:
            line = line.replace("\n", "\t")
            value = float(data[5]) 
            
            if value >= -80:
                line += "#800000\n"
                newFile0.write(line)
            elif -80 > value >= -85:
                line += "#ff0000\n"
                newFile1.write(line)
            elif -85 > value >= -90:
                line += "#ff8080\n"
                newFile2.write(line)
            elif -90 > value >= -95:
                line += "#ffff00\n"
                newFile3.write(line)
            elif -95 > value >= -100:
                line += "#00ff00\n"
                newFile4.write(line)
            elif -100 > value >= -102:
                line += "#00ffff\n"
                newFile5.write(line)
            elif -102 > value >= -105:
                line += "#00ffff\n"
                newFile6.write(line)
            elif -105 > value >= -110:
                line += "#0000ff\n"
                newFile7.write(line)
            else:
                line += "#000000\n"
                newFile8.write(line)

    oldFile.close()
    newFile0.close()
    newFile1.close()
    newFile2.close()
    newFile3.close()
    newFile4.close()
    newFile5.close()
    newFile6.close()
    newFile7.close()
    newFile8.close()
    
    messagebox.showinfo("AVISO", "Filtragem realizada!")
    

janela = Tk()
janela.title("Organizador Drive Test")

# Componentes Operadora
labelOperadora = Label(janela, text="Operadora (Conforme no arquivo NetTrack):")
labelOperadora.grid(row=0, column=0)
entryOperadora = Entry(janela)
entryOperadora.grid(row=0, column=1)

# Componentes Tecnologia
labelTecnologia = Label(janela, text="Tecnoologia: ")
labelTecnologia.grid(row=1, column=0)
listboxTec = Listbox(janela)
listboxTec.grid(row=2, column=0)
listboxTec.insert(0, "5G")
listboxTec.insert(1, "4G")
listboxTec.insert(2, "3G")

'''# Selecionar Arquivo
buttonFile = Button(janela, text="...", command=selecionarPasta())
buttonFile.grid(row=3, column=0)'''

# Botão Executar
buttonEnter = Button(janela, text="Executar", command=executeFilter)
buttonEnter.grid(row=4, column=0)

janela.mainloop()
