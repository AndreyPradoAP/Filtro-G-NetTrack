from tkinter import *
from simplekml import *
from tkinter import messagebox
from tkinter import filedialog

def selectFile(label):
    file = filedialog.askopenfilename()
    label.config(text=file)

def selectFolder(label):
    folder = filedialog.askdirectory()
    label.config(text=folder)

def runFilter():
    operator = entryOperator.get()
    for i in listboxTec.curselection():
        technology = listboxTec.get(i)
        
    file = open(labelFile.cget("text"), "r")
    
    descript = '<style>table{ border-collapse: collapse; width: 100%; } th, td { text-align: left; padding: 10px; border: 1px solid black; }</style> <table> <tr> <td><p align="center"><b>Tecnologia</p></th> <td><p align="center">' + technology + '</p></th></tr> <tr><td><p align="center"><b>Operadora</p></th><td><p align="center">' + operator + '</p></th></tr> <tr><td><p align="center"><b>RSRP</p></th><td><p align="center">rsrpdBm</p></b></p></th></tr> </table>'

    kml = Kml()
    fold1 = kml.newdocument(name="Sinal até -80")
    fold2 = kml.newdocument(name="Sinal de -80 até -85")
    fold3 = kml.newdocument(name="Sinal de -85 até -90")
    fold4 = kml.newdocument(name="Sinal de -90 até -95")
    fold5 = kml.newdocument(name="Sinal de -95 até -100")
    fold6 = kml.newdocument(name="Sinal de -100 até -102")
    fold7 = kml.newdocument(name="Sinal de -102 até -105")
    fold8 = kml.newdocument(name="Sinal de -105 até -110")
    fold9 = kml.newdocument(name="Sinal a partir de -110")

    for line in file:
        data = line.split()

        if data[3] == operator and data[4] == technology:
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

    file.close()

    kml.savekmz(labelFolder.cget("text") + "/drive_test.kml")
    
    messagebox.showinfo("AVISO", "Filtragem realizada!")
    
window = Tk()
window.title("Organizador Drive Test")
window.geometry("400x250")

# Componentes Operadora
labelOperator = Label(window, text="Nome da Operadora (Conforme no arquivo .txt):")
labelOperator.place(x=0, y=0)
entryOperator = Entry(window)
entryOperator.place(x=265, y=2)

# Componentes Tecnologia
labelTechnology = Label(window, text="Geração: ")
labelTechnology.place(x=45, y=30)
listboxTec = Listbox(window, height=3)
listboxTec.place(x=10, y=50)
listboxTec.insert(0, "5G")
listboxTec.insert(1, "4G")
listboxTec.insert(2, "3G")

# Selecionar Arquivo
buttonFile = Button(window, text="Selecionar\nArquivo", command=lambda: selectFile(labelFile))
buttonFile.place(x=5, y=120)

# Caminho Arquivo
labelFile = Label(window, text="Nenhum arquivo selecionado")
labelFile.place(x=70, y=130)

# Selecionar Pasta
buttonFolder = Button(window, text="Selecionar\nPasta", command=lambda: selectFolder(labelFolder))
buttonFolder.place(x=5, y=170)

# Caminho Pasta
labelFolder = Label(window, text="Nenhuma pasta selecionada")
labelFolder.place(x=70, y=180)

# Botão Executar
buttonEnter = Button(window, text="Executar", command=runFilter)
buttonEnter.place(x=200, y=220)

window.mainloop()
