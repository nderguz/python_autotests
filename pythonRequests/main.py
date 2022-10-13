from xml.etree.ElementPath import find
import requests
create_pet = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 13,
  "category": {
    "id": 13,
    "name": "MyNewPet"
  },
  "name": "Chappie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 13,
      "name": "string"
    }
  ],
  "status": "available"
})
print(create_pet.text)

edit_pet = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 13,
  "category": {
    "id": 13,
    "name": "MyNewPetsName"
  },
  "name": "Chappie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 13,
      "name": "string"
    }
  ],
  "status": "available"
} )
print(edit_pet.text)

find_pet = requests.get("https://petstore.swagger.io/v2/pet/13")

print(find_pet.text)