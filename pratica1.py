"""
Módulo para verificação de números primos com otimizações avançadas.
Implementação seguindo princípios de Clean Code.
"""


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo usando otimizações matemáticas.
    
    Implementação eficiente com as seguintes otimizações:
    - Trata casos base rapidamente (números < 2, 2, pares)
    - Verifica apenas até raiz quadrada do número
    - Testa apenas números ímpares
    - Complexidade: O(√n)
    
    Args:
        numero (int): O número a ser verificado (deve ser inteiro)
        
    Returns:
        bool: True se o número é primo, False caso contrário
        
    Raises:
        TypeError: Se o argumento não for um inteiro
        
    Exemplos:
        >>> eh_primo(2)
        True
        >>> eh_primo(17)
        True
        >>> eh_primo(10)
        False
    """
    _validar_entrada(numero)
    
    if _eh_caso_base_nao_primo(numero):
        return False
    
    if numero == 2:
        return True
    
    if _eh_par(numero):
        return False
    
    return _nao_possui_divisor(numero)


def _validar_entrada(numero: int) -> None:
    """
    Valida se a entrada é um inteiro.
    
    Args:
        numero (int): Valor a ser validado
        
    Raises:
        TypeError: Se o valor não for um inteiro
    """
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError(f"Esperado inteiro, recebido {type(numero).__name__}")


def _eh_caso_base_nao_primo(numero: int) -> bool:
    """
    Verifica casos base onde o número definitivamente não é primo.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se é um dos casos base não-primo
    """
    return numero < 2


def _eh_par(numero: int) -> bool:
    """
    Verifica se um número é par.
    
    Args:
        numero (int): O número a ser verificado
        
    Returns:
        bool: True se o número é par
    """
    return numero % 2 == 0


def _nao_possui_divisor(numero: int) -> bool:
    """
    Verifica se o número possui algum divisor entre 3 e √numero.
    
    Testa apenas números ímpares (já que números pares foram eliminados).
    
    Args:
        numero (int): O número a ser verificado (deve ser ímpar)
        
    Returns:
        bool: True se não possui divisor (é primo)
    """
    divisor_limite = int(numero ** 0.5) + 1
    
    for divisor in range(3, divisor_limite, 2):
        if numero % divisor == 0:
            return False
    
    return True


def listar_primos(limite: int) -> list[int]:
    """
    Retorna uma lista com todos os números primos até um limite.
    
    Args:
        limite (int): O valor máximo (inclusive)
        
    Returns:
        list[int]: Lista de números primos encontrados
        
    Exemplos:
        >>> listar_primos(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if limite < 2:
        return []
    
    return [numero for numero in range(2, limite + 1) if eh_primo(numero)]


def contar_primos(limite: int) -> int:
    """
    Conta quantos números primos existem até um limite.
    
    Args:
        limite (int): O valor máximo (inclusive)
        
    Returns:
        int: Quantidade de números primos
        
    Exemplos:
        >>> contar_primos(20)
        8
    """
    return len(listar_primos(limite))


if __name__ == "__main__":
    # Testes com números individuais
    print("=" * 50)
    print("VERIFICAÇÃO DE NÚMEROS PRIMOS")
    print("=" * 50)
    
    numeros_teste = [1, 2, 3, 4, 5, 10, 17, 20, 29, 100, 97]
    
    for num in numeros_teste:
        resultado = "✓ PRIMO" if eh_primo(num) else "✗ NÃO PRIMO"
        print(f"{num:3d} -> {resultado}")
    
    # Teste de listagem de primos
    print("\n" + "=" * 50)
    print("NÚMEROS PRIMOS ATÉ 50")
    print("=" * 50)
    primos = listar_primos(50)
    print(f"Primos: {primos}")
    print(f"Total: {len(primos)} números primos\n")
