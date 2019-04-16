import requests

api_url = "http://localhost:5000/tasksApi/v1/"


if __name__ == "__main__":
    tasks = requests.get(api_url+"tasks").json()
    print(tasks)
    requests.post(api_url+"tasks", json={'description': 'test lab 6', 'urgent': 1})
    tasks = requests.get(api_url+"tasks").json()
    print(tasks)
    for row in tasks:
        if row["description"] == "test lab 6":
            ident = row["id"]
            break
    print(requests.get(api_url + "tasks/"+str(ident)).json())
    requests.put(api_url + "tasks/" + str(ident), json={"description": "test lab 6", "urgent": 0})
    print(requests.get(api_url + "tasks").json())
    requests.delete(api_url + "tasks/"+str(ident))
    print(requests.get(api_url + "tasks").json())
