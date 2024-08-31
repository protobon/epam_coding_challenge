from file_manager import FileManager

if __name__ == '__main__':
    root = dict()
    fm = FileManager(root)
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
    while True:
        fm.execute(commands.pop(0) if commands else None)
