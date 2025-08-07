emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis disponíveis:")
for nome, emoji in emojis.items():
    print(f"{emoji} - {nome}")

frase = input("Digite uma frase e ela será emojizada: ")

for nome, emoji in emojis.items():
    frase = frase.replace(nome,emoji)
print("Frase emojizada:")
print(frase)