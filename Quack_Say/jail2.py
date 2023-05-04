def quack_say(to_print):
    print(f"""
    {to_print}
      \\
       --
     >(' )
       )/   ,
      /(____/\\
     /        )
     \ `  =~~/
      `---Y-'
    -----~~'----
    """)


while(True):
    inp = input("Enter expression : ")
    for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write','process','socket','help']:
        if keyword in inp.lower():
            quack_say("Stop hacking !!")
            exit()
    quack_say(inp + " = " + str(eval(inp)))