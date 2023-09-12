from constant import COFFEE_MACHINE_INIT, COFFEE_DETAILS
from coffee_machine import Coffee_Machine

def init_coffee_machine():
    return Coffee_Machine(COFFEE_MACHINE_INIT, COFFEE_DETAILS)

if __name__ == '__main__':
    coffee_machine : Coffee_Machine = init_coffee_machine()

    while True:
        coffee_list_message = ','.join(COFFEE_DETAILS.keys())
        print(f'Please select coffee from the selected list ({coffee_list_message}):')
        command = input().lower()

        if command == 'stop':
            break

        elif command not in COFFEE_DETAILS.keys():
            coffee_machine.print_report() if command == 'report' else print('Sorry we currently dont have this type of coffee')

        else:
            messsage = coffee_machine.make_coffee(command)
            print(messsage)
