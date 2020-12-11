import database


def menu():
    menu_interface = """
    -- Netflox --
    1) Sign Up
    2) Log in
    0) Exit
    Your Selection: """

    while (user_input := input(menu_interface)) != '0':

        if user_input == '1':
            print("\n\tSign up")
            name = input("\tEnter your name: ")
            email = input("\tEnter your e-mail: ")
            password = input("\tEnter your password: ")
            database.create_user(name, email, password)

        elif user_input == '2':
            print("\n\tLog in")
            email = input("\tEnter your e-mail: ")
            password = input("\tEnter your password: ")
            user = database.log_in(email, password)
            if user == -1:
                return user  # admin
            elif user == 1:
                return user  # client

        else:
            print("Invalid input, please try again")


def client():
    client_interface = """
    1) Search products
    2) View all
    3) View my products
    4) My history
    5) Messages
    0) Exit
    Your Selection: """
    while (client_input := input(client_interface)) != '0':
        if client_input == '1':

            search_interface = """
    Search  by
    1) Name
    2) Actor
    3) Director
    4) Type
    0) Exit
    Your Selection: """

            while (search_input := input(search_interface)) != '0':
                if search_input == '1':
                    name = input("\n\tInsert movie name: ")
                    database.findby_name(name)
                if search_input == '2':
                    actor = input("\n\tInsert actor name: ")
                    database.findby_actor(actor)

                if search_input == '4':
                    type = input("\n\tInsert 'movie' or 'series': ")
                    database.findby_type(type)

                if search_input == '3':
                    director = input("\n\tInsert Director name: ")
                    database.findby_director(director)

                if search_input == '4':
                    type = input("\n\tInsert 'movie' or 'series': ")
                    database.findby_type(type)

        if client_input == '2':
            database.view_allmovies()
            client_input_view = input(
                "\tSelect a movie or\n\tOrder by: 1.Title 2. Director 3.Date of release 4.Imdb rating 0.Go back: ")
            if client_input_view == '1':
                print("\tordered by title:\n")
                database.view_allmovies_ordertitle()

            if client_input_view == '2':
                print("\tordered by Director:\n")
                database.view_allmovies_orderdirector()
            if client_input_view == '3':
                print("\tordered by Date of Release:\n")
                database.view_allmovies_orderdate()
            if client_input_view == '4':
                print("\tordered by Imdb rating:\n")
                database.view_allmovies_orderimdb()

            if (client_input_view != '0') and (client_input_view != '1') and (client_input_view != '2') and (
                    client_input_view != '3') and (client_input_view != '4'):
                print("\tid  name,  actorid, director, imdbrating, genre, price, year, timeavaible, type")
                moviename = database.view_movieinfo(client_input_view)
                if moviename == 0:
                    break
                client_input_view_buy = input("\n\tpress 1 to buy press 0 to leave\n")
                if client_input_view_buy == '1':
                    print("\n\tYour balance is: ")
                    balance = database.view_saldo(USERID)
                    print("\n\tThis item costs: ")
                    cost = database.view_custo(client_input_view)
                    client_input_view_buy = input("press 1 to confirm press 0 to leave\n")
                    if client_input_view_buy == '1':
                        if cost < balance:
                            print("\n\tItem bought successfully!\n")
                            database.compra_filme(cost, balance, USERID)
                            database.create_rent(cost, USERID, moviename)
                            print("\n\tActual balance:\n")
                            database.view_saldo(USERID)
                        else:
                            print("\n\tNot enough balance!")
        if client_input == '3':
            database.view_available_movies(USERID)
            client_input_available_movies = input(
                "Order by: 1.Title 2. Director 3.Date of release 4.Imdb rating 0.Go back\n")
            if client_input_available_movies == '1':
                print("ordered by title:\n")
                # database.view_availablemovies_ordertitle(USERID)
            if client_input_available_movies == '2':
                print("ordered by Director:\n")
                database.view_availablemovies_orderdirector(USERID)
            if client_input_available_movies == '3':
                print("ordered by Date of Realease:\n")
                # database.view_availablemovies_orderdate(USERID)
            if client_input_available_movies == '4':
                print("ordered by Imdb rating:\n")
                # database.view_availablemovies_orderimdb(USERID)

        if client_input == '4':
            print(
                "clientid, date start,                                   price,                     date end,                 usermail,months, id, type, movieid")
            database.view_rent(USERID)

        if client_input == '5':
            message_interface = """
    1) View unread messages
    2) View read messages
    0) Exit
    Your Selection: """
            while (client_input := input(message_interface)) != '0':

                if client_input == '1':
                    y = database.show_unread_messages(USERID)
                    while (x := int(input("\tYour Selection: "))) != 0:
                        database.read_message(y[x - 1][0])
                        print("\n\t" + y[x - 1][1])
                        print("\n\t0) Go back")

                if client_input == '2':
                    y = database.show_read_messages(USERID)
                    while (x := int(input("\tYour Selection: "))) != 0:
                        print("\n\t" + y[x - 1][1])
                        print("\n\t0) Go back")


def admin():
    admin_interface = """
    1) Add new article
    2) Search products
    3) View all
    4) Change price
    5) Remove article
    6) Messages
    7) Alter user balance
    0) Exit
    Your Selection: """
    while (admin_input := input(admin_interface)) != '0':

        if admin_input == '1':
            print("\n\tAdd new article")
            name = input("\tName: ")
            actorid = input("\tActorid/s (separated by commas): ")
            director = input("\tDirector: ")
            imbdrating = input("\tIMDB rating: ")
            genre = input("\tGenre: ")
            price = input("\tPrice: ")
            year = input("\tYear of release:")
            monthsavaible = input("\tHow many months will this movie be available: ")
            type = input("\tPlease insert 'movie' or 'series': ")
            database.add_article(name, str(actorid), director, imbdrating, genre, price, year, monthsavaible, type)

        if admin_input == '4':
            print("\n\tChange price")
            n_id = input("\tMovie name or id: ")
            new_price = input("\tNew Price: ")
            database.change_price(n_id, new_price)

        if admin_input == '5':
            print("\n\tRemove article")
            n_id = input("\tMovie name or id: ")
            database.remove_article(n_id)

        if admin_input == '6':
            message_interface = """
    1) Send message to all
    2) Send message to a client
    0) Exit
    Your Selection: """
            while (admin_input := input(message_interface)) != '0':
                if admin_input == '1':
                    print("\n\tSend message to all")
                    msg = input("\tMessage: ")
                    database.message_all(msg, database.USERID)

                if admin_input == '2':
                    print("\n\tSend message to a client")
                    msg = input("\tMessage: ")
                    recieverid = input("\tClient id: ")
                    database.message_client(msg, recieverid, database.USERID)

        if admin_input == '7':
            print("\n\tAlter user balance")
            userid = input("\tUser id:  ")
            balance = input("\tNew balance: ")
            database.alter_balance(userid, balance)


if menu() != -1:
    USERID = database.USERID
    client()
else:
    USERID = database.USERID
    admin()