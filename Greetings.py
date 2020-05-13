GUEST_LIST = {
	"Randy": "Germany", 
	"Karla": "France", 
	"Wendy": "Japan", 
	"Norman": "England", 
	"Sam": "Argentina"
}
def greeting(name):
	if name in GUEST_LIST:
return "Hi! I'm " + name+ ", and I'm from " + GUEST_LIST[name] + "."
