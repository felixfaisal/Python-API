import requests

def main():
   res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":"GHWJKEZAp54QUjwwKZWFg", "isbns": "9781632168146"})
   data = res.json()
   rate= data["books"]
   new= rate["isbn"]
   print(new)

if __name__ == "__main__":
    main()
