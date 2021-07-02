import core.utility as utility
import core.manager as dbmanager
import core.exceptions as exception
import model.users as user_model


def register_cashier():
    firstname = utility.inputer("enter cashier's firstname :")
    lastname = utility.inputer("enter cashier's lastname :")
    phone_number = ""
    try:

        phone_number = utility.inputer("enter cashier's phone number :",
                                       validator=utility.Validators.check_phone,
                                       retry=True,
                                       retry_print="phone number is not valid. pleas enter a valid number")

        db = dbmanager.DataBaseManager()

        res = db.read_condition("users", "phone_number", phone_number[2:])
        print(res)
        if res:
            raise exception.UserExistError

    except:
        print("this user exist!!..try again")
        register_cashier()

    email = utility.inputer("enter cashier's email:(optional)",
                            validator=utility.Validators.check_email,
                            retry=True,
                            retry_print="email is not valid. pleas enter a valid email"
                            )
    if email == "":
        email = None

    password = utility.inputer("enter cashier's password:",
                               validator=utility.Validators.check_password,
                               retry=True,
                               retry_print="password is not valid. pleas enter a valid email"
                               )


    #TODO : hash password
    #TODO : ask about user added to database
    u = user_model.User(firstname, lastname, phone_number[2:], password, email)
    print(u.to_dict())

    # dbmanager.DataBaseManager().create("users", u)
    print("user added successfully")
