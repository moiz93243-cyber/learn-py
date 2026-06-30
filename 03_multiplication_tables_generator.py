for i in range(2, 11):
    
    file_name = f"table_of_{i}.txt"
    
    try:
        with open(file_name, "w") as f:
            for j in range(1, 11):
                f.write(f"{i} x {j} = {i*j}\n")
                
        print(f"successful!! generated: {file_name}")
        
    except (OSError, ValueError):
        print(f"wrong code or error writing {file_name}")       
        
        
        