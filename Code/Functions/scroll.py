#! /usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk 
 

def printResultsWindow(sizeRequest, selected_names, selected_units, description, results,  request):
    lineHead = []
    titleHead = []
    titleUnit = []
    lineUnit = ["\n"]
    length = []

    # Build the first row with the heads of the columns 
    for i in range (sizeRequest):
        head = selected_names[i]
        unit = selected_units[i]    
        if unit == None:
            unit = ""
        sizeDisplay = max(description[i][3], len(head), len(unit))
        
        if sizeDisplay > 32:
            sizeDisplay = 32
        
        titleHead.append(head)
        titleUnit.append(unit)
        lineHead.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        lineUnit.append(" {u[%d]:^%s} " % (i, sizeDisplay))
        length.append(sizeDisplay)
    
    lineHead = "".join(lineHead)
    lineUnit = "".join(lineUnit)
    lineHead = lineHead.format(t=titleHead)
    lineUnit = lineUnit.format(u=titleUnit)

    # Build the table of results row after row
    truncated = []
    formatted_results = []

    for nb in range(request):
        line = ["\n"]
        title = []
        
        for i in range (sizeRequest):
            sizeDisplay = length[i]
            content = str(results[nb][i])
            sizeContent = len(content)

            if sizeContent > sizeDisplay:
                title.append(content[0:sizeDisplay])
                truncated.append((results[nb], i, sizeContent))
            
            elif content == "None":
                content = ""
                title.append(content)
            
            else:
                title.append(content)
            
            line.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        
        line = "".join(line)
        formatted_results.append(line.format(t=title))
    

    window = tk.Tk(className="Affichage des résultats de votre recherche") 
    window.geometry("1000x500") 

    SVBar = tk.Scrollbar(window) 
    SVBar.pack (side = tk.RIGHT, fill = "y") 

    SHBar = tk.Scrollbar(window, orient = tk.HORIZONTAL) 
    SHBar.pack (side = tk.BOTTOM, fill = "x") 

    TBox = tk.Text(window, height = 500, width = 500, yscrollcommand = SVBar.set, xscrollcommand = SHBar.set, wrap = "none") 

    TBox.pack(expand = 0, fill = tk.BOTH) 

    TBox.insert(tk.END, lineHead) 
    TBox.insert(tk.END, lineUnit)
    for line in formatted_results:
        TBox.insert(tk.END, line)

    SHBar.config(command = TBox.xview) 
    SVBar.config(command = TBox.yview) 

    window.mainloop()

    return(truncated, titleHead, titleUnit)



def printTruncated(truncated, titleHead, titleUnit, results, description, sizeRequest):
    
    # Print the title of each column
    lineHead = []
    lineUnit = ["\n"]
    length = []

    for i in range(sizeRequest):
        listForMax = [32]

        for row in truncated:
            if row[1] == i:
                listForMax.append(row[2])

        sizeMax = max(listForMax, default=0)
        if description[i][3] > 100000:
            sizeDisplay = max(len(titleHead[i]), len(titleUnit[i]), sizeMax)
        elif listForMax == [32]:
            sizeDisplay = max(len(titleHead[i]), len(titleUnit[i]), description[i][3])
        else:
            sizeDisplay = max(len(titleHead[i]), len(titleUnit[i]), sizeMax)

        
        if sizeDisplay < 12:
            sizeDisplay = 12
        
        lineHead.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        lineUnit.append(" {u[%d]:^%s} " % (i, sizeDisplay))
        length.append(sizeDisplay)
    
    lineHead = "".join(lineHead)
    lineUnit = "".join(lineUnit)
    lineHead = lineHead.format(t=titleHead)
    lineUnit = lineUnit.format(u=titleUnit)

    # select the truncated lines
    toPrint = []
    for row in truncated:
        rowToPrint = row[0]
        
        if rowToPrint not in toPrint:
            toPrint.append(rowToPrint)

    # print the truncated lines
    formatted_lines = []
    for row in toPrint:
        line = ["\n"]
        title = []
        
        for i in range (sizeRequest):
            sizeDisplay = length[i]
            content = str(row[i])

            if content == "None":
                content = ""
                title.append(content)
            
            else:
                title.append(content)
            
            line.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        
        line = "".join(line)
        formatted_lines.append(line.format(t=title))

    window = tk.Tk(className="Affichage des résultats de votre recherche non tronquée") 
    window.geometry("1000x500") 

    SVBar = tk.Scrollbar(window) 
    SVBar.pack (side = tk.RIGHT, fill = "y") 

    SHBar = tk.Scrollbar(window, orient = tk.HORIZONTAL) 
    SHBar.pack (side = tk.BOTTOM, fill = "x") 

    TBox = tk.Text(window, height = 500, width = 500, yscrollcommand = SVBar.set, xscrollcommand = SHBar.set, wrap = "none") 

    TBox.pack(expand = 0, fill = tk.BOTH) 

    TBox.insert(tk.END, lineHead) 
    TBox.insert(tk.END, lineUnit)
    for line in formatted_lines:
        TBox.insert(tk.END, line)

    SHBar.config(command = TBox.xview) 
    SVBar.config(command = TBox.yview) 

    window.mainloop()

    return()

