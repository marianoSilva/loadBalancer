ref_arquivo = open("input.txt","r")
usuarios = []
usuarios = ref_arquivo.readlines()
TTICK = int(usuarios[0])
UMAX = int(usuarios[1])
servers = []

tick = 2
ciclo = 2

while tick < len(usuarios):
	
	if tick == 2:
		if int(usuarios[2]) <= UMAX:
			servers.append(int(usuarios[2]))
	else:
		tarefas = int(usuarios[tick])
		server = 0

		if(tick >= (TTICK+2)):
			remover_tarefa = int(usuarios[ciclo])
			remover_server = 0
			while remover_server < len(servers):
				if servers[remover_server] > 0 and remover_tarefa > 0:
					if remover_tarefa >= servers[remover_server]:
						remover_tarefa = remover_tarefa - servers[remover_server]
						servers.pop()
					else:
						servers[remover_server] = servers[remover_server] - remover_tarefa
						remover_tarefa = 0

				remover_server = remover_server + 1
			ciclo = ciclo + 1


		while server < len(servers):
			if servers[server] < int(UMAX):
				if tarefas >= (UMAX - servers[server]):
					tarefas = tarefas - (UMAX - servers[server])
					servers[server] = UMAX	
			if server == (len(servers)-1):
				while tarefas > 0:
					if (tarefas - UMAX) >= 0:
						servers.append(UMAX)
						tarefas = tarefas - UMAX
					else:
						servers.append(tarefas)
						tarefas = 0
				


			server = server + 1


	tick = tick + 1

	


	print(servers)


while tick >= len(usuarios) and len(servers) > 0:
	remover_tarefa = int(usuarios[ciclo])
	remover_server = 0
	while remover_server < len(servers):
		if servers[remover_server] > 0 and remover_tarefa > 0:
			if remover_tarefa >= servers[remover_server]:
				remover_tarefa = remover_tarefa - servers[remover_server]
				servers.pop()
			else:
				servers[remover_server] = servers[remover_server] - remover_tarefa
				remover_tarefa = 0

		remover_server = remover_server + 1
	ciclo = ciclo + 1
	print(servers)













