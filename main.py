import command
import db
database = db.Database()
command_obj = command.Command()
print("The Movie List Program")


def get_user_choice():
    choice = input("\nCOMMAND MENU"
                   "\ncat - View movies by category"
                   "\nyear = View movies by year"
                   "\nmin - View movies by minutes"
                   "\nadd - Add a movie"
                   "\nupdate - Update a movie"
                   "\ndel - Delete a movie"
                   "\nexit - Exit program"
                   "\n\nCOMMAND: ")
    return choice


def main():
    cont = True
    while cont:
        user_choice = get_user_choice()

        if user_choice == "cat":
            command_obj.cat_command()

        elif user_choice == "year":
            command_obj.year_command()

        elif user_choice == "min":
            command_obj.min_command()

        elif user_choice == "add":
            command_obj.add_command()

        elif user_choice == "update":
            command_obj.update_command()

        elif user_choice == "del":
            command_obj.delete_command()

        elif user_choice == "exit":
            cont = False
            print("Bye!")
            command_obj.close_db_connection()
        else:
            print("Invalid input!. Please try again.\n")
            cont = True


if __name__ == "__main__":
    main()
