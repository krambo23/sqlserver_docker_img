import os

def download_docker_image() :
	os.system("docker pull microsoft/mssql-server-linux")

def download_sql_cli() :
	os.system("npm install -g sql-cli")

def get_password() :
	password = input("Input Password : ")
	return password

password = get_password()

def start_sql() :
	os.system("docker run -p 1433:1433 -e SA_PASSWORD='" + password + "' -e ACCEPT_EULA=Y microsoft/mssql-server-linux")

def sqlcli() :
	os.system("mssql -p '" + password + "'")

def list_docker_id() :
	os.system("docker ps -a")

def get_docker_id() :
	docker_id = input("Input Docker ID : ")
	return docker_id

def start_docker_image() :
	os.system("docker start " + get_docker_id())

def stop_docker_image() :
	os.system("docker stop " + get_docker_id())

print("Please ensure Docker is launched")
print("1. Install SQL Server Image")
print("2. Install mssql")
print("3. Run Image (1st Time)")
print("4. Launch CLI")
print("5. Run Image")
print("6. Stop Image")
print("0. Exit")

user_choice = int(input("Input Choice : "))
if (user_choice == 1) :
	download_docker_image()
elif (user_choice == 2) :
	download_sql_cli()
elif (user_choice == 3) :
	start_sql()
elif (user_choice == 4) :
	sqlcli()
elif (user_choice == 5) :
	list_docker_id()
	start_docker_image()
elif (user_choice == 6) :
	list_docker_id()
	stop_docker_image()
else :
	print("Goodbye ;-P")