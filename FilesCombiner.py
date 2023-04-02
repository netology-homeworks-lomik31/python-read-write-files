class Reader:
    def _ReadFile(path: str):
        f = open(path, "r")
        data = f.read()
        f.close()
        return data

    def _GetFullPath(pathToFolder: str, fileNames: list) -> list:
            return list(map(lambda i: f"{pathToFolder}/{i}", fileNames))

    def CreateDictOfFilesData(pathToFolder: str, fileNames: list) -> dict:
        files = Reader._GetFullPath(pathToFolder, fileNames)
        return {fileNames[i]: len(Reader._ReadFile(j).split("\n")) for i, j in enumerate(files)}

class Combiner:
    def __SortFiles(filesData: dict) -> tuple:
        return sorted(filesData, reverse=False, key=lambda x: filesData[x]), filesData

    def Combine(pathToSave: str, filesData: dict, pathToFolder: str) -> None:
        filesData = Combiner.__SortFiles(filesData)
        res = ""
        for i in filesData[0]:
            res += f"{i}\n{filesData[1][i]}\n"
            res += f"{Reader._ReadFile(f'{pathToFolder}/{i}')}\n"
        res = res[:-1]
        Combiner.__WriteFile(res, pathToSave)

    def __WriteFile(data: str, outFile: str) -> None:
        f = open(outFile, "w")
        f.write(data)
        f.close()
        print(f"Successfully saved as {outFile}")

class Program:
    def Main():

        # your code here
        
        pass

if __name__ == "__main__": Program.Main()
