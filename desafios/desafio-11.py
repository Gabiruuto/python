largura = float(input('Largura da parede: '))

altura = float(input('Altura da parede: '))

me = altura * largura

wa = me / 2 

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \n Para pintar sua parede, você precisará de {}l de tinta.'.format(largura, altura, me, wa))