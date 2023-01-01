import funcs.tts as speek
import funcs.stt as ls
import funcs.chatGPT_bot_2020 as GPT
import funcs.check_internet as check_internet
import funcs.google_search_scrap as google

que = "what is chatgpt"
print("cheaking network")

while(check_internet.check_internet()):
    input("\n...")
    mode = 0
    if(mode == 0):
        que = ls.takeCommand()
    else:
        que = str(input("Enter your query: "))

    if(que == "")
    print(f"\nyou said: {que}")

    if(que == "exit"):
        break

    ans = GPT.chatGPT(que)
    print("AI = ", end='')
    print(ans)
    speek.speek(ans)
