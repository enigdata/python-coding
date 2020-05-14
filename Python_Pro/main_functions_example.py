from time import sleep 

print("This is my file to demonstrate best main function practices.")

def process_data(data):
    print('Beginning data processing...')
    modified_data = data + 'that has been modified'
    sleep(3)
    print("Data processing finished")
    return modified_data

##If you want to execute through command line not allowing import
if __name__=="__main__":
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

#### Edit 
from time import sleep 

print("This is my file to demonstrate best main function practices.")

def process_data(data):
    print('Beginning data processing...')
    modified_data = data + 'that has been modified'
    sleep(3)
    print("Data processing finished")
    return modified_data

def main():
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

##If you want to execute through command line not allowing import
if __name__=="__main__":
    main()

##### Final Version

from time import sleep 

print("This is my file to demonstrate best main function practices.")

def process_data(data):
    print('Beginning data processing...')
    modified_data = data + 'that has been modified'
    sleep(3)
    print("Data processing finished")
    return modified_data

def read_data_from_web():
    print("Reading data from the web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Wrtiting data to a database")
    time.sleep(2)
    print(data)
    print('Done.')

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

##If you want to execute through command line not allowing import
if __name__=="__main__":
    main()
