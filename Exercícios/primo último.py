def maior_primo(n):
    if n <= 2:
        return n
    if n % 2 == 0:
        return maior_primo(n-1) #not prime, check again for next biggest number
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return maior_primo(n-1) #not prime, check sagain for next biggest number
        i+=2
    return n