def checkKeywordsInCommand(commandstr: str, keywords: list[str]) -> bool:
    command = commandstr.split()
    if keywords[0] in command:
        for keyword in keywords:
            for word in command:
                if keyword == word.lower():
                    index = command.index(keyword)
                    command = command[index + 1 :]  # type: ignore
                    break
            else:
                return False
        return True
    else:
        return False


print(checkKeywordsInCommand("what is the time", ["what", "time"]))
