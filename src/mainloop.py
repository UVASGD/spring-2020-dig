from "world.py" import World

exit = False
input_icon = "😐️ >"

current_tile = None

while not exit:
    
    
    
    command = input(input_icon)
    
    tokens = command.split(' ')
    
    if tokens[0] in commands:
        execute(tokens)
    else:
        print("I can't do that right now.")
    
    
    