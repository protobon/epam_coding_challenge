root = dict()


def insert(entry: str):
    items = entry.split("/")
    current = root
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


def delete(entry: str):
    items = entry.split("/")
    current = root
    while items:
        item = items.pop(0)
        if item not in current.keys():
            print(f"Cannot delete {entry} - {item} does not exist")
            break
        elif not items:
            del current[item]
        else:
            current = current[item]


def move(target: str, destination: str):
    target_items = target.split("/")
    current_target = current_destination = root
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


def print_tree(tree: dict, indent=0):
    for key in sorted(tree.keys()):
        print("  " * indent + key)
        if isinstance(tree[key], dict):
            print_tree(tree[key], indent + 1)


def main(commands):
    print("Welcome! Type 'quit' to exit.")
    while True:
        if commands:
            query = commands.pop(0)
            print(query)
        else:
            query = input('> ')
        if not query or query.strip() == "":
            print("invalid command")
        if query.lower().strip() == "quit":
            break
        else:
            args = query.split()
            command = args[0].upper()
            if command not in ["CREATE", "DELETE", "MOVE", "LIST"]:
                print("available commands: CREATE, DELETE, MOVE, LIST")
            if command == "CREATE":
                if len(args) != 2:
                    print("usage: CREATE path/to/file")
                insert(args[1])
            elif command == "DELETE":
                if len(args) != 2:
                    print("usage: DELETE path/to/file")
                delete(args[1])
            elif command == "MOVE":
                if len(args) != 3:
                    print("usage: MOVE path/to/target path/to/destination")
                    continue
                move(args[1], args[2])
            else:
                print_tree(root)


if __name__ == '__main__':
    commands = [
        "CREATE fruits",
        "CREATE vegetables",
        "CREATE grains",
        "CREATE fruits/apples",
        "CREATE fruits/apples/fuji",
        "LIST",
        "CREATE grains/squash",
        "MOVE grains/squash vegetables",
        "CREATE foods",
        "MOVE grains foods",
        "MOVE fruits foods",
        "MOVE vegetables foods",
        "LIST",
        "DELETE fruits/apples",
        "DELETE foods/fruits/apples",
        "LIST"
    ]
    main(commands)
