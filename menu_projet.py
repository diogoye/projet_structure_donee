from pro_convert import*
chem =input("donner le chemin de votre fifcier a convertir")
verification_file(chem)
if verification_file(chem)!=False:
    my_dict=verification_file(chem)
    print("**********************Menu********************")
    print("1 Pour convertir en Json")
    print("2 Pour convertir en yaml")
    print("3 Pour convertir en xml")
    print("4 Pour convertir en csv")
    print("5 Pour autre")
    choix=int(input("veuilller faire un choix:"))
    if choix==1:
        conv_dic_to_json(my_dict)
    elif choix==2:
        conv_dic_to_yaml(my_dict)
    elif choix==3:
        conv_dic_to_xml(my_dict)
    elif choix==4:
        conv_dic_to_csv(my_dict)
    elif choix==5:
        print("note availlable")