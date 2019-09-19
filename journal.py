#from banner import banner
#banner("DEEP THOUGHTS", "KELDON BALA")

def main():
    run_event_loop()

def run_event_loop():
    journal_data = []

    while True:
        command = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if command.upper() == "L":
          list_entries(journal_data)
        elif command.upper() == "A":
          add_entry(journal_data)
        elif command.upper() == "X":
            break
        else:
            print("Sorry, I don't understand")


def list_entries(data):
    print("Your data entries:")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1} - {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTRY> to exit: \n")
    data.append(entry)


main()