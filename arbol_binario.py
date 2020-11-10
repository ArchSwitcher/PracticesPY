class Node:
    def __init__(self, number):
        self.left = None
        self.rigth = None
        self.number = number


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.number < node.number:
            if root.rigth is None:
                root.rigth = node
            else:
                insert(root.rigth, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def in_order(root):
    if root is not None:
        print(root.number)
        in_order(root.left)
        in_order(root.rigth)


def search(root, value):
    if root is not None:
        path.append(root.number)
        if root.number > value:
            search(root.left, value)
        if root.number < value:
            search(root.rigth, value)

    if(root.number == value):
        print("\nFue encontrado {} antecesor = {} \n".format(
            root.number,
            path[len(path)-2]
        ))


if __name__ == "__main__":
    path = []
    res = "0"
    root = Node
    numbers = []

    while res != "3":
        print(
            "\n1) ingresar lista de numeros\n" +
            "2) buscar un numero\n" +
            "3) salir"
        )
        res = input("Ingrese un numero.")
        if res == "1":
            print("ingrese una lista de numeros separados por coma")
            list_numbers = input("....: ")
            values = list_numbers.split(",")
            if len(values) > 0:
                for n in range(len(values)):
                    if n == 0:
                        root = Node(int(values[0]))
                    else:
                        insert(root, Node(int(values[n])))
            print("valores ordenados en preorden para ver su antecesor\n")
            in_order(root)
        if res == "2":
            print("Ingrese un valor a buscar")
            answer = int(input(".........: "))
            search(root, answer)

