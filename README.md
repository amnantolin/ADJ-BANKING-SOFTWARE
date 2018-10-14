![ADJ LOGO](https://github.com/amnantolin/ADJ-BANKING-SOFTWARE/blob/master/Source/UI/UI_Resources/logo1.png)
----

## Introduction
> ADJ Banking Software maintains client’s bank accounts and providing basic banking services such as deposit, withdraw, and change PIN. The group tried to recreate a real-life banking management services by providing a Python application of such which consist of two main parts: The administrative module and the ATM module. The administrative module is used and accessed by the System Administrators or Bank Tellers. It has the following functionalities: To open, close accounts and view account information. On the other hand, the ATM module side can be used by the client in order to do deposit, withdraw, balance inquiry, or change pin transaction.

## Walkthrough
> **Database** = contains the database file. (duh? :stuck_out_tongue_closed_eyes:)   
> **Documents** = contains all the paperworks and other files including the final documentation, usecase diagram, detailed class diagram, burndown chart, etc.  
> **Source** = contains all the source codes. The project is a 3-Tier Architecture so it is divided into three parts: Business Logic Layer(BLL), Data Access Layer(DAL), and User Interface(UI). The BLL is sub-divided into admin and client part (as stated in the introduction). Each have their own main and class python files. Next, the DAL contains the "data_handler.py" which is a collection of queries used to manipulate the database file. Lastly, the UI consists of python files which are used as a Graphical User Interface(GUI) for the program that interacts with the users.  
>**Testing** = contains the sample unit testing.  

## Test the Program
> Just go to either **Admin** or **Client** located in Source-->BLL folder. Then run **Admin_Main.py** or **Client_Main.py** for admin side or client side, respectively.  
> NOTE: Check the database file for the default username and password login in the admin part. The program has no feature wherein you can add an admin account, however you can use an insert query directly into the database file.

----
### Group Members
* [ANTOLIN, Arryll Mori](https://github.com/amnantolin)
* [JAWOD, Danielle Nicole](https://github.com/dnojawod)
* [REYES, Jean Marc](https://github.com/jm18reyes)
