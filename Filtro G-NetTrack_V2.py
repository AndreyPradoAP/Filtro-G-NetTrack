from tkinter import *
from simplekml import *
from tkinter import messagebox
from tkinter import filedialog

descript = '<style>table{ border-collapse: collapse; width: 100%; } th, td { text-align: left; padding: 10px; border: 1px solid black; }</style> <table> <tr> <td><p align="center"><b>Tecnologia</p></th> <td><p align="center">tec</p></th></tr> <tr><td><p align="center"><b>Operadora</p></th><td><p align="center">oper</p></th></tr> <tr><td><p align="center"><b>RSRP</p></th><td><p align="center">rsrp</p></b></p></th></tr> <tr><td><p align="center"><b>Tempo</p></td><td><p align="center">temp</p></b></p></th></tr> </table>'

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
    
    descript = '<style>table{ border-collapse: collapse; width: 100%; } th, td { text-align: left; padding: 10px; border: 1px solid black; }</style> <table> <tr> <td><p align="center"><b>Tecnologia</p></th> <td><p align="center">' + tecnologia + '</p></th></tr> <tr><td><p align="center"><b>Operadora</p></th><td><p align="center">' + operadora + '</p></th></tr> <tr><td><p align="center"><b>RSRP</p></th><td><p align="center">rsrpdBm</p></b></p></th></tr> </table>'

    kml = Kml()
    fold1 = kml.newdocument(name="Sinal até -80")
    fold2 = kml.newdocument(name="Sinal de -80 até -85")
    fold3 = kml.newdocument(name="Sinal de -85 até -90")
    fold4 = kml.newdocument(name="Sinal de -90 até -95")
    fold5 = kml.newdocument(name="Sinal de -95 até -100")
    fold6 = kml.newdocument(name="Sinal de -100 até -102")
    fold7 = kml.newdocument(name="Sinal de -102 até -105")
    fold8 = kml.newdocument(name="Sinal de -105 até -110")
    fold9 = kml.newdocument(name="Sinal -110")

    for line in oldFile:
        data = line.split()

        if(data[0] == "Timestamp"):
            '''line = line.replace("Filemark", "Color")
            newFile0.write(line)
            newFile1.write(line)
            newFile2.write(line)
            newFile3.write(line)
            newFile4.write(line)
            newFile5.write(line)
            newFile6.write(line)
            newFile7.write(line)
            newFile8.write(line)'''

        elif data[3] == operadora and data[4] == tecnologia:
            line = line.replace("\n", "\t")
            value = float(data[5]) 
            
            if value >= -80:
                point = fold1.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ff000080' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
            elif -80 > value >= -85:
                point = fold2.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ff0000ff' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
            elif -85 > value >= -90:
                point = fold3.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ff8080ff' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
            elif -90 > value >= -95:
                point = fold4.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ff00ffff' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
            elif -95 > value >= -100:
                point = fold5.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ff00ff00' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
            elif -100 > value >= -102:
                point = fold6.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ffffff00' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
                line += "#00ff00\n"
            elif -102 > value >= -105:
                point = fold7.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ffff8080' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
                line += "#00ffff\n"
            elif -105 > value >= -110:
                point = fold8.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ffff0000' #aabbggrr
                point.description = descript.replace("rsrp", data[5])
            else:
                point = fold9.newpoint(coords=[(float(data[1]), float(data[2]))])
                point.iconstyle.icon.href = 'https://maps.google.com/mapfiles/kml/shapes/shaded_dot.png'
                point.style.iconstyle.color = '#ff000000' #aabbggrr
                point.description = descript.replace("rsrp", data[5])

    oldFile.close()

    kml.savekmz("drive_test.kml")
    
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
