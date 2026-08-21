import platform

print("Distribuição do Sistema Operacional: ", platform.platform())
# ajuda a apontar computadores que não estão atualizados
print("="*100)
print("Nome do Sistema operacional........: ", platform.system())
print("="*100)
print("Versão do Sitema Operacional.......: ", platform.release())
print("="*100)
print("Arquitetura........................: ", platform.architecture())
print("="*100)
print("Nome do Computador.................: ", platform.node())
print("="*100)
# nome do computador na rede
print("Tipo de Máquina....................: ", platform.machine())
print("="*100)
print("Processador........................: ", platform.processor())
print("="*100)
# a identificação do processador pode lhe permitir o direcionamento de patchs de atualização para cada computador que faz parte da rede corporativa
print("Versão do Python...................: ", platform.python_version())
print("="*100)
