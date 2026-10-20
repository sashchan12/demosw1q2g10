from pyscript import document, display

my_list = ["Bryson", "Daniel", "Frank"]

def show_list():
    output= document.getElementById("output")
    output.innerHTML=""

    for item in my_list:
        display(item, target="output")

def append_value(e):
    value=document.getElementById("user_input").value.strip()
    message= document.getElementById("message")

    if value:
        my_list.append(value)
        message.innerHTML = "Data Added Successfully"
        show_list()

    else:
        message.innerHTML="Please add a Value"
    document.getElementById("user_input").value=""

def delete_value(e):
    value=document.getElementById("user_input").value.strip()
    message= document.getElementById("message")

    if value in my_list:
        my_list.remove(value)
        message.innerHTML = "Data Deleted!"
        show_list()

    else:
        message.innerHTML="Value not found or available in the list."

    document.getElementById("user_input".value)=""

show_list()