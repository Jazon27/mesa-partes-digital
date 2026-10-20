def ordenar_expedientes(codigos, nombres, dni, celular, correo, asunto):
    print("\n --------Lista de Expedientes Registrados--------")
    print("-" * 50)
    if len(codigos) == 0:
        print("\nNo hay expedientes registrados......")
        return
    
    print(f"{'codigo':<12}  {'nombre':<20}  {'asunto'}")
    print("-" * 50)
    for i in range(len(codigos) - 1, -1, -1):
        print(f"{codigos[i]:<12} | {nombres[i]:<20} | {asunto[i]}")
        print("-" * 50)
    
    print(f"Total de expedientes: {len(codigos)}")