import funcs.tts as speek
import funcs.stt as ls
import funcs.chatGPT_bot_2020 as GPT
import funcs.check_internet as check_internet
import funcs.google_search_scrap as google

que = "what is chatgpt"
print("cheaking network")

# time = google.search("what is speed of light")
# print(time)
# speek.speek(time)


# text = google.search("what is the time")
# print(text)
# speek.speek(text)
# text = google.search("what is the speed of light")
# print(text)
# speek.speek(text)
# text = google.search("what is the speed of sound")
# print(text)
# speek.speek(text)
# text = google.search("what is the distance between earth and moon")
# print(text)
# speek.speek(text)



# exit()


mode = 0
while(check_internet.check_internet()):
    if(mode == 0):
        input("\n...")
        que = ls.takeCommand()
    else:
        que = str(input("Enter your query: "))

    print(f"\nyou said: {que}")

    if "inputmode" in que:
        if "0" in que:
            mode = 0
            speek.speek("inputmode 0")
        elif "1" in que:
            speek.speek("inputmode 1")
            mode = 1
        else:
            speek.speek("mode not found")
            print("mode not found")
    print(mode)
    if(que == "exit"):
        break

    ans = GPT.chatGPT(que)
    print("AI = ", end='')
    print(ans)
    speek.speek(ans)
