velocidade = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGER = 1

multar = local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER)
vel_carro_passou = velocidade > RADAR_1

if velocidade > RADAR_1:
 print ("Velocidade carro passou radar 1")

if  multar and vel_carro_passou: 
    print("O carro foi mutado em radar 1")