def encontrar_ruta(C, m, n, index, Result):
    if n == len(C) or C[0][0]==1 and index==m:
        return Result
    for i in range(index, m):
        if C[n][i] != 1 and i != (m-1):
            Result += [(n,i)]
            return encontrar_ruta(C, m, n, i+1, Result)
        elif C[n][i] != 1 and i == (m-1):
            Result += [(n,i)]
            return encontrar_ruta(C, m, n+1, i, Result)
        else:
            if (n!=len(C)-1 and C[n+1][i-1]==1 and i>0):
                Result.pop(i-1)
                return encontrar_ruta(C, m, n + 1, i - 2, Result)
            return encontrar_ruta(C, m, n + 1, i-1, Result)

    return []
