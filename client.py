import requests

url = "http://127.0.0.1:8000/students/"

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")

response = requests.post(url, json={"name": name, "age": age, "course": course})
print("Response:", response.json())

response = requests.get(url)
print("All Students:", response.json())
