favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + 
        language.title() + '.')

for name in favourite_languages.keys():
    print(name.title())

print(list(favourite_languages.values()))

print("The following languages have been  mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())