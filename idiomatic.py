print(*[f'The square of {k} is {v}.' for k,v in {x: x*x for x in range(int(100**.5))}.items()], sep='\n')
