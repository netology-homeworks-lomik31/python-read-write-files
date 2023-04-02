class Reader:
    def ReadFile(path: str) -> str:
        file = open(path, "r")
        data = file.read()
        file.close()
        return data
    def CreateList(data: str) -> list:
        return list(map(lambda i: i.split("\n"), data.split("\n\n")))

class Parser:
    def CreateCookBook(data: list) -> dict:
        a = {}
        for i in data:
            name = i[0]
            a[name] = []
            for j in i[2:]:
                sp = j.split(" | ")
                a[name].append({"ingredient_name": sp[0], "quantity": int(sp[1]), "measure": sp[2]})
        return a
    def CreateShopList(dishes: list, personCount: int, cockBook: list) -> dict:
        res = {}
        for i in dishes:
            for j in cockBook[i]:
                if (j["ingredient_name"] in res): res[j["ingredient_name"]]["quantity"] += j["quantity"] * personCount
                else: res[j["ingredient_name"]] = {"measure": j["measure"], "quantity": j["quantity"] * personCount}
        return res

class Program:
    def Main():
        Parser.CreateShopList(
            ['Запеченный картофель', 'Омлет'], 2,
            Parser.CreateCookBook(
                Reader.CreateList(
                    Reader.ReadFile("files/recipes.txt")
                )
            )
        )

if __name__ == "__main__": Program.Main()