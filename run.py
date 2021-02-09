import sys
import os

#Prints 
def usage():
    print("Usage: run.py\n" + 
            "\tmigrate \t- makes migrations and applies them\n" + 
            "\trun [-d] \t- spins up the website [runs quietly]\n" + 
            "\tdown \t\t- brings the docker container down\n" +
            "\tbuild \t\t- builds docker-compose images\n" + 
            "\tadmin [name]\t- creates a new superuser [with given name]\n" + 
            "\tinspectdb \t- inspects the django database setups\n" + 
            "\town \t\t- changes current user to new owner of all subdirectors\n" + 
            "\tstartapp 'name'\t- creates a new app subdirectory with given name (required) ")

import sys
import os

def main():
    
    # Starts the server
    if 'up'.strip() in sys.argv:
        os.system("python manage.py collectstatic --noinput --clear")
        if '-d'.strip() in sys.argv:
            os.system("sudo docker-compose up -d")
        else:
            os.system("sudo docker-compose up")

    # Allows us to run a docker-compose down.
    elif 'down'.strip() in sys.argv:
        os.system("sudo docker-compose down")

    # Builds the containers
    elif 'build'.strip() in sys.argv:
        os.system("sudo docker-compose build")

    # Does the migrations
    elif 'migrate'.strip() in sys.argv:
        os.system("sudo docker-compose run web python3 manage.py makemigrations")
        os.system("sudo docker-compose run web python3 manage.py migrate")
        
    # Creates a superuser
    elif 'admin'.strip() in sys.argv:
        if len(sys.argv) == 3:
            os.system("sudo docker-compose run web python3 manage.py createsuperuser " + sys.argv[2])
        else:
            os.system("sudo docker-compose run web python3 manage.py createsuperuser")

    # Creates a superuser
    elif 'inspectdb'.strip() in sys.argv:
        os.system("sudo docker-compose run web python3 manage.py inspectdb")

    #makes current user owner of all subdirectories/files
    elif 'own'.strip() in sys.argv:
        os.system("sudo chown -R $USER:$USER .")

    #creates a new app subdirectory in django with given name
    elif 'startapp'.strip() in sys.argv:
        if len(sys.argv) == 3:
            os.system("sudo docker-compose run web python3 manage.py startapp " + sys.argv[2])
        else:
            usage()

    else:
        usage()


# end program    
if __name__=="__main__":
    main()
