from sys import exit


class FileManager:
    """ Simulates a file system to Create, Delete, Move and List files within a directory. """
    def __init__(self, root: dict):
        """ Initializes from an existent directory 'root', can be empty """
        print("Welcome! Type 'quit' to exit.")
        self.root = root

    def insert(self, entry: str):
        """ Inserts new file or directory given a path separated by '/'.

            example: CREATE path/to/file
        """
        items = entry.split("/")
        current = self.root
        while items:
            item = items.pop(0)
            if item not in current.keys():
                if items:
                    print(f"Cannot create {entry} - {item} does not exist")
                    break
                current[item] = dict()
            current = current[item]
            if not items and current:
                print(f"{item} already exists")

    def delete(self, entry: str):
        """ Deletes a file or directory given a path separated by '/'.

            example: DELETE path/to/file
        """
        items = entry.split("/")
        current = self.root
        while items:
            item = items.pop(0)
            if item not in current.keys():
                print(f"Cannot delete {entry} - {item} does not exist")
                break
            elif not items:
                del current[item]
            else:
                current = current[item]

    def move(self, target: str, destination: str):
        """ Moves a file or directory into another directory given the target and destination paths, separated by '/'.

            example: MOVE path/to/target path/to/destination
        """
        target_items = target.split("/")
        current_target = current_destination = self.root
        destination_items = destination.split("/")
        while target_items:
            target_item = target_items.pop(0)
            if target_item not in current_target.keys():
                print(f"Cannot move {target} to {destination} - {target_item} does not exist")
                return
            elif not target_items:
                continue
            else:
                current_target = current_target[target_item]
        while destination_items:
            destination_item = destination_items.pop(0)
            if destination_item not in current_destination.keys():
                print(f"Cannot move {target} to {destination} - {destination_item} does not exist")
                return
            else:
                current_destination = current_destination[destination_item]
        current_destination[target_item] = current_target.pop(target_item)

    def print_tree(self, tree: dict, indent=0):
        """ Prints the contents of the root directory in a hierarchical manner """
        for key in sorted(tree.keys()):
            print("  " * indent + key)
            if isinstance(tree[key], dict):
                self.print_tree(tree[key], indent + 1)

    def execute(self, query: str = None):
        """ Executes a single query.

            Commands available: CREATE, DELETE, MOVE, LIST
        """
        if query:
            print(query)
        else:
            query = input("> ")
        if query.strip() == "":
            print("you must type a command")
            return
        if query.strip().lower() == "quit":
            print("Goodbye!")
            exit()

        args = query.split()
        command = args[0].upper()

        if command not in ["CREATE", "DELETE", "MOVE", "LIST"]:
            print("available commands: CREATE, DELETE, MOVE, LIST")
            return
        if command == "CREATE":
            if len(args) != 2:
                print("usage: CREATE path/to/file")
                return
            self.insert(args[1])
        elif command == "DELETE":
            if len(args) != 2:
                print("usage: DELETE path/to/file")
                return
            self.delete(args[1])
        elif command == "MOVE":
            if len(args) != 3:
                print("usage: MOVE path/to/target path/to/destination")
                return
            self.move(args[1], args[2])
        else:
            self.print_tree(self.root)
        return
