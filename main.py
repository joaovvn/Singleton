from vagas import Estacionamento
vaga = Estacionamento(10, 'edifício garagem', 'ocupada')
vaga.print()
vaga.change(15, 'estacionamento externo', 'desocupada')
vaga.print()
vaga1 = vaga
vaga1.change(12, 'estacionamento externo', 'interditada')
vaga.print()