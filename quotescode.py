import random

# Collection of quotes for each category
quote_collection = {
    "motivation": [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
    ],
    "success": [
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "The only place where success comes before work is in the dictionary. - Vidal Sassoon"
    ],
    "life": [
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "Life is really simple, but we insist on making it complicated. - Confucius"
    ],
    "love": [
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - Victor Hugo",
        "Love yourself first and everything else falls into line. - Lucille Ball"
    ]
}

def generate_quote():
    name = input("Enter your name: ")
    category = input("Select a category for the quote (motivation, success, life, love): ")

    while category not in quote_collection:
        print("Invalid category! Please try again.")
        category = input("Select a category for the quote (motivation, success, life, love): ")

    quote = random.choice(quote_collection[category])
    quote = quote.replace("{name}", name)

    print("Here's your personalized quote:")
    print(quote)

generate_quote()
