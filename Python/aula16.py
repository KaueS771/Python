velocidade1 = input('Digite um velocidade para o veiculo: ')
velocidade = float(velocidade1)

local_carro = input('Digite um valor para local carro:')
local_carro1 = float(local_carro)

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >=(LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

if velocidade_carro_pass_radar_1:
    print('Acima da velocidade permitida!')

if carro_passou_radar_1:
    print('Carro passou radar 1')
    
if carro_multado_radar_1:
    print('Carro multado em radar 1')
    
    
    
