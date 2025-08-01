print("         ==========================")
print("        !WELCOME TO HYDERABAD AUTOS!")
print("         ==========================")

data = {"Toyota":{"Fortuner":{"Name":"Fortner","year":2008,"Model":"xli","price":12344455},
                 "Corolla ":{"Name":"Corolla","year":2005,"Model":"Grande","price":12344455},
                 "Yaris":{"Name":"Yaris","year":2024,"Model":"xli","price":12344455},
                 "Prius":{"Name":"Prius","year":2023,"Model":"Hybrid","price":12344455},
                 "Aqua":{"Name":"Aqua","year":2024,"Model":"Hybrid","price":12344455}},
        "Suzuki":{"Mehran":{"Name":"Mehran","year":2008,"Model":"xli","price":12344455},
                "Swift":{"Name":"Swift","year":2008,"Model":"xli","price":12344455},
                "Cultus":{"Name":"Cultus","year":2008,"Model":"xli","price":12344455},
                "Alt0":{"Name":"Alto","year":2008,"Model":"xli","price":12344455},
                "Vagon-R":{"Name":"Vagon-R","year":2019,"Model":"xli","price":12344455}},
        "Kia":{"sportage":{"Name":"Sportage","year":2023,"Model":"V-XR","price":12344455},
               "Picanto":{"Name":"Picanto","year":2023,"Model":"V-XR","price":12344455},
               "Sorento":{"Name":"Sorento","year":2021,"Model":"AWD","price":12344455},
               "Stonic":{"Name":"Stonic","year":2022,"Model":"GT-Line","price":12344455}},
        "Honda":{"City":{"Name":"City","year":2012,"Model":"V-XR","price":12344455},
               "CIVIC":{"Name":"Civic","year":2022,"Model":"1.8","price":12344455},
               "BR-V":{"Name":"Br-V","year":2014,"Model":"VXR","price":12344455},
               "Accord":{"Name":"Accord","year":2021,"Model":"EX","price":12344455}}}
while True:               
    for index, Brands in enumerate (data.keys()):
        print(index+1,Brands)

    user_comp_choice = input("Enter you Brand Choice : ").capitalize()
    if user_comp_choice in data.keys():
        for index, cars in enumerate(data[user_comp_choice].values()):
            print(index+1,cars["Name"])
        cars =[car["Name"] for car in data[user_comp_choice].values()] 

    user_car_choice = input("Enter your car choice :  ").capitalize()
    for car in data[user_comp_choice].values():
            if car["Name"]==user_car_choice:
                print("Name: ",car["Name"])
                print("Year",car["year"])
                print("Model: ",car["Model"])
                print("Price: ",car["price"])
    else:
         print("Brand not Found...!")

         userinpt = input("Would you like to continue (Y/N)").lower()
         if userinpt !="y":
              print("Thanks for visiting....! ")

