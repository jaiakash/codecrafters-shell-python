import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        if command == "exit 0":
            break

        if command.startswith("echo"):
            sys.stdout.write(command[5:] + "\n")
            continue

        if command.startswith("type"):
            if command[5:] == "echo" or command[5:] == "exit" or command[5:] == "type":
                sys.stdout.write(command[5:] + " is a shell builtin\n")
                continue
            else:
                sys.stdout.write(f"{command[5:]}: not found\n")
                continue
            continue

        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
