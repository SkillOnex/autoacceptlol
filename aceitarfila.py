import pyautogui



print("")
print("  /$$$$$$ /$$   /$$/$$$$$$$$/$$$$$$         /$$$$$$ /$$   /$$/$$$$$$$$/$$   /$$/$$$$$$$$ ")      
print(" /$$__  $| $$  | $|__  $$__/$$__  $$       /$$__  $| $$  | $| $$_____| $$  | $| $$_____/ ")     
print("| $$  \ $| $$  | $$  | $$ | $$  \ $$      | $$  \ $| $$  | $| $$     | $$  | $| $$       ")      
print("| $$$$$$$| $$  | $$  | $$ | $$  | $$      | $$  | $| $$  | $| $$$$$  | $$  | $| $$$$$    ")      
print("| $$__  $| $$  | $$  | $$ | $$  | $$      | $$  | $| $$  | $| $$__/  | $$  | $| $$__/    ")       
print("| $$  | $| $$  | $$  | $$ | $$  | $$      | $$/$$ $| $$  | $| $$     | $$  | $| $$       ")      
print("| $$  | $|  $$$$$$/  | $$ |  $$$$$$/      |  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$| $$$$$$$$ ")
print("|__/  |__/\______/   |__/  \______/        \____ $$$\______/|________/\______/|________/ ")
print("Auto queue ativo [by - SkillOnex]") 
print("")      
print("Para Funcionar a tela do lol deve estar sendo mostrada!")
print("Esse Script foi desenvolvido para você que gosta de dar queue e ir fazer outra coisa !")                                                            
                                                                                                                          
# tempo entre a procura 
pyautogui.PAUSE = 1                                                                                                                  

#loop
while True:
    #foto scan    
    queue_pop = pyautogui.locateOnScreen('queue_pop.png')

    
    #comando se achar
    if queue_pop is not None:

        pyautogui.click(queue_pop)
        print("queue Aceita !")
             
    #se nao achar continua
    else:
        
        continue