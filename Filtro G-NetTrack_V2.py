from tkinter import *
from simplekml import *
from tkinter import messagebox
from tkinter import filedialog

def selecionarArquivo(label):
    file = filedialog.askopenfilename()
    label.config(text=file)

def selecionarPasta(label):
    folder = filedialog.askdirectory()
    label.config(text=folder)

def executeFilter():
    operadora = entryOperadora.get()
    for i in listboxTec.curselection():
        tecnologia = listboxTec.get(i)
        
    oldFile = open(labelFile.cget("text"), "r")
    newFile0 = open(labelFolder.cget("text") + "/file_earth_80.txt", "w")
    newFile1 = open(labelFolder.cget("text") + "/file_earth_85.txt", "w")
    newFile2 = open(labelFolder.cget("text") + "/file_earth_90.txt", "w")
    newFile3 = open(labelFolder.cget("text") + "/file_earth_95.txt", "w")
    newFile4 = open(labelFolder.cget("text") + "/file_earth_100.txt", "w")
    newFile5 = open(labelFolder.cget("text") + "/file_earth_102.txt", "w")
    newFile6 = open(labelFolder.cget("text") + "/file_earth_105.txt", "w")
    newFile7 = open(labelFolder.cget("text") + "/file_earth_110.txt", "w")
    newFile8 = open(labelFolder.cget("text") + "/file_earth_NS.txt", "w")

    kml0 = Kml()
    kml1 = Kml()
    kml2 = Kml()
    kml3 = Kml()
    kml4 = Kml()
    kml5 = Kml()
    kml6 = Kml()
    kml7 = Kml()
    kml8 = Kml()

    for line in oldFile:
        data = line.split()

        if(data[0] == "Timestamp"):
            line = line.replace("Filemark", "Color")
            newFile0.write(line)
            newFile1.write(line)
            newFile2.write(line)
            newFile3.write(line)
            newFile4.write(line)
            newFile5.write(line)
            newFile6.write(line)
            newFile7.write(line)
            newFile8.write(line)

        elif data[3] == operadora and data[4] == tecnologia:
            line = line.replace("\n", "\t")
            value = float(data[5]) 
            
            if value >= -80:
                kml0.newpoint(coords=[(float(data[1]), float(data[2]))])
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

    kml0.savekmz("teste1.kml")
    kml1.savekmz("teste2.kml")
    kml2.savekmz("teste3.kml")
    kml3.savekmz("teste4.kml")
    kml4.savekmz("teste5.kml")
    kml5.savekmz("teste6.kml")
    kml6.savekmz("teste7.kml")
    kml7.savekmz("teste8.kml")
    kml8.savekmz("teste9.kml")
    
    messagebox.showinfo("AVISO", "Filtragem realizada!")
    

janela = Tk()
janela.title("Organizador Drive Test")
janela.geometry("500x300")

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

# Caminho Arquivo
labelFile = Label(janela, text="Nenhum arquivo selecionado")
labelFile.grid(row=3, column=0)

# Selecionar Arquivo
buttonFile = Button(janela, text="...", command=lambda: selecionarArquivo(labelFile))
buttonFile.grid(row=3, column=1)

# Caminho Pasta
labelFolder = Label(janela, text="Nenhuma pasta selecionada")
labelFolder.grid(row=4, column=0)

# Selecionar Pasta
buttonPasta = Button(janela, text="...", command=lambda: selecionarPasta(labelFolder))
buttonPasta.grid(row=4, column=1)

# Botão Executar
buttonEnter = Button(janela, text="Executar", command=executeFilter)
buttonEnter.grid(row=5, column=0)

janela.mainloop()
