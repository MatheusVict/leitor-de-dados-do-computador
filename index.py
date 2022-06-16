import wmi

#Aqui carrega as informações
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

#Aqui vai exibir as informações
print(f"Marca: {my_system.Manufacturer}")
print(f"Modelo: {my_system.Model}")
print(f"Nome: {my_system.Name}")
print(f"Qtde CPUs: {my_system.NumberOfProcessors}")
print(f"Arquitetura da placa: {my_system.SystemType}")
print(f"Família do modelo computador: {my_system.SystemFamily}")