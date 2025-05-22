PROGRAMMINGLANGUAGES = [
    " python",
    "   java",
    "c++",
    "  rust",
    "sQL",
    "  assembly"
]

def main():
    cleaned_programming_languages = []
    for programming_languages in PROGRAMMINGLANGUAGES:
        cleaned_programming_languages.append(programming_languages.title().split())

    print(cleaned_programming_languages)

main()