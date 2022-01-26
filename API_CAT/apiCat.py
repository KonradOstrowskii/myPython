import requests
import json

headers = {"x-api-key": "05da2018-c2c8-49ff-b4XX-4895ee4882e7"}


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Incorrect format", response.text)
    else:
        return content


def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get('https://api.thecatapi.com/v1/favourites/', params,
                     headers=headers)

    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers=headers)

    return get_json_content_from_response(r)


def add_favourite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }

    r = requests.post('https://api.thecatapi.com/v1/favourites/', json=catData,
                      headers=headers)

    return get_json_content_from_response(r)


userId = "agh2m"
name = "Konrad"

print("Hello " + name)
favouriteCats = get_favourite_cats(userId)
print("Your favourite cats are : ", favouriteCats)
randomCat = get_random_cat()
print("Random cat: ", randomCat[0]["url"])

addToFavourites = input(
    "Would You like to add this cat to Your favourite list : yes/no  ")

if (addToFavourites == "yes"):
    print(add_favourite_cat(randomCat[0]["id"], userId))
