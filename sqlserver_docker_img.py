import os

def download_docker_image() :
	os.system("docker pull microsoft/mssql-server-linux")

def download_sql_cli() :
	os.system("npm install -g sql-cli")

def get_password() :
	password = input("Input SQL Password : ")
	return password

password = get_password()

def start_sql() :
	os.system("docker run -p 1433:1433 -e SA_PASSWORD='" + password + "' -e ACCEPT_EULA=Y microsoft/mssql-server-linux")

def sqlcli() :
	os.system("mssql -p '" + password + "'")

def list_docker_id() :
	os.system("docker ps -a")

def get_docker_id() :
	docker_id = input("Input Container ID : ")
	return docker_id

def start_docker_image() :
	os.system("docker start " + get_docker_id())

def stop_docker_image() :
	os.system("docker stop " + get_docker_id())

def install_homebrew() :
	os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
	os.system("brew update")

def install_openssl() :
	os.system("brew install openssl")
	os.system("ln -s /usr/local/opt/openssl/lib/libcrypto.1.0.0.dylib /usr/local/lib/")
	os.system("  ln -s /usr/local/opt/openssl/lib/libssl.1.0.0.dylib /usr/local/lib/")

def sqlgui() :
	os.system("open -a Visual\ Studio\ Code")

os.system("open -a Docker")
print("Docker Launched")
user_choice = 99
while (user_choice != 0) :
	print("1. Install SQL Server Image")
	print("2. Install mssql")
	print("3. Install Homebrew")
	print("4. Install OpenSSL")
	print("5. Run Image (1st Time)")
	print("6. Launch CLI")
	print("7. Launch GUI")
	print("8. Run Image")
	print("9. Stop Image")
	print("0. Exit")

	user_choice = int(input("Input Choice : "))
	if (user_choice == 1) :
		download_docker_image()
	elif (user_choice == 2) :
		download_sql_cli()
	elif (user_choice == 3) : 
		install_homebrew()
	elif (user_choice == 4) :
		install_openssl()
	elif (user_choice == 5) :
		start_sql()
	elif (user_choice == 6) :
		sqlcli()
	elif (user_choice == 7) :
		sqlgui()
	elif (user_choice == 8) :
		list_docker_id()
		start_docker_image()
	elif (user_choice == 9) :
		list_docker_id()
		stop_docker_image()
	else :
		print("Goodbye ;-P")