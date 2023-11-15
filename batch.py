def batch_subtask_3_1(lista,st,dr):
    """
    functia tipareste partea imaginara pentru numerele din lista,
    ce se afla intre pozitiile st si dr
    """

    if st>dr or dr>=len(lista) or st<0:
        raise ValueError

    imaginare = []
    for i in range(st, dr + 1):
        imaginare.append(get_imaginar(lista[i]))
    return imaginare

def batch_subtask_2_1(v,poz):
    """
    se sterge din lista v de pe pozitia poz elementul
    """
    if not (poz<len(v)):
        raise ValueError("pozitie incorecta")

    v.pop(poz)

def get_instruction(instr):
    """
    se citeste de la tastatura instructiunea
    si se returneaza , insotita de o lista de numere,ce are
    diferite interpretari: pozitie,numar,etc
    """
    instr=instr.strip()
    instr=instr.split()

    if instr[0].isalpha():
        try:
            for i in range(1,len(instr)):
                x=int(instr[i])
                instr[i]=x
        except ValueError:
            return 'NONE', []

        instr[0]=instr[0].lower()
        return instr[0], list(instr[1:])#!!!!!!!
    else:
        return 'NONE', []

def get_mode():
    """
    se citeste de la tastatura 1 sau 2
    reprezentand modul ce se doreste a fi folosit
    """
    mode=-1
    while not (mode==1 or mode==2):
        mode=int(input("Introduceti modul de folosire a aplicatiei: "))
    return mode

def afisare_moduri():
    """
    se afiseaza cele doua moduri in care putem introduce
    instructiunile in program
    """
    print("1. Batch mode\n")
    print("2.Normal mode\n")

def run():
    v = []
    history = []
    history.append(list(v))

    afisare_moduri()
    mode=get_mode()
    if mode==1: #BATCH
        line_command=input("Introduceti comenzile separate prin ';' ")
        line_command=line_command.split(';')
        for cmd in line_command[:]:
            instr, aux1=get_instruction(cmd)
            if instr=='add':
                """
                adauga la sfarsitul listei numarul "aux1"
                """
                v.append(creeaza_complex(aux1[0],aux1[1]))
                history.append(list(v))
                print(v)
            elif instr=='sterge':
                #"se sterge numarul de pe pozitia aux1[0] din lista v"
                try:
                    batch_subtask_2_1(v,aux1[0])
                    history.append(list(v))
                    print(v)
                except ValueError as ve:
                    print(ve)
            elif instr=='filtrare':
               # "tipareste partea imaginara pentru numerele din "lista"
               # ",ce se afla intr-un anumit interval de pozitii"
               rez=[]
               try:
                    rez=batch_subtask_3_1(v,aux1[0],aux1[1])
                    print(rez)
               except ValueError as ve:
                   print(ve)
            elif instr=='undo':
                try:
                    v=undo(history)
                    print(v)
                except ValueError as ve:
                    print(ve)

            elif instr=='exit':
                exit(0)
