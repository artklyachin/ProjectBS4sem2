import app_module
from request import Request

print("main!")

req = Request()
temperature_list = req.get_temp()
print(temperature_list)
for elem in temperature_list:
    print(elem)

app_module.app.run()


