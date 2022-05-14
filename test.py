body = "command hadjfhjka"
command = body.split()[0]
if " " in body:
    prompt = body.split(' ', 1)[1]
else:
    prompt = "EMPTY"
print(prompt)