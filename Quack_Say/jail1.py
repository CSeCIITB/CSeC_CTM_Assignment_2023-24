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
    quack_say(inp + " = " + str(eval(inp)))