from sys import exit
import pprint #de leitourgei pote to pprint
Students = {}
#key = am, value = onoma
def menu():
    print('''Πατήστε:
        1 για εισαγωγή μαθητή
        2 για διαγραφή μαθητή
        3 για αλλαγή ονόματος
        4 για προβολή όλων των μαθητών
        5 κλείσιμο''')
while True:
    menu()
    choice = input()
    # if choice not in range(1,6):
    # #2 epiloges: i vazw choice = int(input) kai an to input einai grammata petaei error
    # #i to vazw choice = input kai elif choice == '5' kai petaei se ola wrong input
    # #i deyteri epilogi me volevei. tha valw kai ta alla elif kai de tha crusharei. pote.
    # #omws giati de leitourgei swsta to in range? oute me not in range oute me != range???
    #     print('Wrong input.')
    if choice == '5':
        exit()
    elif choice == '4':
        pprint.pprint(Students) #kanei kanoniko print
    elif choice == '1':
        print('Δώστε όνομα ')
        name = input()
        am = (len(Students) + 1)
        Students[am] = name
        # Students[name] = (len(Students) + 1) #leitourgei alla dinei key = onoma LITHIKE
        # Students[(len(Students) + 1)] = name #de leitourgei ypotithetai oti dinei key = am (keyerror) LITHIKE
        print('Δώθηκε το ΑΜ: ' + str(am)) #leitourgei alla dinei key = onoma LITHIKE
        # print('Δώθηκε το ΑΜ: ' + (Students[name])) #de leitourgei ypotithetai oti dinei key = am (keyerror) LITHIKE
        #ti kanw an dyo mathites exoun idio onoma?
    elif choice == '2':
        print('Δώστε ΑΜ: ')
        am = int(input())
        if am in Students.keys():
            del Students[am] #?????????
            print(Students)
            print('Διαγραφή μαθητή επιτυχής.')
        else:
            print('Δεν υπάρχει το ΑΜ.')
        #meta apo diagrafes, kathe fora sto neo mathiti dinetai sygkekrimeno am (to teleytaio pou emeine)
        #kai antikathista to proigoumeno onoma
        #ti kanw an dyo mathites exoun idio onoma?
    elif choice == '3':
        print('Δώστε ΑΜ: ')
        am = int(input())
        if am in Students.keys():
            print('Δώστε νέο όνομα.')
            name = input()
            Students[am] = name
            print('Το νέο όνομα καταχωρήθηκε στο μαθητή με ΑΜ:'  )
            #fainetai na leitourgei swsta
        else:
            print('Δεν υπάρχει το ΑΜ.')
        #ti kanw an dyo mathites exoun idio onoma?
